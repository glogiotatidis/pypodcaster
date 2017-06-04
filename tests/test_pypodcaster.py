#!/usr/bin/python

import yaml
import os
from pypodcaster.podcast import Channel, Item


def test_channel():
    path = os.path.dirname(__file__)
    sources_list = [path]
    options = yaml.safe_load(open("%s/channel.yml" % path))
    print(Channel(sources_list, options).render_xml())


def test_item():
    path = os.path.dirname(__file__)
    options = yaml.safe_load(open("%s/channel.yml" % path))
    mp3_file = "%s/test.mp3" % path
    Item(mp3_file, options)
