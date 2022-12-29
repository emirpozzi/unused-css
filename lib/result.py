from lib.console import CONSOLE_GREEN

class Result:
    count = 0
    def __init__(self, count) -> None:
        if(count > 0):
            self.count = count

    def __str__(self) -> str:
        if(self.count > 0):
            return CONSOLE_GREEN + f"Unused CSS classes: {self.count}"
        else:
            return CONSOLE_GREEN + "No unused CSS classes found"