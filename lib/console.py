CONSOLE_GREEN = "\033[92m"
CONSOLE_BLUE = "\033[96m"
CONSOLE_ENDCOLOR = "\033[0m"

def print_number_unused(count):
    if(count):
        print(CONSOLE_GREEN, f"Unused CSS classes: {count}")
    else:
        print(CONSOLE_GREEN, "No unused CSS classes found")

def print_unused_classes(file):
    print(CONSOLE_BLUE, f"Not used:{file}", CONSOLE_ENDCOLOR, '\n')
