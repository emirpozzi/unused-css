import os
import sys
from lib.unused_css import get_unused_css

def main():
    '''
    Get unused classes in all css/scss files
    '''

    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        root_path = os.getcwd()

    get_unused_css(root_path)


if __name__ == "__main__":
    main()
