'''
	@brief States module component containing game state related routines
	@date Sat, 11 Feb 2023 04:52:36 +0530
'''

# standard lib imports
from enum import Enum

# custom lib imports
from engine import logger, game_lib, SwitchTo
from engine.state import MenuState

class GameMenuOptions(Enum):
	_continue = 1
	_new_game = 2
	_options = 3
	_quit_game = 4

class GameMenuState(MenuState):
	def __init__(self) -> None:
		super().__init__()
		self._logger = logger
		self._options = {option.name: option.value for option in GameMenuOptions}
		self._surface = None # this is the display surface which will be updated

		self._logger.info("Initialised GameMenuState")

	def set_surface(self, surface):
		if surface is not None:
			self._surface = surface

	def show_options(self):
		if self._surface is None:
			return

	def get_menu_options(self):
		# fixme: add code for getting the list of options to be shown in the menu screen
		self._logger.debug(f"Populated options : {self._options}")

	def update(self):
		if self._surface is None:
			self._logger.warning("Surface not set")
			return

		self._surface.fill(game_lib.Color(0, 0, 0))
		game_lib.display.update()
		self.get_menu_options()

	# note: do not add logger lines here which will spam the logger
	def handle_events(self, event) -> int:
		if event.key == game_lib.K_RETURN:
			self._logger.info("Enter/return key pressed, moving to game play state")
			return SwitchTo.GAME.value
		return 0
