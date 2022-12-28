import os
import sys
from lib.console import print_all_unused_classes, print_number_unused
from lib.unused_css import UnusedCss

def main():
    '''
    Get unused classes in all css/scss files
    '''
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        root_path = os.getcwd()

    logic = UnusedCss(root_path)
    (files, count) = logic.get_unused_css()

    print_all_unused_classes(files)
    print_number_unused(count)

if __name__ == "__main__":
    main()
