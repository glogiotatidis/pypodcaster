import logging
import validators
from pypodcaster.item import Item

__author__ = 'mantlepro'

import os, glob
from time import strftime
from jinja2 import Environment, PackageLoader

source_files = []

class Channel:
    """Podcast channel. Sources can be a string or list
    pointing to a one or more directories or mp3 files."""

    def __init__(self, sources, options):
        self.sources = sources
        self.options = options

        for source in sources:
            logging.debug("Adding %s to source_files" % source)
            add_files(source)

    def items(self, options):
        """Return all items of the channel newest-to-oldest"""
        all_items = []
        for src in source_files:
            all_items.append(Item(src, options))
        logging.debug("Sorting all_items from newest-to-oldest")
        sorted(all_items, key=lambda item: item.pub_date)
        return all_items

    def render_xml(self):
        """render xml template with items"""
        env = Environment(loader=PackageLoader("pypodcaster", 'templates'))
        template_xml = env.get_template('template.xml')
        # set up template variables
        return template_xml.render(channel=self.options,
                                  items=self.items(self.options),
                                  last_build_date=strftime("%a, %d %b %Y %T %Z"),
                                  generator="pypodcaster"
                                  )
def add_files(source):
    """add absolute paths to source_files"""
    if os.path.isdir(source):
        os.chdir(source)
        for file in glob.glob("*.mp3"):
            logging.debug("Appending %s/%s to source_files" % (os.getcwd(), file))
            source_files.append("%s/%s" % (os.getcwd(), file))
    else:
        logging.debug("Appending %s to source_files" % (source))
        source_files.append(source)