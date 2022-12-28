CONSOLE_GREEN = "\033[92m"
CONSOLE_BLUE = "\033[96m"
CONSOLE_ENDCOLOR = "\033[0m"

def print_all_unused_classes(unused_classes : dict) -> None:
    for file in unused_classes.keys():
        if unused_classes[file]:
            print(file)
            print(CONSOLE_BLUE, f"Not used:{unused_classes[file]}", CONSOLE_ENDCOLOR, '\n')
