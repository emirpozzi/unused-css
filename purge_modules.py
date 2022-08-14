from lib.functions import get_files_by_extension, get_classes_in_css, is_not_component, is_source_file, merge_files_content
from lib.console import print_number_unused, print_unused_classes, CONSOLE_BLUE, CONSOLE_ENDCOLOR, CONSOLE_GREEN
import os

def main():
    '''
    Get unused classes in all modules and global style sheets
    '''
    root_path = os.getcwd()

    file_list_scss = get_files_by_extension(root_path, 'scss')
    file_list_html = get_files_by_extension(root_path, 'html')

    cleaned_css = tuple(filter(is_source_file, file_list_scss))
    cleaned_html = tuple(filter(is_source_file, file_list_html))

    modules_global_scss = tuple(filter(is_not_component, cleaned_css))

    all_html = merge_files_content(cleaned_html)
   
    count = 0
    unused_classes = {}
    class_list = { file : get_classes_in_css(file) for file in modules_global_scss }
    for style_file in modules_global_scss:
        unused_classes[style_file] = ''
        for css_class in class_list[style_file]:
            if css_class not in all_html:
                count = count + 1
                unused_classes[style_file] += f" {css_class}"

    
    for file in unused_classes.keys():
        if unused_classes[file]:
            print(file)
            print_unused_classes(unused_classes[file])

    print_number_unused(count)


if __name__ == "__main__":
    main()
