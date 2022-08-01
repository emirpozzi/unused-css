from fnmatch import fnmatch
import os
import re


def get_files_by_extension(root, extension):
    pattern = f"*.{extension}"
    result = []

    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                result.append(os.path.join(path, name))
    
    return result


def get_classes_in_css(path):
    with open(path) as f: 
        content = f.read()

    regex = re.compile(r'\.([a-z][a-z0-9]*) {|\.([a-z][a-z0-9]*)(-[a-z0-9]+) {|([a-z][a-z0-9]*)(__[a-z0-9]+) {')
    matches = regex.findall(content)

    result = []
    if matches:
        for match in matches:
            element = ''.join(match)
            if element not in result: 
                result.append(element)
    
    return result
