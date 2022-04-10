from tkinter import Tk


class ExitCommand:
    def __init__(self, root: Tk):
        self.root = root

    def __call__(self, *args, **kwargs):
        self.root.destroy()
        print("Bye bye!")
        exit(0)
