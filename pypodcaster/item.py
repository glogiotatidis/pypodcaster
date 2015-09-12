import os, ntpath
from time import strftime, gmtime
from datetime import datetime as dt
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import validators

__author__ = 'mantlepro'

class Item:
    """Item object containing vars related to id3 tag"""
    def __init__(self, file_path, options):

        if file_path.endswith('.mp3'):
            id3 = EasyID3(file_path)
            mp3_file = MP3(file_path)
            self.title = id3['title']
            self.album = id3['album']
            self.comment = id3
            self.artist = id3['artist']
            self.subtitle = options.get("subtitle")
            self.url = "%s/%s" % (options.get("podcast_url"),ntpath.basename(file_path))
            # date should be in RFC 822 format (e.g. Sat, 07 Sep 2002 0:00:01 GMT)
            self.pub_date = dt.fromtimestamp(os.stat(file_path).st_mtime).strftime("%a, %d %b %Y %T ") + strftime('%Z')
            self.length = os.stat(file_path).st_size
            self.duration = strftime('%M:%S', gmtime(float(self.seconds)))
            self.image_url = get_image_url(file_path, options, self.title, self.album)
            self.subtitle = options.get("subtitle")
            self.url = "%s/%s" % (options.get("podcast_url"),ntpath.basename(file_path))
            # date should be in RFC 822 format (e.g. Sat, 07 Sep 2002 0:00:01 GMT)
            self.pub_date = dt.fromtimestamp(os.stat(file_path).st_mtime).strftime("%a, %d %b %Y %T ") + strftime('%Z')
            self.length = os.stat(file_path).st_size
            self.seconds = mp3_file.info.length
            self.duration = strftime('%M:%S', gmtime(float(self.seconds)))

def get_image_url(file_path, options, title, album):
    """check for episodic image with similar name or add channel default"""

    files = os.listdir(os.path.dirname(file_path))
    image_guess = os.path.splitext(os.path.basename(file_path))[0] + ".jpg"

    for file in files:
        if file.lower() == image_guess.lower():
            print "Episodic image found using filename."
            image_url = "%s/%s" % (options["podcast_url"],file)
            break
        elif os.path.isfile(title + ".jpg"):
            print "Episodic image found using title tag"
            image_url = "%s/%s" % (options["podcast_url"],title + ".jpg")
            break
        elif os.path.isfile(album + ".jpg"):
            print "Episodic image found using album tag"
            image_url = "%s/%s" % (options["podcast_url"],title + ".jpg")
            break
        else:
            print "No episodic image found. Using channel default image."
            if validators.url(options["image"]):
                image_url = options["image"]
            else:
                image_url = "%s/%s" % (options["podcast_url"],options["image"])
            break

    return image_url