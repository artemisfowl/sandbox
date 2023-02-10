'''
	@brief States module component containing game state related routines
	@date Sat, 11 Feb 2023 04:52:36 +0530
'''

import pygame as game_lib
from pygame.locals import * # fixme: add the specific imports here

from engine.state import MenuState

class GameMenuState(MenuState):
	def __init__(self) -> None:
		super().__init__()

	def handle_events(self) -> None:
		pass
