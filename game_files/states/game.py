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
		self._logger.info("Enabled GamePlayState")

	# note: do not add logger lines here which will spam the logger
	# fixme: return proper int value in order to switch game state
	def handle_events(self, event) -> int:
		# fixme: add the game state event handling below
		if event.code == game_lib.K_ESCAPE:
			self._logger.info("Escape key pressed, moving to menu state")
			return SwitchTo.MENU.value
		return 0
