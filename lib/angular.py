from fnmatch import fnmatch
from lib.css import get_classes_in_css
from lib.file import get_files_by_extension
import os


class Angular:
    component_extension = "html"

    def __str__(self) -> str:
        return "Angular"

    def get_unused_component_css(self, style_files, files, count) -> tuple:
        """
        Given a list of the content of global style sheets/Sass module files, it returns CSS classes unused in html
        """
        components_css = tuple(filter(self.is_component, style_files))
        component_class_list = {file:
                                get_classes_in_css(file) for file in components_css}

        for style_file in components_css:
            file_without_extension, _ = os.path.splitext(style_file)
            html_file_path = file_without_extension + "." + self.component_extension
            try:
                with open(html_file_path) as f:
                    html_content = f.read()
            except Exception:
                continue

            files[style_file] = ''
            for css_class in component_class_list[style_file]:
                if css_class not in html_content:
                    count = count + 1
                    files[style_file] += f" {css_class}"

        return (files, count)

    def is_component(self, file_name: str) -> bool:
        '''
        File path is for an Angular component file
        '''
        pattern = "*.component.*"
        return fnmatch(file_name, pattern)

    def get_component_files(self, path: str) -> tuple:
        return get_files_by_extension(path, self.component_extension)
