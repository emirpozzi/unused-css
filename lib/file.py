from fnmatch import fnmatch
import os
from lib.ignore_terms import IGNORE_TERMS


def get_files_by_extension(folder: str, extension: str) -> tuple:
    '''
    Finds all files with the input extension in the given folder
    '''
    pattern = f"*.{extension}"
    result = []

    for path, _, files in os.walk(folder):
        for name in files:
            if fnmatch(name, pattern):
                result.append(os.path.join(path, name))

    return tuple(result)


def merge_files_content(file_list: tuple[str]) -> str:
    '''
    Given a list of files path, gets all content of all files and returns a string
    '''
    result = ''
    for file in file_list:
        try:
            with open(file) as f:
                content = f.read()
            result = result + content
        except Exception:
            continue
    return result


def is_source_file(file_name: str) -> bool:
    '''
    File is source file, not an artifact
    '''
    return not any(term in file_name for term in IGNORE_TERMS)
