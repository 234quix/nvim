import logging
import sys

format = "%(levelname)s :: %(message)s"
logging.basicConfig(level=logging.INFO, format=format)
logger = logging.getLogger()


logger.info(f"hello")
sys.exit(1)
