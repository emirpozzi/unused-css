from fnmatch import fnmatch
import os

CSS_SELECTOR_REGEX = r'\.-?[_a-zA-Z]+[_a-zA-Z0-9-]*\s*\{'

def get_files_by_extension(root : str, extension : str) -> tuple:
    '''
    Finds all files with the input extension in the root folder
    '''
    pattern = f"*.{extension}"
    result = []

    for path, _, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                result.append(os.path.join(path, name))
    
    return tuple(result)

def merge_files_content(file_list : list) -> str:
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

def is_component(file_name : str) -> bool:
    '''
    File path is for an Angular component file
    '''
    pattern = "*.component.*"
    return fnmatch(file_name, pattern)

is_not_component = lambda x: not is_component(x)

def is_source_file(file_name : str) -> bool:
    '''
    File is source file, not an artifact
    '''
    return ("/node_modules/" not in file_name ) and ("/dist/" not in file_name) and ("/coverage/" not in file_name)