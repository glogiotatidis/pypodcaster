#!/usr/bin/env python

"""Generate podcast feed from directory of media files"""

import argparse
import logging
import os
import time

import validators
import yaml
from pkg_resources import get_distribution

from pypodcaster.channel import Channel

__author__ = 'mantlepro'

VERSION = get_distribution('pypodcaster').version

def main():
    sources_list = [os.getcwd()]

    logging.basicConfig(filename='podcast.log', format='%(levelname)s: %(message)s', filemode="w", level=logging.DEBUG)
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
        version=VERSION,
    )
    args = parser.parse_args()

    if not args.sources == sources_list:
        sources_list = args.sources

    logging.debug("Sources: " + str(sources_list))

    if args.channel:
        options = yaml.safe_load(open(args.channel))
    elif os.path.isfile(os.getcwd() + "/channel.yml"):
        options = yaml.safe_load(open(os.getcwd() + "/channel.yml"))
    elif os.path.isfile(args.sources[0] + "/channel.yml"):
        options = yaml.safe_load(open(args.sources[0] + "/channel.yml"))
    else:
        options = ""
        parser.print_help()
        print "\nNo channel.yml found"
        exit(1)

    def trailing_slash(url):
        """remove trailing slash from url"""
        if url.endswith('/'):
            url = url.rstrip('/')
        return url

    # TODO: Validate channel file.
    # TODO: Is link url valid?
    # TODO: Does channel's cover image exist?

    def validate(url):
        validators.url(url)

    # remove trailing slashes to support either format in channel.yml
    options['podcast_url'] = trailing_slash(options['podcast_url'])

    if args.output:
        with open(args.output, 'w') as output_file:
            output_file.write("%s\n" % Channel(sources_list, options).render_xml().encode('ascii', 'xmlcharrefreplace'))
    else:
        print Channel(sources_list, options).render_xml().encode('ascii', 'xmlcharrefreplace')

    logging.info("Finished %s" % time.strftime("%a, %d %b %Y %T %Z"))

if __name__ == "__main__":
    main()
