import os, ntpath, eyeD3
from time import strftime, gmtime
from datetime import datetime as dt

__author__ = 'mantlepro'

class Item:
    """Item object containing vars related to id3 tag"""
    def __init__(self, file_path, options):
        self.options = options
        if eyeD3.isMp3File(file_path):
            mp3_file = eyeD3.Mp3AudioFile(file_path)
            id3 = mp3_file.getTag()
            id3.link(file_path)
            # TODO: check for episodic images and add default if none provided
            self.image_url = "%s/%s" % (options.get("podcast_url"),options.get("image"))
            self.title = id3.getTitle()
            self.album = id3.getAlbum()
            self.comment = id3.getComment()
            self.artist = id3.getArtist()
            self.subtitle = options.get("subtitle")
            self.url = "%s/%s" % (options.get("podcast_url"),ntpath.basename(file_path))
            # date should be in RFC 822 format (e.g. Sat, 07 Sep 2002 0:00:01 GMT)
            self.pub_date = dt.fromtimestamp(os.stat(file_path).st_mtime).strftime("%a, %d %b %Y %T ") + strftime('%Z')
            self.length = os.stat(file_path).st_size
            self.seconds = mp3_file.getPlayTime()
            self.duration = strftime('%M:%S', gmtime(float(self.seconds)))