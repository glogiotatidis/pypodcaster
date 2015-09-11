__author__ = 'mantlepro'

import yaml
from nose.tools import *
from pypodcaster.channel import Channel, Item

def test_channel():
    options = yaml.safe_load(open("/home/mantlepro/Documents/pypodcaster/channel.yml"))
    Channel('/home/mantlepro/Desktop', options)

def test_item():
    options = yaml.safe_load(open("/home/mantlepro/Documents/pypodcaster/channel.yml"))
    Item('/home/mantlepro/Desktop/Spotlight.mp3', options)

def test_pypodcaster():
    args