
#!/usr/bin/env python
'''No docstring has been added yet.'''

import click
import os
from urllib.parse import unquote

import myhacks as myh

@click.command()
@click.argument('feedspoturl', required=True)
def run_parseFeedSpot(feedspoturl):
    '''test docstring'''

    print("Feedspot URL: ", feedspoturl)

    site_url = unquote(feedspoturl.split("site:")[1])
    print("Site URL: ", site_url)


if __name__ == '__main__':
    run_parseFeedSpot()