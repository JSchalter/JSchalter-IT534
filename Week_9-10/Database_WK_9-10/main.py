from tkinter import Tk
from gui.gui import BookApp

def main():
    """Entry point for the application."""
    root = Tk()
    root.title('Books Database')
    root.geometry("1000x500")
    app = BookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
