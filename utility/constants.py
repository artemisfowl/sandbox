'''
	@brief Utility module component containing all the constants
	@date Fri, 10 Feb 2023 00:34:30 +0530
'''

from os import sep

LOGGER_INSTANCE = "albatross"
LOGGER_DIR = f".{sep}logs{sep}"
LOGGER_FILE = f".{sep}exec.log"
LOGGER_FORMAT = '[%(levelname)-7s] - %(asctime)s - %(name)s {%(filename)s:%(funcName)s:%(lineno)d} - %(message)s'
