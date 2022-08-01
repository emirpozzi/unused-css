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

    file_list_scss = get_files_by_extension(root_path, 'scss')
    file_list_css = get_files_by_extension(root_path, 'css')
    style_files = file_list_scss + file_list_css

    class_list = { file : get_classes_in_css(file) for file in style_files }

    count = 0
    for style_file in style_files:
        file_without_extension, _ = os.path.splitext(style_file)
        html_file = file_without_extension + ".html"

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



