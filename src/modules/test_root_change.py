import tkinter as tk


class main(tk.Tk):
    def __init__(self, root):
        self.root = root
        label = tk.Label(self.root, text="Testing, attention please.")
        label.pack(fill=tk.X)
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    ob1 = main(root)
