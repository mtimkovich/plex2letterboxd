"""Export watched Plex movies to the Letterboxd import format."""
import argparse
import configparser
import csv
import sys

from plexapi.myplex import MyPlexAccount


def parse_args():
    parser = argparse.ArgumentParser(
        description='Export watched Plex movies to the Letterboxd import '
                    'format.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--ini', default='config.ini',
                        help='config file')
    parser.add_argument('-o', '--output', default='letterboxd.csv',
                        help='file to output to')
    parser.add_argument('-s', '--sections', default=['Movies'], nargs='+',
                        help='sections to grab from')
    return parser.parse_args()


def parse_config(ini):
    """Read and validate config file."""
    config = configparser.ConfigParser()
    config.read(ini)
    auth = config['auth']
    missing = {'username', 'password', 'server'} - set(auth.keys())
    if missing:
        print(f'Missing the following config values: {missing}')
        sys.exit(1)
    return auth


def write_csv(sections, output):
    """Generate Letterboxd import CSV."""
    with open(output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Year', 'Rating10', 'WatchedDate'])

        count = 0
        for section in sections:
            for movie in section.search(sort='lastViewedAt', unwatched=False):
                date = movie.lastViewedAt.strftime('%Y-%m-%d')
                rating = movie.userRating
                if rating is not None:
                    rating = f'{movie.userRating:.0f}'
                writer.writerow([movie.title, movie.year, rating, date])
                count += 1
    print(f'Exported {count} movies to {output}.')


def main():
    args = parse_args()
    auth = parse_config(args.ini)

    account = MyPlexAccount(auth['username'], auth['password'])
    plex = account.resource(auth['server']).connect()

    sections = [plex.library.section(s) for s in args.sections]
    write_csv(sections, args.output)
