import logging
from logging import debug, info, warning, error

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] {%(levelname)s} %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
