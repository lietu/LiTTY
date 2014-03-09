from colorama import init, Fore, Style
import logging


defaultLevel = logging.DEBUG


def _get_logger():
    init()

    logger = logging.getLogger('LiTTY')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('litty_debug.log')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(defaultLevel)

    fmt = "%(asctime)s [%(levelname)+20s] %(message)s"
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    colors = {
        "DEBUG": Style.BRIGHT + Fore.WHITE,
        "INFO": Style.BRIGHT + Fore.CYAN,
        "WARNING": Style.BRIGHT + Fore.YELLOW,
        "ERROR": Style.BRIGHT + Fore.RED,
    }

    for key in colors:
        level = logging.__dict__[key]
        name = str(logging.getLevelName(level))
        color = colors[key]
        logging.addLevelName(level, color + name + Style.RESET_ALL)

    return logger


log = _get_logger()
