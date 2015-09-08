#!/usr/bin/env python

__author__ = 'mantlepro'

import glob
from jinja2 import Environment, PackageLoader
import eyeD3, os, time
from datetime import datetime
from time import strftime, gmtime
from email.utils import formatdate
from dateutil import tz


source_files = []

class Channel:

    """Channel object. Sources can be a string or list of strings,
    pointing to a one or more directories or mp3 files."""

    def __init__(self, sources, options):
        # if sources is list or single file/directory
        if isinstance(sources, list):
            for s in sources:
                add_files(s)
        else:
            # single file or dir
            add_files(sources)


        def items():
            "Returns all items of the channel newest-to-oldest"
            all_items = []
            for src in source_files:
                all_items.append(Item(src, options))
                # not tested yet all_items.sort(self, key=lambda item: item.pub_date)
            return all_items

        # load templates
        env = Environment(loader=PackageLoader('pypodcaster', 'templates'))
        template_xml = env.get_template('template.xml')

        print template_xml.render(channel=options, items=items())

def add_files(src):
    "add absolute paths to list"
    if os.path.isdir(src):
        os.chdir(src)
        for file in glob.glob("*.mp3"):
            source_files.append(file)
    else:
        source_files.append(src)

class Item:
    """Item object containing vars related to id3 tag"""

    def __init__(self, file_path, options):
        if eyeD3.isMp3File(file_path):
            mp3_file = eyeD3.Mp3AudioFile(file_path)
            self.seconds = mp3_file.getPlayTime()
            id3 = mp3_file.getTag()
            id3.link(file_path)
            # TODO: check for existing cover_image for episodic images and add default if none provided
            # if options.image_url:
            #     id3.removeImages()
            #     id3.addImage(0x03, options.image_url)
            #     id3.update()
            self.title = id3.getTitle()
            self.album = id3.getAlbum()
            self.comment = id3.getComment()
            self.artist = id3.getArtist()
            # TODO: check for mp3 date tag. If none, set to file's mtime or default in channel.yml
            # date should be in RFC 822 format (e.g. Sat, 07 Sep 2002 0:00:01 GMT)
            timezone=strftime('%Z')
            self.pub_date = datetime.fromtimestamp(os.stat(file_path).st_mtime).strftime("%a, %d %b %Y %T ") + timezone
            self.length = os.stat(file_path).st_size
            # replace with id3 method?
            self.duration = strftime('%M:%S', gmtime(float(self.seconds)))
