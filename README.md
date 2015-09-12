# pypodcaster

Simple Podcast Publishing

`pypodcaster` is meant to be one of the simplist podcast publishers available. It generates a standard RSS feed based on the ID3 tags of media files in a given directory. Podcast media can be served from a public-facing HTML server or hosted from the Public folder in Dropbox.
  
## Setup

Create a directory to hold your podcast media on a public-facing html server or Dropbox Public folder (e.g. `~/Dropbox/Public`).

    mkdir podcast

Enter channel information into `channel.yml`

Note: `title`, `link`, and `description` are required fields. The rest are optional.

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

## Podcast Specifications

- [iTunes Podcast Specs](http://www.apple.com/itunes/podcasts/specs.html)
- [RSS 2.0 Specifications](https://validator.w3.org/feed/docs/rss2.html)
