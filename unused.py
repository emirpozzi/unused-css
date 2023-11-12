import os
import sys
from lib.file_result import FileResult
from lib.framework import get_framework
from lib.result import Result
from lib.unused_css import UnusedCss


def main():
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        root_path = os.getcwd()

    framework = get_framework(root_path)
    print(f"Looking for unused CSS in {framework} project at {root_path}\n")

    logic = UnusedCss(root_path, framework)
    files, count = logic.get_unused_css()

    print(FileResult(files))
    print(Result(count))


if __name__ == "__main__":
    main()
