'''
	@brief States module component containing game state related routines
	@date Sat, 11 Feb 2023 05:45:11 +0530
'''

from engine import logger, game_lib
from engine.state import GameState
from utility.constants import SwitchTo

class GamePlayState(GameState):
	def __init__(self) -> None:
		super().__init__()
		self._logger = logger
		self._surface = None
		self._logger.info("Enabled GamePlayState")

	def set_surface(self, surface):
		if surface is not None:
			self._surface = surface

	# note: do not add logger lines here which will spam the logger
	# fixme: return proper int value in order to switch game state
	def handle_events(self, event) -> int:
		# fixme: add the game state event handling below
		if event.key == game_lib.K_ESCAPE:
			self._logger.info("Escape key pressed, moving to menu state")
			return SwitchTo.MENU.value
		return 0

	def update(self):
		# fixme: add necessary code in this function
		if self._surface is None:
			return

		self._logger.info("Inside the GamePlayState update function")
