#!/usr/bin/env python

import argparse

import yaml

import pypodcaster

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
parser.add_argument("-c", "--channel", help="Read the channel definition from FILE instead current directory's channel.yml")
args = parser.parse_args()

if args.channel:
    options = yaml.safe_load(open(args.channel))
else:
    options = yaml.safe_load(open("channel.yml"))

print(pypodcaster.Channel(sources, options))

