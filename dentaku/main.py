import tkinter as tk

class Dentaku():
    def __init__(self, root):
        self.tf = tk.Frame(root)
        self.tf.grid(column = 0, row = 0, padx = 15, pady = 15)

        self.current = "0"
        self.operation = None
        self.result = None

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
            (4, 1, "*", self.set_operation),
            (4, 2, "/", self.set_operation),
            (1, 3, "-", self.set_operation),
            (2, 3, "+", self.set_operation),
            (3, 3, "=", self.calculate),
            (4, 3, "C", self.clear))

        root.option_add('*Button.font', 'ＭＳゴシック 28')
        for r, c, label, func in ButtonDef:
            Button = tk.Button(self.tf, text=label)
            Button.bind("<Button-1>", func)
            Button.grid(column=c, row=r, sticky=tk.N + tk.E + tk.S + tk.W)

        root.option_add('*Entry.font', 'ＭＳゴシック 32')
        self.NumBox = tk.Entry(self.tf, width=10, justify=tk.RIGHT)
        self.NumBox.insert(tk.END, "0")
        self.NumBox.grid(column=0, columnspan=4, row=0)

    def numinput(self, e):
        num = e.widget.cget("text")
        if self.current == "0":
            self.current = num
        else:
            self.current += num
        self.update_numbox()

    def set_operation(self, e):
        if not self.result:
            self.result = int(self.current)
        self.current = "0"
        self.operation = e.widget.cget("text")

    def calculate(self, e):
        if self.operation:
            if self.operation == "+":
                self.result += int(self.current)
            elif self.operation == "-":
                self.result -= int(self.current)
            elif self.operation == "*":
                self.result *= int(self.current)
            elif self.operation == "/":
                self.result /= int(self.current)
            self.current = str(self.result)
            self.update_numbox()
            self.operation = None

    def clear(self, e):
        self.current = "0"
        self.operation = None
        self.result = None
        self.update_numbox()

    def update_numbox(self):
        self.NumBox.delete(0, tk.END)
        self.NumBox.insert(tk.END, self.current)

def main():
    root = tk.Tk()
    root.title("電卓L1")
    den = Dentaku(root)
    root.mainloop()

if __name__ == '__main__':
    main()
