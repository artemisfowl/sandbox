#!/usr/bin/env python

# custom lib/module imports
from utility.cli import cli_util_parse_args
from engine.env import Environment

def main() -> None:
	with Environment(enable_debug=cli_util_parse_args()["debug"]) as environment:
		environment.listresolutions()
		environment.mainloop()

if __name__ == "__main__":
	main()
