import logging
from configparser import ConfigParser

logging.basicConfig(
                    # filename="logs/server.log",
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    # filename='./logs/tornado.log',
                    format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

cf = ConfigParser()
cf.read("./config.ini")