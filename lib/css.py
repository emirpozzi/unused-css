import re
from lib.functions import CSS_SELECTOR_REGEX

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