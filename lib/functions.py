from fnmatch import fnmatch
import os
import re

def get_files_by_extension(root, extension) -> tuple:
    '''
    Finds all files with the input extension in the root folder
    '''
    pattern = f"*.{extension}"
    result = []

    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                result.append(os.path.join(path, name))
    
    return tuple(result)

def get_classes_in_css(path) -> tuple:
    '''
    Given a CSS or SCSS file path, it gives back a list of all css in the file
    '''
    with open(path) as f: 
        content = f.read()

    CSS_SELECTOR_REGEX = r'\.([a-z][a-z0-9]*) {|\.([a-z][a-z0-9]*)(-[a-z0-9]+) {|([a-z][a-z0-9]*)(__[a-z0-9]+) {'
    regex = re.compile(CSS_SELECTOR_REGEX)
    matches = regex.findall(content)

    result = []
    if matches:
        for match in matches:
            element = ''.join(match)
            if element not in result: 
                result.append(element)
    
    return tuple(result)

def merge_files_content(file_list) -> str:
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

def is_component(file_name) -> bool:
    '''
    File path is for an Angular component file
    '''
    pattern = "*.component.*"
    return fnmatch(file_name, pattern)

def is_source_file(file_name) -> bool:
    '''
    File path is for a file in nodemodules/ and dist/
    '''
    return ("/node_modules/" not in file_name ) and ("/dist/" not in file_name)
