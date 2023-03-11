#!/usr/bin/env python

# standard lib imports
from sys import path

path.append("..")

# custom lib/module imports
import engine
from states.menu import GameMenuState
from states.game import GamePlayState

def main() -> None:
	mode = None
	if engine.cli_args["debug_with_console"]:
		mode = engine.LoggingOptions.debug_with_console_io
	elif engine.cli_args["debug_with_file"]:
		mode = engine.LoggingOptions.debug_with_file_io
	elif engine.cli_args["debug_with_all"]:
		mode = engine.LoggingOptions.debug_with_all_io

	# now create the environment with the right mode
	with engine.Environment(
			states=[GameMenuState(), GamePlayState()], debugging_mode=mode) as environment:
		environment.mainloop()

if __name__ == "__main__":
	main()
