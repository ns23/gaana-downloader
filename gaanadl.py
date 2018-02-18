from core import handle
from core import const

import sys
import platform
import pprint

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

    pass

if __name__ == '__main__':
    main()
