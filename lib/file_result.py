CONSOLE_GREEN = "\033[92m"
CONSOLE_BLUE = "\033[96m"
CONSOLE_ENDCOLOR = "\033[0m"


class FileResult:
    def __init__(self, unused_classes: dict) -> None:
        self.unused_classes = unused_classes

    def __str__(self) -> str:
        output = ""
        for file in self.unused_classes.keys():
            if self.unused_classes[file]:
                output += file + CONSOLE_BLUE + "\n" + \
                    f"Not used:{self.unused_classes[file]}" + \
                    CONSOLE_ENDCOLOR + '\n\n'
        # Remove last new line
        return output[:-1]
