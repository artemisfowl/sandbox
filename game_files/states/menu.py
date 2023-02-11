'''
	@brief States module component containing game state related routines
	@date Sat, 11 Feb 2023 04:52:36 +0530
'''

# custom lib imports
from engine import logger, game_lib, SwitchTo
from engine.state import MenuState

class GameMenuState(MenuState):
	def __init__(self) -> None:
		super().__init__()
		self._logger = logger
		self._logger.info("Initialised GameMenuState")

	# note: do not add logger lines here which will spam the logger
	# fixme: return proper int value in order to switch states
	def handle_events(self, event) -> int:
		if event.key == game_lib.K_RETURN:
			self._logger.info("Enter/return key pressed, moving to game play state")
			return SwitchTo.GAME.value
		return 0
