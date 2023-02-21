'''
	@brief Utility module component containing all CLI related routines
	@date Sun, 29 Jan 2023 16:55:09 +0530
'''

from argparse import ArgumentParser

def cli_util_parse_args() -> dict:
	'''
		@brief function to parse the cli arguments
		@return returns a dictionary containing the arguments
	'''
	parser = ArgumentParser()

	# add required arguments here

	# optional arguments
	parser.add_argument("--debug-with-console", "-dwc",
					 help="Enable debug mode in console only", action="store_true", required=False)
	parser.add_argument("--debug-with-file", "-dwf",
					 help="Enable debug mode in file only", action="store_true", required=False)
	parser.add_argument("--debug-with-all", "-dwa",
					 help="Enable debug mode in both console and file", action="store_true", required=False)

	# parse the arguments
	args = parser.parse_args()
	return vars(args)
