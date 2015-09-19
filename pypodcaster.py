#!/usr/bin/env python

"""Generate podcast feed from directory of media files"""

import argparse, yaml, os
import logging
import validators
from pypodcaster.channel import Channel
import time

__author__ = 'mantlepro'

global VERSION
VERSION = "0.5.1"

sources_list = [os.getcwd()]

logging.basicConfig(filename='podcast.log',format='%(levelname)s: %(message)s', filemode="w", level=logging.DEBUG)
logging.info("Started %s" % time.strftime("%a, %d %b %Y %T %Z"))
parser = argparse.ArgumentParser(
    description="%(prog)s - free, open source podcast rss generator by Josh Wheeler <mantlepro@gmail.com>",
    epilog="example: %(prog)s > index.rss"
)
# TODO: log levels from commandline
parser.add_argument("sources",
                    nargs="*",
                    help="Specify source files or directories",
                    default=sources_list
                    )
parser.add_argument("-c", "--channel", metavar="/path/to/channel.yml", help="Specify channel definition instead of current directory's channel.yml")
parser.add_argument("-o", "--output", help="Direct output to FILE instead of stdout")
parser.add_argument('-V', "--version",
                    action="version",
                    version="%(prog)s " + VERSION,
                    )
args = parser.parse_args()

if not args.sources == sources_list:
    sources_list = args.sources

logging.debug("Sources: " + str(sources_list))

# TODO: Validate channel file.
# TODO: Is link url valid?
# TODO: Does channel's cover image exist?

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

# remove trailing slashes to support either format in channel.yml
options['podcast_url'] = trailing_slash(options['podcast_url'])

if args.output:
    with open(args.output, 'w') as output_file:
        output_file.write("%s\n" % Channel(sources_list, options).render_xml())
else:
    print Channel(sources_list, options).render_xml()

logging.info("Finished %s" % time.strftime("%a, %d %b %Y %T %Z"))