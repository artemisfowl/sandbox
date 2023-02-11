'''
	@brief States module component containing game state related routines
	@date Sat, 11 Feb 2023 05:45:11 +0530
'''

from engine import logger, game_lib
from engine.state import GameState

class GamePlayState(GameState):
	def __init__(self) -> None:
		super().__init__()
		self._logger = logger
		self._logger.info("Enabled GamePlayState")

	# note: do not add logger lines here which will spam the logger
	# fixme: return proper int value in order to switch game state
	def handle_events(self) -> int:
		# fixme: add the game state event handling below
		for event in game_lib.event.get():
			if event.type == game_lib.K_ESCAPE:
				self._logger.debug("Received ESCAPE key event, switching to GameMenuState")
		return 0
