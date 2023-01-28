from lib.angular import Angular
from lib.react import React


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
