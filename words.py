#!/usr/bin/env python3
"""Retrieve and print words from a URL.
Tools to read a UTF-8 text document from a URL which
will be split into its component words for printing.
Script usage:
   python3 words.py
"""



import sys
from urllib.request import Request,urlopen
from urllib.error import URLError, HTTPError

def fetch_words(url):
    """Fetch a list of words from a URL.
    Args:
        url: The URL of a UTF-8 text document.
    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf8').split()
            for word in line_words:
                story_words.append(word)
    print(locals())
    return story_words


def print_items(items):
    """Print items one per line.
    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from at a URL.
    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
  url = input('Please enter a valid URL.')

  try:
    req = Request(url)
    response = urlopen(req)
  except URLError as e:
    if hasattr(e, 'reason'):
      print ('I failed to reach a server.')
      print ('Reason: ', e.reason)
    elif hasattr(e, 'code'):
      print ('The server couldn\'t fulfill the request.')
      print ('Error code: ', e.code)
  else:
      main(req)  # The 0th arg is the module filename.