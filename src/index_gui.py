from tkinter import Tk
from ui.ui_tkinter import UI



def main():

    window = Tk()
    window.title("MiukuM@uku")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
    