'''
	@brief engine utility component containing the environment related details
	@date Sun, 29 Jan 2023 20:09:07 +0530
'''

# standard imports
from os import environ
from sys import exit

from engine.state import GameState, MenuState
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# game lib import
import pygame as game_lib
from pygame.locals import QUIT
from logging import getLogger, DEBUG

from utility.log import log_setup
from utility.constants import LOGGER_INSTANCE, SwitchTo, LoggingOptions

class Environment:
	def __init__(self, states: list, debugging_mode=None) -> None:
		self.__run__ = True
		self.__surface__ = None

		# fixme: test the debugging_mode code from the execute file
		if debugging_mode == LoggingOptions.debug_with_console_io:
			log_setup(log_level=DEBUG)
		elif debugging_mode == LoggingOptions.debug_with_file_io:
			log_setup(log_level=DEBUG, log_to_file=True, log_to_stdout=False)
		elif debugging_mode == LoggingOptions.debug_with_all_io:
			log_setup(log_level=DEBUG, log_to_file=True)
		elif debugging_mode is None:
			pass # ignore and move on

		self._logger = getLogger(LOGGER_INSTANCE)
		self._logger.info("Initializing environment")

		if states is None or len(states) < 2:
			self._logger.error("Menu and Game states are not provided, exiting run")
			exit(-1)

		self._state_stack = states if isinstance(states, list) else []
		self._state = self.__select_state__(state_type=MenuState)

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

		self._logger.info("Setting the state initially to MenuState instance")

		self._logger.debug("Returning a reference to object")
		return self

	def __exit__(self, *args, **kwargs) -> None:
		self._logger.info("Exiting the game environment")

		# fixme: Keeping these in order to remove the warnings away
		self._logger.debug(f"Non-keyword arguments : {args}")
		self._logger.debug(f"Keyword arguments : {kwargs}")

		# fixme: provide the information in the logs about the error that occurred
		#self._logger.error(msg="Error occurred", *args)

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

	def __select_state__(self, state_type, store_state=None):
		self._logger.info("About to search for state of the desired type")
		self._logger.debug(f"Desired state type : {state_type.__class__.__name__}")
		# note: may return None if not found
		for index, state in enumerate(self._state_stack):
			if isinstance(state, state_type):
				self._logger.debug(f"Found desired state : {state.__class__.__name__}")
				if store_state is not None:
					self._state_stack.append(store_state)
				return self._state_stack.pop(index)

	# note: do not add loggers here which may result in spamming of the logging capacity
	def __handle_events__(self) -> None:
		for event in game_lib.event.get():
			if event.type == QUIT:
				self._logger.debug(f"Quit event received, setting run to False")
				self.__run__ = False
			# for some reason the code is not going inside this at all
			elif event.type == game_lib.KEYDOWN:
				self._logger.debug(f"Keydown event details : {event}")
				self._logger.debug(f"Current state : {type(self._state)}")

				r = self._state.handle_events(event=event) # type: ignore
				if r == SwitchTo.GAME.value:
					self._logger.info("Switching to GameState instance")
					self.update_cur_state(state_type=GameState)
				elif r == SwitchTo.MENU.value:
					self._logger.info("Switching to MenuState instance")
					self.update_cur_state(state_type=MenuState)

	# fixme: add public functions as and when required
	def listresolutions(self):
		self._logger.debug(f"Supported resolutions : ")
		for resolution in game_lib.display.list_modes():
			self._logger.debug(f"{resolution}")

	def update_cur_state(self, state_type):
		self._logger.debug(f"Current state instance of (before stack push) : {type(self._state)}")
		self._logger.debug(f"Before pushing back in stack : {self._state_stack}")
		self._state = self.__select_state__(state_type=state_type, store_state=self._state)
		#self._state_stack.append(self._state) # push at the back
		self._logger.debug(f"After pushing back in stack : {self._state_stack}")
		self._logger.debug(f"Current state instance of (after stack pop) : {type(self._state)}")

	def mainloop(self) -> None:
		self._logger.info("Starting main loop")
		self._logger.debug(f"Current state instance : {type(self._state)}")
		# note: do not add loggers here which may result in spamming of the logging capacity
		while self.__run__:
			self.__handle_events__()
			self.__update__()
