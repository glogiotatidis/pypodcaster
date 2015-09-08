__author__ = 'mantlepro'

from nose.tools import *
import pypodcaster

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"