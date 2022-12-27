from fnmatch import fnmatch
import os
import re

CSS_SELECTOR_REGEX = r'\.-?[_a-zA-Z]+[_a-zA-Z0-9-]*\s*\{'

def get_files_by_extension(root : str, extension : str) -> tuple:
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

def get_classes_in_css(path : str) -> tuple:
    '''
    Given a CSS or SCSS file path, it gives back a list of all css in the file
    '''
    with open(path) as f: 
        content = f.read()

    regex = re.compile(CSS_SELECTOR_REGEX)
    matches = regex.findall(content)

    result = []
    if matches:
        for match in matches:
            element = match[1:-2]
            if element not in result: 
                result.append(element)
    
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

def get_unused_global_css(style_files : tuple, html : str) -> tuple:
    count = 0
    unused_classes = {}
    modules_class_list = { file : get_classes_in_css(file) for file in style_files }
    for style_file in style_files:
        unused_classes[style_file] = ''
        for css_class in modules_class_list[style_file]:
            if css_class not in html:
                count = count + 1
                unused_classes[style_file] += f" {css_class}"

    return (unused_classes, count)

def get_unused_component_css(unused_classes : dict, source_code_style_files : tuple, count : int):
    components_css = tuple(filter(is_component, source_code_style_files))
    component_class_list = { file : get_classes_in_css(file) for file in components_css }

    for style_file in components_css:
        file_without_extension, _ = os.path.splitext(style_file)
        html_file_path = file_without_extension + ".html"
        try:
            with open(html_file_path) as f: 
                html_content = f.read()
        except Exception:
            continue
            
        unused_classes[style_file] = ''
        for css_class in component_class_list[style_file]:
            if css_class not in html_content:
                count = count + 1
                unused_classes[style_file] += f" {css_class}"
    
    return (unused_classes, count)