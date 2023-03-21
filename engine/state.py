'''
	@brief Engine module component housing all the Game State related routines
	@date Fri, 10 Feb 2023 08:49:37 +0530
'''

# standard lib imports
from abc import abstractmethod

class State:
	def __init__(self) -> None:
		self._options = None
		self._font = None
		self._font_surface = None
		self._clock = None

class GameState(State):
	def __init__(self) -> None:
		super().__init__()

	@abstractmethod
	def handle_events(self, event):
		pass

	@abstractmethod
	def update(self):
		pass

class MenuState(State):
	def __init__(self) -> None:
		super().__init__()

	@abstractmethod
	def handle_events(self, event):
		pass

	@abstractmethod
	def update(self):
		pass

