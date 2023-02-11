'''
	@brief engine utility component containing the environment related details
	@date Sun, 29 Jan 2023 20:09:07 +0530
'''

# standard imports
from os import environ
from sys import exit
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# game lib import
import pygame as game_lib
from pygame.locals import QUIT
from logging import getLogger, DEBUG

from utility.log import log_setup
from utility.constants import LOGGER_INSTANCE, SwitchTo
from .state import GameState, MenuState

class Environment:
	def __init__(self, states: list, enable_debug=False) -> None:
		self.__run__ = True
		self.__surface__ = None
		self._logger = None

		if enable_debug:
			log_setup(log_level=DEBUG)
		self._logger = getLogger(LOGGER_INSTANCE)
		self._logger.info("Initializing environment")

		if states is None or len(states) < 2:
			self._logger.error("Menu and Game states are not provided, exiting run")
			exit(-1)

		self._state_stack = states if isinstance(states, list) else []
		self._state = self._state_stack.pop(0) if len(self._state_stack) > 0 else None

	# basic context handler function
	def __enter__(self):
		self._logger.info("Initializing game library modules")
		game_lib.init()
		self._logger.info("Setting the resolution")
		self.__surface__ = game_lib.display.set_mode((600, 400))
		self._logger.debug(f"Display surface resolution set to :"
					 f"{self.__surface__.get_width()}x{self.__surface__.get_height()}")
		game_lib.display.set_caption("Game Window Test")
		self._logger.debug(f"Setting window caption to : Game Window Test")

		self._logger.info("Setting the state initially to MenuState")
		self._state = MenuState()

		self._logger.debug("Returning a reference to object")
		return self

	def __exit__(self, *args, **kwargs) -> None:
		self._logger.info("Exiting the game environment")

		# fixme: Keeping these in order to remove the warnings away
		self._logger.debug(f"Non-keyword arguments : {args}")
		self._logger.debug(f"Keyword arguments : {kwargs}")

		self._logger.debug("Cleaning up")
		self.__cleanup__()

	# other hidden functions
	def __cleanup__(self) -> None:
		self._logger.info("Quitting the game lib modules and exiting")
		game_lib.quit()
		exit(0)

	# note: do not add loggers here which may result in spamming of the logging capacity
	def __update__(self):
		game_lib.display.update()

	# note: do not add loggers here which may result in spamming of the logging capacity
	def __handle_events__(self) -> None:
		for event in game_lib.event.get():
			if event.type == QUIT:
				self._logger.debug(f"Quit event received, setting run to False")
				self.__run__ = False

	# fixme: add public functions as and when required
	def listresolutions(self):
		self._logger.debug(f"Supported resolutions : ")
		for resolution in game_lib.display.list_modes():
			self._logger.debug(f"{resolution}")

	def update_cur_state(self):
		self._logger.debug(f"Current state instance of (before stack push) : {type(self._state)}")
		self._logger.debug(f"Before pushing back in stack : {self._state_stack}")
		self._state_stack.append(self._state) # push at the back
		self._logger.debug(f"After pushing back in stack : {self._state_stack}")
		self._state = self._state_stack.pop(0) # pop from the top
		self._logger.debug(f"Current state instance of (after stack pop) : {type(self._state)}")

	def mainloop(self) -> None:
		self._logger.info("Starting main loop")
		self._logger.debug(f"Current state instance : {type(self._state)}")
		# note: do not add loggers here which may result in spamming of the logging capacity
		while self.__run__:
			self.__handle_events__()
			should_switch = False # by default it should not switch
			if isinstance(self._state, MenuState):
				r = self._state.handle_events()
				if r == SwitchTo.GAME.value:
					should_switch = True
			elif isinstance(self._state, GameState):
				r = self._state.handle_events()
				if r == SwitchTo.MENU.value:
					should_switch = True

			if should_switch:
				self._logger.info("About to switch the current state")
				self.update_cur_state()
				should_switch = False
			self.__update__()
