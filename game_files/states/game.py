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

		self._clock = None

	def set_surface(self, surface):
		if surface is not None:
			self._surface = surface
			self._surface.fill(game_lib.Color(0, 0, 255))

	def set_clock(self, clock):
		if clock is not None:
			self._clock = clock

	# note: do not add logger lines here which will spam the logger
	# fixme: return proper int value in order to switch game state
	def handle_events(self, event) -> int:
		# fixme: add the game state event handling below
		if event.key == game_lib.K_ESCAPE:
			self._logger.info("Escape key pressed, moving to menu state")
			return SwitchTo.MENU.value
		elif event.key == game_lib.K_UP:
			self._logger.info("Up Arrow has been pressed")
			if self._surface:
				self._surface.fill(game_lib.Color(0, 128, 255))
		elif event.key == game_lib.K_DOWN:
			self._logger.info("Down arrow was pressed")
			if self._surface:
				self._surface.fill(game_lib.Color(127, 127, 0))
		return 0

	def update(self):
		# fixme: add necessary code in this function
		if self._surface is None:
			return

		self._logger.info("Inside the GamePlayState update function")
		game_lib.display.update()
