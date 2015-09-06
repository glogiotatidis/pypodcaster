# pypodcaster

Simple Podcast Publishing

`pypodcaster` is meant to be one of the simplist podcast publishers available. It creates a standard RSS feed based on ID3 tags of media files in a given directory. Podcast media can be served from an existing web server or hosted on a public Dropbox folder.

## Install (not available yet)

    pip install pypodcaster

If you do not have `pip` installed on your system, pypodcaster can be installed using `easy_install`.

    easy_install pypodcaster
  
## Setup

Create a directory to hold your podcast media. e.g. `podcast` folder on a web server, Dropbox Public folder, (e.g. `~/Dropbox/Public`), or other public-facing html server.

    mkdir podcast

Enter channel information into `channel.yml`

```
title: 'Podcast Title'
subtitle: 'Podcast Subtitle'
url: 'http://website.com'
enclosures_url: 'https://dl.dropboxusercontent.com/u/12345678/podcast/'
language: 'en-us'
copyright: 'Copyright 2015 Podcast Creator'
author: 'Author name or Company'
description: 'A description of the podcast'
owner:
  name: 'John Doe'
  email: 'john@doe.com'
image_url: 'https://dl.dropboxusercontent.com/u/12345678/podcast/cover.jpb'
categories: ['Religion & Spirituality', 'Christianity']
explicit: No
keywords: [comma, separated, list]
```

[See iTunes podcast specs](http://www.apple.com/itunes/podcasts/specs.html)

## Usage

`cd` to directory containing podcast media and run

    pypodcaster > podcast.xml

`pypodcaster` will create `podcast.xml` with settings from `channel.yml`. Run the command every time you wish to update the podcast feed.

## Notes

Use [Feedburner](http://feedburner.com) as a middle-man to:

- Collect statistics and subscriber count
- Monitor the health of your podcast
- Analyze, optimize, and troubleshoot
- Seamlessly update your feed's location
