# ref: https://github.com/ta93-ito/ict-app-2/blob/main/dentaku/main.py

import tkinter as tk
import math

class Dentaku():
    def __init__(self, root):
        self.tf = tk.Frame(root)
        self.tf.grid(column=0, row=0, padx=15, pady=15)

        self.current = "0"
        self.operation = None
        self.result = None
        self.is_decimal_mode = False
        self.memory = 0

        ButtonDef = (
            (5, 0, "0", self.numinput),
            (4, 0, "1", self.numinput),
            (4, 1, "2", self.numinput),
            (4, 2, "3", self.numinput),
            (3, 0, "4", self.numinput),
            (3, 1, "5", self.numinput),
            (3, 2, "6", self.numinput),
            (2, 0, "7", self.numinput),
            (2, 1, "8", self.numinput),
            (2, 2, "9", self.numinput),
            (2, 3, "*", self.set_operation),
            (3, 3, "/", self.set_operation),
            (4, 3, "-", self.set_operation),
            (5, 3, "+", self.set_operation),
            (5, 1, ".", self.numinput),
            (4, 4, "=", self.calculate),
            (5, 4, "C", self.clear)
        )

        ExtraButtonDef = (
            (1, 0, "MC", self.memory_clear),
            (1, 1, "MR", self.memory_recall),
            (1, 2, "MS", self.memory_save),
            (1, 3, "M+", self.memory_add),
            (1, 4, "M-", self.memory_subtract),
            (6, 0, "税込", self.add_tax),
            (6, 1, "税抜", self.subtract_tax),
            (6, 2, "√", self.square_root),
            (6, 3, "±", self.toggle_sign)
        )

        root.option_add('*Button.font', 'ＭＳゴシック 28')

        self.NumBox = tk.Entry(self.tf, width=20, font=('ＭＳゴシック', 18), justify=tk.RIGHT)
        self.NumBox.insert(tk.END, "0")
        self.NumBox.grid(column=0, columnspan=5, row=0)

        for r, c, label, func in ButtonDef + ExtraButtonDef:
            Button = tk.Button(self.tf, text=label)
            Button.bind("<Button-1>", func)
            Button.grid(column=c, row=r, sticky=tk.N + tk.E + tk.S + tk.W)

    def numinput(self, e):
        num = e.widget.cget("text")
        if self.current == "0" and num != ".":
            self.current = num
        elif num == "." and "." not in self.current:
            self.current += "."
            self.is_decimal_mode = True
        elif num != ".":
            self.current += num
        self.update_numbox()

    def set_operation(self, e):
        if self.result is None:
            self.result = float(self.current)
        else:
            if self.operation:
                self.calculate(None)
        self.current = "0"
        self.operation = e.widget.cget("text")
        self.is_decimal_mode = False

    def calculate(self, e):
        if self.operation:
            try:
                self.result = eval(f"{self.result}{self.operation}float('{self.current}')")
            except ZeroDivisionError:
                self.result = "Error"
            else:
                self.result = int(self.result) if self.result.is_integer() else self.result
            self.current = str(self.result)
            self.update_numbox()
            self.operation = None
            self.is_decimal_mode = False

    def clear(self, e):
        self.current = "0"
        self.operation = None
        self.result = None
        self.is_decimal_mode = False
        self.update_numbox()

    def memory_clear(self, e):
        self.memory = 0

    def memory_recall(self, e):
        self.current = str(self.memory)
        self.update_numbox()

    def memory_save(self, e):
        self.memory = float(self.current)

    def memory_add(self, e):
        self.memory += float(self.current)

    def memory_subtract(self, e):
        self.memory -= float(self.current)

    def add_tax(self, e):
        result = float(self.current) * 1.1
        if abs(result - round(result)) < 1e-10:
            result = round(result) 
        self.current = str(result)
        self.update_numbox()

    def subtract_tax(self, e):
        result = float(self.current) / 1.1
        self.current = str(int(result)) if result.is_integer() else str(result)
        self.update_numbox()

    def square_root(self, e):
        result = math.sqrt(float(self.current))
        if abs(result - round(result)) < 1e-10:
            result = round(result)
        self.current = str(result)
        self.update_numbox()

    def toggle_sign(self, e):
        result = -float(self.current)
        if abs(result - round(result)) < 1e-10:
            result = round(result)
        self.current = str(result)
        self.update_numbox()

    def update_numbox(self):
        self.NumBox.delete(0, tk.END)
        self.NumBox.insert(tk.END, self.current)

def main():
    root = tk.Tk()
    root.title("電卓")
    den = Dentaku(root)
    root.mainloop()

if __name__ == '__main__':
    main()
