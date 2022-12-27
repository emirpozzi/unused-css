import os
from lib.functions import get_classes_in_css, is_component

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