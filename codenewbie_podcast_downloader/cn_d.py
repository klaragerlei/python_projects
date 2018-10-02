# -*- coding: utf-8 -*-

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pickle
import sys

def dowload_podcast(url, filename):
    sys.stdout.write("Downloading " + filename)
    sys.stdout.flush()

    urlretrieve(url, filename)

def serialize_picke(dowloaded_podcasts):
    _create_pickle(dowloaded_podcasts)

def deserialize_picke():
    try:
        with open('entry.pickle', 'rb') as f:
            return pickle.load(f)
    except (OSError, IOError) as error:
        _create_pickle(None)
        return set()

def _create_pickle(data):
    with open('entry.pickle', 'wb') as f:
        pickle.dump(data, f)

def get_all_podcast(url):
    soup = BeautifulSoup(urlopen(url))
    return soup.findAll('enclosure')

"""
Simple python program to download all the podcast from codenewbie,
It uses a picke to check if a track has already been downloaded
"""
def main():
    url = 'http://feeds.codenewbie.org/cnpodcast.xml'
    podcasts = get_all_podcast(url)
    downloaded_tracks = deserialize_picke()

    for podcast in podcasts:
        podcast_url = podcast["url"]
        podcast_name = podcast_url.split("/")[::-1][0]
        if podcast_name not in downloaded_tracks:

            dowload_podcast(podcast_url, podcast_name)
            downloaded_tracks.add(podcast_name)
            serialize_picke(downloaded_tracks)
        else:
            sys.stdout.write("File  " + filename + "already downloaded")
            sys.stdout.flush()

# Run the script as "python cn_d.py"
#Note: You need to install BeautifulSoup library using pip
if __name__ == "__main__":
    main()
