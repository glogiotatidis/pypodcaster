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

        self.options['image_url'] = "%s/%s" % (options.get("podcast_url"),options.get("image"))

        # if list
        if isinstance(sources, list):
            for s in sources:
                add_files(s)
        else:
            # single file or dir
            add_files(sources)

    def items(self, options):
        """Return all items of the channel newest-to-oldest"""
        all_items = []
        for src in source_files:
            all_items.append(Item(src, options))
            sorted(all_items, key=lambda item: item.options.get("pub_date"))
        return all_items

    def xml(self):
        env = Environment(loader=PackageLoader("pypodcaster", 'templates'))
        template_xml = env.get_template('template.xml')
        # set up template variables
        return template_xml.render(channel=self.options,
                                  items=self.items(self.options),
                                  last_build_date=strftime("%a, %d %b %Y %T %Z"),
                                  generator="pypodcaster"
                                  )
def add_files(src):
    """add absolute paths to source_files"""
    if os.path.isdir(src):
        os.chdir(src)
        for file in glob.glob("*.mp3"):
            source_files.append(file)
    else:
        source_files.append(src)