#!/usr/bin/env python

"""Generate podcast feed from directory of media files"""

import argparse, yaml, os
import validators
from pypodcaster.channel import Channel

__author__ = 'mantlepro'

global VERSION
VERSION = "0.5.1"

parser = argparse.ArgumentParser(
    description="%(prog)s - free, open source podcast rss generator by Josh Wheeler <mantlepro@gmail.com>",
    epilog="example: %(prog)s > index.rss"
)
parser.add_argument("sources",
                    nargs="?",
                    help="Specify source files or directories",
                    default=os.getcwd()
                    )
parser.add_argument("-c", "--channel", metavar="/path/to/channel.yml", help="Specify channel definition instead of current directory's channel.yml")
parser.add_argument("-o", "--output", help="Direct output to FILE instead of stdout")
parser.add_argument('-V', "--version",
                    action="version",
                    version="%(prog)s " + VERSION,
                    )
args = parser.parse_args()


# TODO: Are urls valid?
# TODO: Does cover image exist?

if args.channel:
    options = yaml.safe_load(open(args.channel))
elif os.path.isfile(os.getcwd() + "/channel.yml"):
    options = yaml.safe_load(open(os.getcwd() + "/channel.yml"))
else:
    parser.print_help()
    print "No channel.yml found"

def trailing_slash(url):
    """remove trailing slash from url"""
    if url.endswith('/'):
        url = url.rstrip('/')
    return url

def validate(url):
    validators.url(url)

# following line for testing only
options = yaml.safe_load(open("/home/mantlepro/Documents/pypodcaster/channel.yml"))
options['podcast_url'] = trailing_slash(options['podcast_url'])

#Channel(args.sources, options)
if args.output:
    with open(args.output, 'w') as output_file:
        output_file.write("%s\n" % Channel(args.sources, options).render_xml())
else:
    print Channel(args.sources, options).render_xml()