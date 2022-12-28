import os
import sys
from lib.console import print_all_unused_classes, print_number_unused
from lib.unused_css import get_unused_css

def main():
    '''
    Get unused classes in all css/scss files
    '''
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        root_path = os.getcwd()

    (unused_classes, count) = get_unused_css(root_path)

    print_all_unused_classes(unused_classes)
    print_number_unused(count)


if __name__ == "__main__":
    main()
