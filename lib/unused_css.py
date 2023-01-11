import os
from lib.css import get_classes_in_css
from lib.file import get_files_by_extension, is_source_file, merge_files_content

class UnusedCss:
    def __init__(self, path : str, framework):
        self.path = path
        self.count = 0
        self.files = {}
        self.framework = framework
    
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
    
    def get_unused_css(self) -> tuple:
        """
        Get all unused CSS in the project in path
        """
        file_list_scss = get_files_by_extension(self.path, 'scss')
        file_list_css = get_files_by_extension(self.path, 'css')
        file_list_html = get_files_by_extension(self.path, self.framework.component_extension)
        
        style_files = file_list_scss + file_list_css

        # TODO use list comprehension instead of filter??
        source_code_style_files = tuple(filter(is_source_file, style_files))
        source_code_html = tuple(filter(is_source_file, file_list_html))

        not_component_style_files = tuple(filter(self.is_not_component, source_code_style_files))

        all_html = merge_files_content(source_code_html)
        self.get_unused_global_css(not_component_style_files, all_html)
        (self.files, self.count) = self.framework.get_unused_component_css(source_code_style_files, self.files, self.count)

        return (self.files, self.count)
    
    def is_not_component(self, file_name : str):
        return not self.framework.is_component(file_name)