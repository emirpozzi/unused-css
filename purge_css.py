import os
from lib.functions import get_files_by_extension, is_source_file, merge_files_content, get_unused_global_css, is_not_component, get_unused_component_css
from lib.console import print_number_unused, print_all_unused_classes

def main():
    '''
    Get unused classes in all css/scss files
    '''
    root_path = os.getcwd()

    file_list_scss = get_files_by_extension(root_path, 'scss')
    file_list_css = get_files_by_extension(root_path, 'css')
    style_files = file_list_scss + file_list_css

    file_list_html = get_files_by_extension(root_path, 'html')
    source_code_style_files = tuple(filter(is_source_file, style_files))
    source_code_html = tuple(filter(is_source_file, file_list_html))

    not_component_style_files = tuple(filter(is_not_component, source_code_style_files))

    all_html = merge_files_content(source_code_html)
    (unused_classes, count) = get_unused_global_css(not_component_style_files, all_html )
    (unused_classes, count) = get_unused_component_css(unused_classes, source_code_style_files, count)
    
    print_all_unused_classes(unused_classes)
    print_number_unused(count)


if __name__ == "__main__":
    main()
