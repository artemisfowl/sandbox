#!/usr/bin/env python

# custom lib/module imports
from utility.cli import cli_util_parse_args
from engine.env import Environment

def main() -> None:
	cli_args = cli_util_parse_args()
	with Environment(enable_debug=cli_args["debug"]) as environment:
		environment.listresolutions()
		environment.mainloop()

if __name__ == "__main__":
	main()
