import os
from lib.css import get_classes_in_css
from lib.file import get_files_by_extension, is_component, is_source_file, merge_files_content, is_not_component

class UnusedCss:
    def __init__(self, path : str):
        self.path = path
        self.count = 0
        self.files = {}
    
    def get_unused_global_css(self, style_files : tuple, html : str):
        """
        Given a list of the content of global style sheets/Sass module files, it returns CSS classes unused in html
        """
        modules_class_list = { file : get_classes_in_css(file) for file in style_files }
        for style_file in style_files:
            self.files[style_file] = ''
            for css_class in modules_class_list[style_file]:
                if css_class not in html:
                    self.count = self.count + 1
                    self.files[style_file] += f" {css_class}"
    
    def get_unused_component_css(self, style_files : tuple):
        """
        Given a list of the content of global style sheets/Sass module files, it returns CSS classes unused in html
        """
        components_css = tuple(filter(is_component, style_files))
        component_class_list = { file : get_classes_in_css(file) for file in components_css }

        for style_file in components_css:
            file_without_extension, _ = os.path.splitext(style_file)
            html_file_path = file_without_extension + ".html"
            try:
                with open(html_file_path) as f: 
                    html_content = f.read()
            except Exception:
                continue
                
            self.files[style_file] = ''
            for css_class in component_class_list[style_file]:
                if css_class not in html_content:
                    self.count = self.count + 1
                    self.files[style_file] += f" {css_class}"

    def get_unused_css(self) -> tuple:
        """
        Get all unused CSS in the project in path
        """
        file_list_scss = get_files_by_extension(self.path, 'scss')
        file_list_css = get_files_by_extension(self.path, 'css')
        file_list_html = get_files_by_extension(self.path, 'html')
        
        style_files = file_list_scss + file_list_css

        source_code_style_files = tuple(filter(is_source_file, style_files))
        source_code_html = tuple(filter(is_source_file, file_list_html))

        not_component_style_files = tuple(filter(is_not_component, source_code_style_files))

        all_html = merge_files_content(source_code_html)
        self.get_unused_global_css(not_component_style_files, all_html)
        self.get_unused_component_css(source_code_style_files)

        return (self.files, self.count)