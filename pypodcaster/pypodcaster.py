#!/usr/bin/env python

"""Generate podcast feed"""

import argparse, yaml
from pypodcaster.objects import Channel

__author__ = 'mantlepro'

HELP = """pypodcaster is a podcast feed generator for the command line.
Author: Josh Wheeler <mantlepro@gmail.com>

Basic Usage:

  pypodcaster               Output a podcast feed for mp3 files in the current directory.
  pypodcaster [FILE(s)]...  Output a podcast feed for specified FILE(s)
  pypodcaster [DIR]...      Output a podcast feed for mp3 files in DIR

Examples:

  pypodcaster > index.rss
"""

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--channel", help="Specify channel definition instead of current directory's channel.yml")
parser.add_argument("-o", "--output", help="Output to FILE instead of stdout")
args = parser.parse_args()

# TODO: Add validation layer:
  # TODO: Are urls valid?
  # TODO: Does cover image exist?
  # TODO: Can I write to specified output?

if args.channel:
    options = yaml.safe_load(open(args.channel))
else:
    options = yaml.safe_load(open(os.getcwd() + "/channel.yml"))

# remove trailing slash from channel.yml
if options.get("podcast_url").endswith('/'):
  # replace trailing slash with ''
  options = options

if args.output:
  # TODO: Add file writer
else:
  print Channel(sources, options)
