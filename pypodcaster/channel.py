import logging

from pypodcaster.item import Item

__author__ = 'mantlepro'

import os, glob, jinja2
from time import strftime

source_files = []

class Channel:
    """Podcast channel. Sources can be a string or list
    pointing to a one or more directories or mp3 files."""

    def __init__(self, sources, options):
        self.sources = sources
        self.options = options

        for source in sources:
            add_files(source)

    def items(self, options):
        """Return all items of the channel newest-to-oldest"""
        all_items = []
        for src in source_files:
            all_items.append(Item(src, options))
        logging.debug("Sorting all_items from newest-to-oldest")
        all_items = sorted(all_items, key=lambda item: item.sort_date, reverse=True)
        return all_items

    def render_xml(self):
        """render xml template with items"""
        if os.path.isfile(os.getcwd() + "/template.xml"):
            loader = jinja2.FileSystemLoader(os.getcwd())
            logging.debug("Using template from: " + os.getcwd())
        elif os.path.isfile(self.sources[0] + "/template.xml"):
            loader = jinja2.FileSystemLoader(self.sources[0])
            logging.debug("Using template from: " + self.sources[0])
        else:
            # fallback to built-in template in case no template is present
            loader = jinja2.PackageLoader("pypodcaster", 'templates')
            logging.debug("Using default template")
        env = jinja2.Environment(loader=loader)
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
        logging.debug(source + " is directory")
        os.chdir(source)
        for file in glob.glob("*.mp3"):
            source_files.append("%s/%s" % (os.getcwd(), file))
            logging.debug("Adding %s/%s to source_files" % (os.getcwd(), file))
    else:
        source_files.append(source)
        logging.debug("Adding %s to source_files" % source)
