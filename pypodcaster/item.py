import os, ntpath, logging, validators, re, time
from datetime import datetime
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

__author__ = 'mantlepro'

class Item:
    """Item object containing vars related to id3 tag"""
    def __init__(self, file_path, options):

        if file_path.endswith('.mp3'):
            id3 = EasyID3(file_path)
            audio = MP3(file_path)
            self.title = ''.join(id3['title'])
            self.album= ''.join(id3['album'])
            # TODO: add ability for user to add description through id3 tag or otherwise
            self.comment = ""
            self.artist = ''.join(id3['artist'])
            self.subtitle = options.get("subtitle")
            self.url = "%s/%s" % (options.get("podcast_url"),ntpath.basename(file_path))
            self.pub_date = get_pub_date(file_path)
            self.length = os.stat(file_path).st_size
            self.seconds = audio.info.length
            self.duration = time.strftime('%M:%S', time.gmtime(float(self.seconds)))
            self.image_url = get_image_url(file_path, options, self.title, self.album)

def get_image_url(file_path, options, title, album):
    """check for episodic image with similar name or add channel default"""

    files = os.listdir(os.path.dirname(file_path))
    mp3file = os.path.basename(file_path)
    image_guess = os.path.splitext(mp3file)[0] + ".jpg"
    found = False

    for file in files:
        if file.lower() == image_guess.lower():
            logging.info("Episodic image found for %s using filename." % mp3file)
            image_url = "%s/%s" % (options["podcast_url"],file)
            found=True
            break
        elif os.path.isfile(title + ".jpg"):
            logging.info("Episodic image found for %s using title tag" % mp3file)
            image_url = "%s/%s" % (options["podcast_url"],title + ".jpg")
            found=True
            break
        elif os.path.isfile(title.lower() + ".jpg"):
            logging.info("Episodic image found for %s using lowercase title tag" % mp3file)
            image_url = "%s/%s" % (options["podcast_url"],title.lower() + ".jpg")
            found=True
            break
        elif os.path.isfile(album + ".jpg"):
            logging.info("Episodic image found for %s using album tag" % mp3file)
            image_url = "%s/%s" % (options["podcast_url"],album + ".jpg")
            found=True
            break
        elif os.path.isfile(album.lower() + ".jpg"):
            logging.info("Episodic image found for %s using album lowercase tag" % mp3file)
            image_url = "%s/%s" % (options["podcast_url"],album.lower() + ".jpg")
            found=True
            break

    if not found:
        logging.debug("No episodic image found for %s. Using channel default image." % mp3file)
        if validators.url(options["image"]):
            image_url = options["image"]
        else:
            image_url = "%s/%s" % (options["podcast_url"],options["image"])

    return image_url

def get_pub_date(filename):
    """Extract pub_date from filename containing YYYY-MM-DD
    or else use file's modified time as a fallback."""

    date = datetime.fromtimestamp(os.stat(filename).st_mtime)

    dashless_date = re.search(r'(\d{4}\d{2}\d{2})', filename)
    dashed_date = re.search(r'(\d{4}\-\d{2}\-\d{2})', filename)

    try:
        if dashless_date:
            date = datetime.strptime(dashless_date.group(0), "%Y%m%d")
        elif dashed_date:
            date = datetime.strptime(dashed_date.group(0), "%Y-%m-%d")

    except ValueError as err:
        logging.error("Filename contains incorrect date: " + filename + " " + str(err))
        logging.info("Using file's mtime for " + filename)

    # date must be in RFC 822 format (e.g. Sat, 07 Sep 2002 0:00:01 GMT)
    date = date.strftime("%a, %d %b %Y %T ") + time.strftime('%Z')

    return date

# TODO: Find cover image in id3 tag or add it if missing
# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3, APIC, error
#
# audio = MP3('example.mp3', ID3=ID3)
#
# # add ID3 tag if it doesn't exist
# try:
#     audio.add_tags()
# except error:
#     pass
#
# audio.tags.add(
#     APIC(
#         encoding=3, # 3 is for utf-8
#         mime='image/png', # image/jpeg or image/png
#         type=3, # 3 is for the cover image
#         desc=u'Cover',
#         data=open('example.png').read()
#     )
# )
# audio.save()

# TODO: Detect existing picture
# def pict_test(audio):
#     try:
#         x = audio.pictures
#         if x:
#             return True
#     except Exception:
#         pass
#     if 'covr' in audio or 'APIC:' in audio:
#         return True
#     return False