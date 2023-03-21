'''
	@brief Utility module component containing all the constants
	@date Fri, 10 Feb 2023 00:34:30 +0530
'''

from os import sep
from enum import Enum

LOGGER_INSTANCE = "albatross"
LOGGER_DIR = f".{sep}logs{sep}"
LOGGER_FILE = f".{sep}exec.log"
LOGGER_FORMAT = '[%(levelname)-7s] - %(asctime)s - %(name)s {%(filename)s:%(funcName)s:%(lineno)d} - %(message)s'

GAME_FPS = 60
FPS_TEXT_COLOR_PRIMARY = (255, 255, 255) # this will be for light background colors
FPS_TEXT_COLOR_ALTERNA = (0, 0, 0) # this will be for the dark background colors

DEBUG_TEXT_SIZE = 12

class LoggingOptions(Enum):
	debug_with_console_io = 10 # enable logging in only console stream handler, default this one should be used
	debug_with_file_io = 20	   # enable logging in only file stream handler, no console output of the logging lines
	debug_with_all_io = 30	   # enable logging in both console as well as file stream handler

class SwitchTo(Enum):
	MENU=1
	GAME=2

class StateName:
	game_play_state = "GAME"
	game_menu_state = "MENU"
