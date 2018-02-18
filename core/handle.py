import logging
import argparse

import os
import sys

_LOG_LEVEL_STR = ['INFO','ERROR','WARNING','DEBUG']

def log_leveller(log_level_str):
    loggin_levels = [logging.INFO,logging.ERROR,logging.WARNING,logging.DEBUG]
    logging_level_str_index = _LOG_LEVEL_STR.index(log_level_str)
    loggin_level = loggin_levels[logging_level_str_index]
    return loggin_level

def get_arguments(raw_args=None,to_group=True,to_merge=True):
    parser =  argparse.ArgumentParser(
        description='Download and convert songs from spotify',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    if to_group:
        
        group =  parser.add_mutually_exclusive_group(required=True)

        group.add_argument(
            '-s','--song',help='Download song by gaana link'
        )
        group.add_argument(
            '-p','--playlist',help='Download song by playlist link'
        )
        group.add_argument(
            '-a','--album',help='Download song by album link or name'
        )
    
    parser.add_argument(
        '-m','--manual',default=False,
        help='choose the song to download manually',action='store_true'
    )
    parser.add_argument(
        '-d', '--dry-run', default=False,
        help='Show only track title and YouTube URL',
        action='store_true')

    parser.add_argument(
        '-ns', '--no-spaces', default=False,
        help='Replace spaces with underscores in file names',
        action='store_true')
    
    parser.add_argument(
        '-ll', '--log-level', default='INFO',
        choices=_LOG_LEVEL_STR,
        type=str.upper,
        help='set log verbosity')

    parsed = parser.parse_args(raw_args)
    parsed.log_level = log_leveller(parsed.log_level)

    return parsed
