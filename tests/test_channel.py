#!/usr/bin/env python

__author__ = 'mantlepro'

import yaml

from pypodcaster.objects import Channel

options = yaml.safe_load(open("/home/mantlepro/Documents/pypodcaster/channel.yml"))
channel = Channel('/home/mantlepro/Desktop/Spotlight.mp3', options)