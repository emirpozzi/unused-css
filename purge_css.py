from lib.functions import get_files_by_extension, get_classes_in_css
from lib.console import CONSOLE_BLUE, CONSOLE_ENDCOLOR, CONSOLE_GREEN
import os

# TODO build output string so that files with multiple unused classes get printed out once as:
# /User/foo - Unused: container, flex-container, bold

def main():
    '''
    - get all html files in any directory
    - for each file, get all unique css classes and save result
    - for each file, in same folder find html file with same name
    - for each html file search if any css class is not used
    '''
    root_path = os.getcwd()
    style_type_extension = "scss"

    file_list = get_files_by_extension(root_path, style_type_extension)

    class_list = {}
    for style_file in file_list:
        classes = get_classes_in_css(style_file)
        class_list[style_file] = classes

    count = 0
    for style_file in file_list:
        file_name, _ = os.path.splitext(style_file)
        html_file = file_name + ".html"

        try:
            with open(html_file) as f: 
                html_content = f.read()
        except:
            continue
            
        for css_class in class_list[style_file]:
            if css_class not in html_content:
                count = count + 1
                print(style_file)
                print(CONSOLE_BLUE, f"Not used: {css_class}", CONSOLE_ENDCOLOR, '\n')

    print(CONSOLE_GREEN, f"Unused CSS classes: {count}")
    

if __name__ == "__main__":
    main()



