#!/usr/bin/env python

# standard lib imports
from sys import path
path.append("..")

# custom lib/module imports
import engine
from states.menu import GameMenuState
from states.game import GamePlayState

def main() -> None:
	with engine.Environment(
			states=[GameMenuState(), GamePlayState()], enable_debug=engine.cli_args["debug"]) as environment:
		environment.mainloop()

if __name__ == "__main__":
	main()
