# pypodcaster

Simple Podcast Publishing

pypodcaster generates a standard iTunes-compatible podcast feed from media files in a directory. Use a Dropbox Public folder or any other public-facing html server to host your podcast.

## Install

If you have `git` installed

    git clone https://github.com/mantlepro/pypodcaster.git
    cd pypodcaster
    sudo python setup.py install

If you do not have `git` installed

Download the zip: https://github.com/mantlepro/pypodcaster/archive/master.zip

    unzip pypodcaster-master.zip
    cd pypodcaster-master
    sudo python setup.py install

## Setup

Create a directory to hold your podcast media (e.g. `~/Dropbox/Public`).

    mkdir podcast

Enter channel information into `channel.yml`

Note: `title`, `link`, `description`, and `podcast_url` are required fields. The rest are optional but recommended.

```
title: 'Podcast Title'
link: 'http://link-to-website-corresponding-to-the-channel.com'
description: 'Phrase or sentence describing the channel.'
language: 'en-us'
copyright: 'Copyright notice for channel content.'
subtitle: 'Podcast Subtitle'
podcast_url: 'https://dl.dropboxusercontent.com/u/12345678/podcast/'
image: 'cover.jpg' # full url or image under podcast_url
author: 'Author name or Company'
owner:
  name: 'John Doe'
  email: 'john@doe.com'
categories: ['Religion & Spirituality', 'Christianity']
explicit: No
keywords: [comma, separated, list]
```

#### Dropbox URL

To find your Dropbox url, right-click any file inside your Dropbox/Public/podcast directory and select Dropbox > Copy Public Link. `Replace 12345678` in the example above with your actual Dropbox id.

## Usage

`cd` to directory containing podcast media and run

    pypodcaster > podcast.xml

pypodcaster will create `podcast.xml` with settings from `channel.yml`. Run the command every time you wish to update the podcast feed.

To see everything pypodcaster is capable of, run `pypodcaster --help`

```
$ pypodcaster --help
usage: pypodcaster [-h] [-c /path/to/channel.yml] [-o OUTPUT] [-V]
                   [sources [sources ...]]

pypodcaster - free, open source podcast rss generator by Josh Wheeler
<mantlepro@gmail.com>

positional arguments:
  sources               Specify source files or directories

optional arguments:
  -h, --help            show this help message and exit
  -c /path/to/channel.yml, --channel /path/to/channel.yml
                        Specify channel definition instead of current
                        directory's channel.yml
  -o OUTPUT, --output OUTPUT
                        Direct output to FILE instead of stdout
  -V, --version         show program's version number and exit

example: pypodcaster > index.rss
```

## Advanced

### Sorting by Date

By default, the podcast feed is sorted by file modification time. If you wish to modify the date of a podcast episode, prepend the date to the episode's filename in the following format: `YYYY-MM-DD` or `YYYYMMDD`.

#### Example

    2016-03-17 Episode Title.mp3
    20160317 Episode Title.mp3

### Episodic Images

To add an image to the episode or series, add a jpg with the same filename, title or album tag alongside the mp3 file.

If album name is used, the image will carry across an entire series. If no jpg is provided, the cover image will default to the channel's cover image set in `channel.yml`.

#### Example

```
Contents of Dropbox/Public/podcast:
  First Podcast.mp3
  First Podcast.jpg # lower case "first podcast.jpg" would also work
  series01.mp3
  series02.mp3
  series03.mp3
  Series Name.jpg # from id3's album tag. 
```

### Customize XML Template

pypodcaster uses [Jinja2](http://jinja.pocoo.org/) for beautiful xml templating. If you wish to edit the feed's format beyond pypodcaster's basic template, add `template.xml` to your podcast directory with contents based on [template.xml](https://github.com/mantlepro/pypodcaster/blob/master/pypodcaster/templates/template.xml) 

## Notes

Use [Feedburner](http://feedburner.com) as a middle-man to:

- Collect statistics and subscriber count
- Monitor the health of your podcast
- Analyze, optimize, and troubleshoot
- Seamlessly update your feed's location

## Podcast Specifications

- [iTunes Podcast Specs](http://www.apple.com/itunes/podcasts/specs.html)
- [RSS 2.0 Specifications](https://validator.w3.org/feed/docs/rss2.html)
