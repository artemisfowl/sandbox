'''
	@brief Utility module component containing all logging related routines
	@date Fri, 10 Feb 2023 00:26:02 +0530
'''

from logging import getLogger, StreamHandler, FileHandler, Formatter
from logging import INFO

from .constants import LOGGER_FILE, LOGGER_FORMAT, LOGGER_INSTANCE, LOGGER_DIR
from .filesystem import fsystem_create_dir

def log_setup(logger_module_name: str=LOGGER_INSTANCE, log_to_file: bool=False,
			  log_to_stdout: bool=True, log_level: int=INFO):
	logger = getLogger(logger_module_name)
	logger.setLevel(log_level)

	# handler instances
	file_handler = None
	stdout_handler = None

	# logging format
	logging_format = Formatter(LOGGER_FORMAT)

	# enable handlers based on the flags
	if log_to_file:
		if not fsystem_create_dir(LOGGER_DIR):
			print("Something went wrong while trying to create the directory for log files")

		logger_fpath = f"{LOGGER_DIR}{LOGGER_FILE}"
		file_handler = FileHandler(logger_fpath)
		file_handler.setLevel(log_level)
		file_handler.setFormatter(logging_format)
		logger.addHandler(file_handler)

	if log_to_stdout:
		stdout_handler = StreamHandler()
		stdout_handler.setLevel(log_level)
		stdout_handler.setFormatter(logging_format)
		logger.addHandler(stdout_handler)

