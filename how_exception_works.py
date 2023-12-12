import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

def errorable_task():
    try:
        1 / 0
    except Exception as e:
        logger.exception("errorable_taskが原因不明で復旧不能なエラーをだしました", stack_info=True)

def tasks():
    try:
        errorable_task()
    except Exception as e:
        logger.exception("tasksが原因不明で復旧不能なエラーをだしました", stack_info=True)

def main():
    try:
        tasks()
    except Exception as e:
        logger.exception("mainが原因不明で復旧不能なエラーをだしました", stack_info=True)

main()
