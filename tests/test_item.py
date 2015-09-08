#!/usr/bin/env python
__author__ = 'mantlepro'

import yaml, time
from pypodcaster.objects import Item
from time import strftime, gmtime, localtime
from datetime import datetime

options = yaml.safe_load(open("/home/mantlepro/Documents/pypodcaster/channel.yml"))
item = Item('/home/mantlepro/Desktop/Spotlight.mp3', options)

print item.pub_date