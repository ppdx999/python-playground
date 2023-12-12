import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def stdout_by_print():
    print("stdout_by_print start")

    try:
        1 / 0
    except ZeroDivisionError:
        print("stdout_by_print error")

    print("stdout_by_print end")

def stdout_by_logger():
    logger.info("stdout_by_logger start")

    try:
        1 / 0
    except ZeroDivisionError:
        logger.error("stdout_by_logger error")

    logger.info("stdout_by_logger end")


if __name__ == "__main__":
    stdout_by_print()
    stdout_by_logger()
