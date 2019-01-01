import logging
from configparser import ConfigParser

logging.basicConfig(
                    # filename="/var/log/blogback/tornado.log",
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

cf = ConfigParser()
cf.read("./config.ini")