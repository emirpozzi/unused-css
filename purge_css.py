from lib.functions import get_files_by_extension, get_classes_in_css
from lib.console import CONSOLE_BLUE, CONSOLE_ENDCOLOR, CONSOLE_GREEN
import os

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
    unused_classes = {}
    for style_file in style_files:
        file_without_extension, _ = os.path.splitext(style_file)
        html_file = file_without_extension + ".html"

        try:
            with open(html_file) as f: 
                html_content = f.read()
        except Exception:
            # The style sheet is not for a component (ex. global, scss module...)
            continue
            
        unused_classes[style_file] = ''
        for css_class in class_list[style_file]:
            if css_class not in html_content:
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



