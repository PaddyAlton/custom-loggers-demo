# custom_loggers/workhorse.py
# does all the hard work round here

import logging

logger = logging.getLogger(__name__)


def do_something():
    logger.info("I'm working hard, honest")
    logger.warning("Working hard, or hardly working??")
    logger.info("That's it, I quit!")
    logger.error("uh-oh!")
