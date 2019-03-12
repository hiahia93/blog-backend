import logging
from configparser import ConfigParser

cf = ConfigParser()
cf.read("./script/config.ini")

logging.basicConfig(
                    # filename=cf.get('server', 'log_file_path'),
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
