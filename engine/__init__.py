'''
	@brief Engine component init containing required imports
	@date Sat, 11 Feb 2023 05:35:01 +0530
'''

# parse the cli arguments and prepare the directory
from utility.cli import cli_util_parse_args
cli_args = cli_util_parse_args()

# import logging related routines and modules as well
from utility.constants import LOGGER_INSTANCE
from logging import getLogger
logger = getLogger(LOGGER_INSTANCE)

# provide the project with the environment
from engine.env import Environment

# game library related imports
import pygame as game_lib
from pygame.locals import * # fixme: write the names of the specific imports here

# constants and enums
from utility.constants import SwitchTo, LoggingOptions

