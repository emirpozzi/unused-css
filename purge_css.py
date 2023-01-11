import os
import sys
from lib.angular import Angular
from lib.console import print_all_unused_classes
from lib.result import Result
from lib.unused_css import UnusedCss

def main():
    '''
    Get unused classes in all css/scss files
    '''
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        root_path = os.getcwd()

    logic = UnusedCss(root_path, Angular())
    files, count = logic.get_unused_css()
    
    print_all_unused_classes(files)
    print(Result(count))

if __name__ == "__main__":
    main()
