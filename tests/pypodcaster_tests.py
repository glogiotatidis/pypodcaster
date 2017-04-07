__author__ = 'mantlepro'

import yaml
import os
from pypodcaster import channel, item


def test_channel():
    path = os.path.dirname(__file__)
    options = yaml.safe_load(open("%s/channel.yml" % path))
    channel.Channel(os.getcwd(), options)


def test_item():
    path = os.path.dirname(__file__)
    options = yaml.safe_load(open("%s/channel.yml" % path))
    mp3_file = "%s/test.mp3" % path
    item.Item(mp3_file, options)
