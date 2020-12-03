# Plex to Letterboxd

Exports watched movies from Plex to the [Letterboxd Import Format][import].

Movies are exported to a CSV file containing:
* Movie's Title
* Release Year
* User Rating
* Last Watched Date

## Installation

```
$ git clone https://github.com/mtimkovich/plex_to_letterboxd.git
$ cd plex_to_letterbox
$ pip install .
```

## Usage

Rename `config.ini.example` to `config.ini` and fill it with your Plex credentials.

```
$ python -m plex_to_letterboxd -i config.ini
```

```
optional arguments:
  -h, --help            show this help message and exit
  -i INI, --ini INI     config file
  -o OUTPUT, --output OUTPUT
                        file to output to
```

## Author

[Max Timkovich][profile]

[import]: https://letterboxd.com/about/importing-data/
[profile]: https://letterboxd.com/djswerve/
