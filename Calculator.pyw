__author__ = "Dhanalakshmi Narala"

"""A simple desktop calculator application using tkinter library"""

from tkinter import *


def create_buttons(window, btn_width=5, btn_height=2, btn_bg="lavender", btn_fg="red"):
    """Creates buttons for calculator"""

    answer = Text(window, width=20, height=3)
    answer.grid(columnspan=4)

    button_1 = Button(window, text=" 1 ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 1))
    button_1.grid(column=0, row=1)

    button_2 = Button(window, text=" 2 ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 2))
    button_2.grid(column=1, row=1)

    button_3 = Button(window, text=" 3 ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 3))
    button_3.grid(column=2, row=1)

    divide = Button(window, text=" / ", width=btn_width, height=btn_height, border=1,
                    bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, "/"))
    divide.grid(column=3, row=1)

    button_4 = Button(window, text=" 4 ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 4))
    button_4.grid(column=0, row=2)

    button_5 = Button(window, text=" 5 ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 5))
    button_5.grid(column=1, row=2)

    button_6 = Button(window, text=" 6 ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 6))
    button_6.grid(column=2, row=2)

    multiply = Button(window, text=" x ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, "x"))
    multiply.grid(column=3, row=2)

    button_7 = Button(window, text=" 7 ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 7))
    button_7.grid(column=0, row=3)

    button_8 = Button(window, text=" 8 ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 8))
    button_8.grid(column=1, row=3)

    button_9 = Button(window, text=" 9 ", width=btn_width, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 9))
    button_9.grid(column=2, row=3)

    minus = Button(window, text=" - ", width=btn_width, height=btn_height,
                   border=1, bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, "-"))
    minus.grid(column=3, row=3)

    clear = Button(window, text="Clear", width=btn_width, height=btn_height, border=1,
                   bg=btn_bg, fg=btn_fg, command=lambda: clear_text(answer))
    clear.grid(column=0, row=4)

    button_0 = Button(window, text=" 0 ", width=btn_width*2+1, height=btn_height, border=1,
                      bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, 0))
    button_0.grid(columnspan=2, column=1, row=4)

    plus = Button(window, text=" + ", width=btn_width, height=btn_height, border=1,
                  bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, "+"))
    plus.grid(column=3, row=4)

    point = Button(window, text=" . ", width=btn_width, height=btn_height, border=1,
                   bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, "."))
    point.grid(column=0, row=5)

    equal = Button(window, text=" = ", width=btn_width*2+1, height=btn_height, border=1,
                   bg=btn_bg, fg=btn_fg, command=lambda: calculate_result(answer))
    equal.grid(columnspan=2, column=1, row=5)

    modulus = Button(window, text=" % ", width=btn_width, height=btn_height, border=1,
                     bg=btn_bg, fg=btn_fg, command=lambda: insert(answer, "%"))
    modulus.grid(column=3, row=5)
    return window


def insert(text, value):
    text.insert(END, value)


def clear_text(text):
    text.delete(1.0, END)


def calculate_result(text):
    expression = text.get(1.0, END)
    text.delete(1.0, END)
    try:
        result = eval(expression)
        text.insert(1.0, result)
    except Exception as error:
        text.insert(1.0, "Error")


def app():
    root = Tk()
    root.title("Calculator")
    root.geometry("200x280")
    root.resizable(width=False, height=False)
    root.configure(padx=12, pady=15, background='#ECEFF1')
    root = create_buttons(root)
    root.mainloop()


if __name__ == "__main__":
    app()