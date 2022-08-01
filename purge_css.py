from lib.functions import get_files_by_extension, get_classes_in_css
import os

"""
STEPS:
- get all html files in any directory
- for each file, get all unique css classes and save result
- for each file, in same folder find html file with same name
- for each html file search if any css class is not used
"""
# TODO build output string so that files with multiple unused classes get printed out once as:
# /User/foo - Unused: container, flex-container, bold

def main():
    root_path = os.getcwd()
    style_type_extension = "scss"

    file_list = get_files_by_extension(root_path, style_type_extension)

    class_list = {}
    count = 0
    for file in file_list:
        classes = get_classes_in_css(file)
        class_list[file] = classes

    for file in file_list:
        html_file = file[:-4] + "html"
        try:
            with open(html_file) as f: 
                content = f.read()
        except:
            continue
            
        for css_class in class_list[file]:
            if css_class not in content:
                count = count + 1
                print(file)
                print(f"\033[96m" + "Not used: " + css_class + '\033[0m' + '\n')

    print(f"\033[92mUnused CSS classes: {count}")
    

if __name__ == "__main__":
    main()



