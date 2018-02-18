from core import handle
from core import const
from core import internals
from core import gaana_tools

import sys
import platform
import pprint

def download_single(raw_song, number=None):
    """ logic behind downloading single song"""
    if internals.is_youtube(raw_song):
        log.debug('Input song is a YouTube URL')
    else:
        meta_tags = gaana_tools.generate_metadata(raw_song)    
    pass


def main():
    const.args = handle.get_arguments()

    const.log = const.logzero.setup_logger(
        formatter=const.formatter,
        level=const.args.log_level
    )

    log = const.log
    log.debug('Python version: {}'.format(sys.version))
    log.debug('Platform: {}'.format(platform.platform()))
    log.debug(pprint.pformat(const.args.__dict__))

    try:
        if const.args.song:
            download_single(raw_song=const.args.song)
    except KeyboardInterrupt as e:
        log.exception(e)
        sys.exit(3)
    pass


if __name__ == '__main__':
    main()
