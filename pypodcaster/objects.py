#!/usr/bin/env python

__author__ = 'mantlepro'

import glob
from jinja2 import Environment, PackageLoader
import eyeD3, os
from datetime import datetime
from time import strftime, gmtime
import ntpath

source_files = []

class Channel:
    
    """Podcast channel. Sources can be a string or list
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
            """Return all items of the channel newest-to-oldest"""
            all_items = []
            for src in source_files:
                all_items.append(Item(src, options))
                sorted(all_items, key=lambda item: item.options.get("pub_date"))
            return all_items

        # load templates
        env = Environment(loader=PackageLoader('pypodcaster', 'templates'))
        template_xml = env.get_template('template.xml')
        # set up template variables
        print template_xml.render(channel=options,
                                  items=items(),
                                  last_build_date=strftime("%a, %d %b %Y %T %Z"),
                                  generator="pypodcaster"
                                  )
def add_files(src):
    """add absolute paths to source_files list"""
    if os.path.isdir(src):
        os.chdir(src)
        for file in glob.glob("*.mp3"):
            source_files.append(file)
    else:
        source_files.append(src)

class Item:
    
    """Item object containing vars related to id3 tag"""
    
    def __init__(self, file_path, options):
        
        self.options = options
        
        if eyeD3.isMp3File(file_path):
            mp3_file = eyeD3.Mp3AudioFile(file_path)
            id3 = mp3_file.getTag()
            id3.link(file_path)
            # TODO: check for episodic images and add default if none provided
            self.image_url = "%s%s" % (options.get("podcast_url"),options.get("image"))
            self.title = id3.getTitle()
            self.album = id3.getAlbum()
            self.comment = id3.getComment()
            self.artist = id3.getArtist()
            self.subtitle = options.get("subtitle")
            self.url = "%s%s" % (options.get("podcast_url"),ntpath.basename(file_path))
            # date should be in RFC 822 format (e.g. Sat, 07 Sep 2002 0:00:01 GMT)
            self.pub_date = datetime.fromtimestamp(os.stat(file_path).st_mtime).strftime("%a, %d %b %Y %T ") + strftime('%Z')
            self.length = os.stat(file_path).st_size
            self.seconds = mp3_file.getPlayTime()
            self.duration = strftime('%M:%S', gmtime(float(self.seconds)))
