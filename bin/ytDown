#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python
from pytube import YouTube

import click

@click.command()
def ytdown():
    '''Downloads youtube videos.'''

    YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.first().download()


if __name__ == '__main__':
    ytdown()
