#!/usr/bin/env python

__author__ = 'mantlepro'

import glob
from jinja2 import Environment, PackageLoader
from pypodcaster.pypodcaster.pypodcaster import item
import eyeD3, os, time
from time import strftime, gmtime

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

        # load templates
        env = Environment(loader=PackageLoader('pypodcaster', 'templates'))
        template_xml = env.get_template('template.xml')

        print template_xml.render(the='variables', go='here')

        def items():
            "Returns all items of the channel newest-to-oldest"
            all_items = []
            for src in source_files:
                all_items.append(item.Item(src))
                # not tested yet all_items.sort(self, key=lambda item: item.pub_date)


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
            # pub_date = "Thu, " + day + now.strftime(" %b %Y 19:00:00 -0600")
            self.pub_date = time.ctime(os.path.getmtime(file_path))
            self.length = os.stat(file_path).st_size
            # replace with id3 method?
            self.duration = strftime('%M:%S', gmtime(float(self.seconds)))
