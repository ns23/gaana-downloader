import os
import sys

from core import const

log = const.log


def is_youtube(raw_song):
    """ Check if the input song is a YouTube link. """
    status = len(raw_song) == 11 and raw_song.replace(" ", "%20") == raw_song
    status = status and not raw_song.lower() == raw_song
    status = status or 'youtube.com/watch?v=' in raw_song
    return status
