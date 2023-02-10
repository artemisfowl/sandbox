'''
	@brief Utility module containing filesystem related routines
	@date Fri, 10 Feb 2023 06:56:20 +0530
'''

from pathlib import Path
from os import makedirs

def fsystem_create_dir(dir_path: str) -> bool:
	if not isinstance(dir_path, str):
		return False
	if not Path(dir_path).exists():
		makedirs(dir_path)
	return True
