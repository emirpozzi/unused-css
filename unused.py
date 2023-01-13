import os
import sys
from lib.angular import Angular
from lib.file_result import FileResult
from lib.result import Result
from lib.unused_css import UnusedCss

# TODO rename lib in src
# TODO rename any purge to unusedCSS
# TODO update README, not only Angular also React
# TODO add in readme no packages needed to run?


def main():
    '''
    Get unused classes in all css/scss files
    '''
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        root_path = os.getcwd()

    # TODO set up script to detect if project is Angular or React based on package.json
    logic = UnusedCss(root_path, Angular())
    files, count = logic.get_unused_css()

    print(FileResult(files))
    print(Result(count))


if __name__ == "__main__":
    main()
