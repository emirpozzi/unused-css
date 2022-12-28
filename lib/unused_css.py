import os
from lib.console import print_all_unused_classes, print_number_unused
from lib.functions import get_classes_in_css, get_files_by_extension, is_component, is_not_component, is_source_file, merge_files_content

def get_unused_global_css(style_files : tuple, html : str) -> tuple:
    """
    Given a list of the content of global style sheets/Sass module files, it returns CSS classes unused in html
    """
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
    """
    Given a list of the content of global style sheets/Sass module files, it returns CSS classes unused in html
    """
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

def get_unused_css(path):
    file_list_scss = get_files_by_extension(path, 'scss')
    file_list_css = get_files_by_extension(path, 'css')
    file_list_html = get_files_by_extension(path, 'html')
    
    style_files = file_list_scss + file_list_css

    source_code_style_files = tuple(filter(is_source_file, style_files))
    source_code_html = tuple(filter(is_source_file, file_list_html))

    not_component_style_files = tuple(filter(is_not_component, source_code_style_files))

    all_html = merge_files_content(source_code_html)
    (unused_classes, count) = get_unused_global_css(not_component_style_files, all_html )
    (unused_classes, count) = get_unused_component_css(unused_classes, source_code_style_files, count)
    
    print_all_unused_classes(unused_classes)
    print_number_unused(count)