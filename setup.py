from setuptools import setup

with open('README.md') as f:
    README = f.read()

setup(
    name='plex_to_letterboxd',
    url='https://github.com/mtimkovich/plex_to_letterboxd',
    version='1.0',
    author='Max Timkovich',
    author_email='max@timkovi.ch',
    license='MIT',
    description='Export watched movies on Plex to the Letterboxd import format.',
    long_description=README,
    install_requires=['plexapi'],
    entry_points={'console_scripts': [
        'plex_to_letterboxd=plex_to_letterboxd:main'
    ]},
)
