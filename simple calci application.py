import tkinter as tk
from tkinter import messagebox
import math
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.equation = ""
        self.memory = 0

        self.display = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 18))
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('^', 5, 2), ('M+', 5, 3),
            ('MR', 6, 0), ('MC', 6, 1)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col, sticky="nsew")

    def button_click(self, text):
        if text == 'C':
            self.equation = ""
        elif text == '=':
            try:
                self.equation = str(eval(self.equation))
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero")
                self.equation = ""
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
                self.equation = ""
        elif text == '√':
            try:
                self.equation = str(math.sqrt(eval(self.equation)))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
                self.equation = ""
        elif text == '^':
            self.equation += '**'
        elif text == 'M+':
            try:
                self.memory += eval(self.equation)
                self.equation = ""
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
                self.equation = ""
        elif text == 'MR':
            self.equation = str(self.memory)
        elif text == 'MC':
            self.memory = 0
            self.equation = ""
        else:
            self.equation += text

        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.equation)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
