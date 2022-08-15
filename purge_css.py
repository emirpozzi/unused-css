from lib.functions import get_files_by_extension, get_classes_in_css, is_component, is_source_file, merge_files_content
from lib.console import print_number_unused, print_unused_classes, CONSOLE_BLUE, CONSOLE_ENDCOLOR, CONSOLE_GREEN
import os

def main():
    '''
    Get unused classes in all css/scss files
    '''
    root_path = os.getcwd()

    file_list_scss = get_files_by_extension(root_path, 'scss')
    file_list_css = get_files_by_extension(root_path, 'css')
    style_files = file_list_scss + file_list_css

    file_list_html = get_files_by_extension(root_path, 'html')
    source_code_css = tuple(filter(is_source_file, style_files))
    source_code_html = tuple(filter(is_source_file, file_list_html))

    is_not_component = lambda x: not is_component(x)
    modules_styles = tuple(filter(is_not_component, source_code_css))

    # Unused classes in Sass partials and global style sheets
    all_html = merge_files_content(source_code_html)
    count = 0
    unused_classes = {}
    modules_class_list = { file : get_classes_in_css(file) for file in modules_styles }
    for style_file in modules_styles:
        unused_classes[style_file] = ''
        for css_class in modules_class_list[style_file]:
            if css_class not in all_html:
                count = count + 1
                unused_classes[style_file] += f" {css_class}"

    # Unused classes in components style files
    components_css = tuple(filter(is_component, source_code_css))
    component_class_list = { file : get_classes_in_css(file) for file in components_css }
    for style_file in components_css:
        file_without_extension, _ = os.path.splitext(style_file)
        html_file = file_without_extension + ".html"
        try:
            with open(html_file) as f: 
                html_content = f.read()
        except Exception:
            continue
            
        unused_classes[style_file] = ''
        for css_class in component_class_list[style_file]:
            if css_class not in html_content:
                count = count + 1
                unused_classes[style_file] += f" {css_class}"

    # Output result
    for file in unused_classes.keys():
        if unused_classes[file]:
            print(file)
            print_unused_classes(unused_classes[file])

    print_number_unused(count)


if __name__ == "__main__":
    main()
