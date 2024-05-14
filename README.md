# Plex2Letterboxd

Exports watched movies from Plex to the [Letterboxd Import Format][import].

Movies are exported to a CSV file containing:
* Movie Title
* Release Year
* User Rating
* Last Watched Date

## Installation

```console
$ git clone https://github.com/mtimkovich/plex2letterboxd.git
$ cd plex2letterbox
$ pip install .
```

### Docker

Build the Docker image and pass a `letterboxd.csv` file into the Docker run command to store the generated CSV.

```console
$ docker build -t plex2letterboxd .
$ docker run -v $(pwd)/config.ini:/app/config.ini -v $(pwd)/letterboxd.csv:/app/letterboxd.csv plex2letterboxd
```

## Usage

Rename `config.ini.example` to `config.ini` and fill it with your Plex credentials.

```console
$ python -m plex2letterboxd
```

```
optional arguments:
  -h, --help            show this help message and exit
  -i INI, --ini INI     config file (default: config.ini)
  -o OUTPUT, --output OUTPUT
                        file to output to (default: letterboxd.csv)
  -s SECTIONS [SECTIONS ...], --sections SECTIONS [SECTIONS ...]
                        sections to grab from (default: ['Movies'])
  -m MANAGED_USER, --managed-user MANAGED_USER
                        name of managed user to export (default: None)
  -w WATCHED_AFTER, --watched-after WATCHED_AFTER
                        only return movies watched after the given time [format:
                        YYYY-MM-DD or 30d] (default: None)
```

The generated CSV file can be uploaded to Letterboxd at https://letterboxd.com/import/.

## Author

[Max Timkovich][profile]

[import]: https://letterboxd.com/about/importing-data/
[profile]: https://letterboxd.com/djswerve/
