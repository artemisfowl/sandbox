'''
	@brief States module component containing game state related routines
	@date Sat, 11 Feb 2023 05:45:11 +0530
'''

from engine import logger, game_lib
from engine.state import GameState
from utility.constants import DEBUG_TEXT_SIZE, SwitchTo

class GamePlayState(GameState):
	def __init__(self) -> None:
		super().__init__()
		self._logger = logger
		self._surface = None
		self._logger.info("Enabled GamePlayState")
		self._screen_color = game_lib.Color(0, 0, 255)

		# clock used for the fps
		self._clock = None
		self._show_fps = False

		# font for debugging certain issues
		game_lib.font.init()
		self._font = game_lib.font.Font(game_lib.font.get_default_font(), DEBUG_TEXT_SIZE)

	def set_surface(self, surface):
		if surface is not None:
			self._surface = surface
			self._surface.fill(self._screen_color)

	def set_clock(self, clock):
		if clock is not None:
			self._clock = clock

	def show_fps(self):
		if not self._clock:
			self._logger.warning("Clock not set")
			return
		# fixme: Create the font for the GamePlayState
		self._font_surface = self._font.render(f"FPS : {int(self._clock.get_fps())}", True, game_lib.Color(0, 0, 0))
		if self._surface:
			self._surface.blit(self._font_surface, (10, 10))

	# note: do not add logger lines here which will spam the logger
	# fixme: return proper int value in order to switch game state
	def handle_events(self, event) -> int:
		# fixme: add the game state event handling below
		if event.key == game_lib.K_ESCAPE:
			self._logger.info("Escape key pressed, moving to menu state")
			return SwitchTo.MENU.value
		elif event.key == game_lib.K_UP:
			self._logger.info("Up Arrow has been pressed")
			self._screen_color = game_lib.Color(0, 128, 255)
		elif event.key == game_lib.K_DOWN:
			self._logger.info("Down arrow was pressed")
			self._screen_color = game_lib.Color(127, 127, 0)
		elif event.key == game_lib.K_F10:
			self._logger.info("F10 key pressed, showing fps")
			self._logger.debug(f"Show FPS flag : {self._show_fps}")
			self._show_fps = not self._show_fps
		return 0

	def update(self):
		# fixme: add necessary code in this function
		if self._surface is None:
			return

		self._surface.fill(self._screen_color)
		if self._show_fps:
			self.show_fps()
		game_lib.display.update()
