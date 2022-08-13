from fnmatch import fnmatch
from lib.functions import get_files_by_extension, get_classes_in_css
from lib.console import CONSOLE_BLUE, CONSOLE_ENDCOLOR, CONSOLE_GREEN
import os

def is_not_component(file_name):
    pattern = "*.component.*"
    return not fnmatch(file_name, pattern)

def is_source_file(file_name):
    return ("/node_modules/" not in file_name ) and ("/dist/" not in file_name)

def main():
    root_path = os.getcwd()

    file_list_scss = get_files_by_extension(root_path, 'scss')
    file_list_html = get_files_by_extension(root_path, 'html')

    cleaned_css = tuple(filter(is_source_file, file_list_scss))
    cleaned_html = tuple(filter(is_source_file, file_list_html))

    modules_global_scss = tuple(filter(is_not_component, cleaned_css))

    all_html = ""
    for file in cleaned_html: 
        with open(file) as f: 
            content = f.read()
        all_html = all_html + content
    
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
            print(CONSOLE_BLUE, f"Not used:{unused_classes[file]}", CONSOLE_ENDCOLOR, '\n')

    if(count):
        print(CONSOLE_GREEN, f"Unused CSS classes: {count}")
    else:
        print(CONSOLE_GREEN, "No unused CSS classes found")


if __name__ == "__main__":
    main()
