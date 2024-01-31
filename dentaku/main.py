import tkinter as tk

class Dentaku():
    def __init__(self, root):
        self.tf = tk.Frame(root)
        self.tf.grid(column=0, row=0, padx=15, pady=15)

        self.current = "0"
        self.operation = None
        self.result = None
        self.is_decimal_mode = False

        ButtonDef = (
            (4, 0, "0", self.numinput),
            (3, 0, "1", self.numinput),
            (3, 1, "2", self.numinput),
            (3, 2, "3", self.numinput),
            (2, 0, "4", self.numinput),
            (2, 1, "5", self.numinput),
            (2, 2, "6", self.numinput),
            (1, 0, "7", self.numinput),
            (1, 1, "8", self.numinput),
            (1, 2, "9", self.numinput),
            (1, 3, "*", self.set_operation),
            (2, 3, "/", self.set_operation),
            (3, 3, "-", self.set_operation),
            (4, 3, "+", self.set_operation),
            (4, 1, ".", self.numinput),
            (3, 4, "=", self.calculate),
            (4, 4, "C", self.clear)
        )

        root.option_add('*Button.font', 'ＭＳゴシック 28')
        for r, c, label, func in ButtonDef:
            Button = tk.Button(self.tf, text=label)
            Button.bind("<Button-1>", func)
            Button.grid(column=c, row=r, sticky=tk.N + tk.E + tk.S + tk.W)

        self.NumBox = tk.Entry(self.tf, width=10, justify=tk.RIGHT)
        self.NumBox.insert(tk.END, "0")
        self.NumBox.grid(column=0, columnspan=5, row=0)

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
