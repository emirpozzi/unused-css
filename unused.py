import os
import sys
from lib.angular import Angular
from lib.react import React
from lib.file_result import FileResult
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

    framework = get_framework(root_path)
    print(
        f"\nLooking for unused CSS in {framework} project at {root_path}\n")

    logic = UnusedCss(root_path, framework)
    files, count = logic.get_unused_css()

    print(FileResult(files))
    print(Result(count))


def get_framework(root_path) -> Angular | React:
    try:
        with open(root_path + "/package.json") as f:
            content = f.read()
            if "@angular/core" in content:
                return Angular()
            if "react" in content:
                return React()
            print(
                "\nUnsupported framework. UnusedCSS works with Angular and React based projects.")
            exit(1)
    except Exception:
        print("\nUnable to find a package.json file. Please make sure you are running in the root folder.")
        exit(1)


if __name__ == "__main__":
    main()
