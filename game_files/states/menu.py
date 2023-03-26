'''
	@brief States module component containing game state related routines
	@date Sat, 11 Feb 2023 04:52:36 +0530
'''

# standard lib imports
from enum import Enum

# custom lib imports
from engine import logger, game_lib, SwitchTo
from engine.state import MenuState
from utility.constants import DEBUG_TEXT_SIZE

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

		game_lib.font.init()
		self._font = game_lib.font.Font(game_lib.font.get_default_font(), DEBUG_TEXT_SIZE)
		self._show_fps = False

		self._logger.info("Initialised GameMenuState")

	def set_surface(self, surface):
		if surface is not None:
			self._surface = surface

	def set_clock(self, clock):
		if clock is not None:
			self._clock = clock

	def show_options(self):
		if self._surface is None:
			return

	def get_menu_options(self):
		# fixme: add code for getting the list of options to be shown in the menu screen
		self._logger.debug(f"Populated options : {self._options}")

	def show_debug(self, message: str):
		# fixme: Add the code for showing debug related information in the screen itself
		self._logger.debug(f"Message to be printed : {message}")

	def show_fps(self):
		# fixme: Add the code for creating the surface and the rendering
		if not self._clock:
			self._logger.warning("Clock not set")
			return
		self._font_surface = self._font.render(f"FPS : {int(self._clock.get_fps())}", True, game_lib.Color(0, 0, 0))
		if self._surface:
			self._surface.blit(self._font_surface, (10, 10))

	def update(self):
		if self._surface is None:
			self._logger.warning("Surface not set")
			return

		self._surface.fill(game_lib.Color(255, 255, 255))
		if self._show_fps:
			self.show_fps()
		game_lib.display.update()
		#self.get_menu_options() # fixme: this is spamming a lot of log lines, need to remove that

	# note: do not add logger lines here which will spam the logger
	def handle_events(self, event) -> int:
		if event.key == game_lib.K_RETURN:
			self._logger.info("Enter/return key pressed, moving to game play state")
			return SwitchTo.GAME.value
		elif event.key == game_lib.K_F10:
			self._logger.info("F10 key pressed, showing the fps")
			self._logger.debug(f"Show FPS : {self._show_fps}")
			self._show_fps = not self._show_fps
		elif event.key == game_lib.K_ESCAPE:
			return 1005
		return 0
