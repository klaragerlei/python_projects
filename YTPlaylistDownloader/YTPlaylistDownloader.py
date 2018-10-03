#!/usr/bin/env python

# To use this code, you have to execute it from a bash environment and have an up-to-date youtube-dl installation. 

from threading import Thread
import subprocess
from copy import copy
from logging import Formatter

COLORS = { # This is used for Terminal Colors.
	'RESET'	: "\033[1;m",
    'BLUE'   : "\033[1;34m",
    'SUCCESS'    : "\033[1;32m", 
    'WARNING' : "'\033[1;33m", 
    'ERROR'   : "\033[1;41m", 
    'CRITICAL': "\033[1;41m"
}


playlistlinks = ["https://www.youtube.com/playlist?list=PLfRDnxXohb4lWnpsT5hHXi4ZSARKKhXSg", "https://www.youtube.com/playlist?list=PLfRDnxXohb4l9_45PNrf9RX41I6ZEyj12"] # Al target YouTube playlist links are added here.

def downloadPlaylist(url): # This is a function intended to be used as a thread.
	try: 
		print(COLORS["SUCCESS"] + "[OK]" + COLORS["RESET"] + " Started downloading " + url) # The output is constructed of the colors defined earlier.
		subprocess.check_call("youtube-dl -i --extract-audio --audio-format m4a --embed-thumbnail --add-metadata --audio-quality 0 --prefer-ffmpeg -o '%(title)s.%(ext)s' --postprocessor-args '-strict -2' " + url + " > /dev/null 2>&1", shell=True) # This starts the youtube-dl package, an utility for downloading YouTube Videos. It has to be installed, but the script will configure it on it's own.
		print(COLORS["SUCCESS"] + "[SUCCESS]" + COLORS["RESET"] + " Downloaded " + url + " sucessfully!")
	except: 
		print(COLORS["ERROR"] + "[FAIL]" + COLORS["RESET"] + " Couldn't download " + url + ".") # When any exception occurs, it is catched here and the playlist is skipped.


""" # Some more colors that I didn't end up using.
print '\033[1;30mGray like Ghost\033[1;m'
print '\033[1;31mRed like Radish\033[1;m'
print '\033[1;32mGreen like Grass\033[1;m'
print '\033[1;33mYellow like Yolk\033[1;m'
print '\033[1;34mBlue like Blood\033[1;m'
print '\033[1;35mMagenta like Mimosa\033[1;m'
print '\033[1;36mCyan like Caribbean\033[1;m'
print '\033[1;37mWhite like Whipped Cream\033[1;m'
print '\033[1;38mCrimson like Chianti\033[1;m'
print '\033[1;41mHighlighted Red like Radish\033[1;m'
print '\033[1;42mHighlighted Green like Grass\033[1;m'
print '\033[1;43mHighlighted Brown like Bear\033[1;m'
print '\033[1;44mHighlighted Blue like Blood\033[1;m'
print '\033[1;45mHighlighted Magenta like Mimosa\033[1;m'
print '\033[1;46mHighlighted Cyan like Caribbean\033[1;m'
print '\033[1;47mHighlighted Gray like Ghost\033[1;m'
print '\033[1;48mHighlighted Crimson like Chianti\033[1;m'
"""

print(COLORS["SUCCESS"] + "[OK]" + COLORS["RESET"] + " " + str(len(playlistlinks)) + " playlists staged for download.") # This simply shows the count of playlists in the array.

for url in playlistlinks: # This loops over the playlist array.
	thr = Thread(target=downloadPlaylist, args=[url]) # Using the Thread() function we start a new thread for each download.
	thr.start()
