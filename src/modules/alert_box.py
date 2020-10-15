import tkinter as tk


class Example(object):
    def __init__(self):
        self.value = None
        self.root = None

    def show(self):
        self.root = tk.Tk()
        self.root.wm_geometry("300x50")
        tk.Label(
            master=self.root,
            text="You will be deleting a ticket, do you wish to continue?",
        ).pack()
        true_button = tk.Button(
            self.root, text="Continue", command=lambda: self.finish(True)
        )
        false_button = tk.Button(
            self.root, text="Cancel", command=lambda: self.finish(False)
        )

        true_button.pack(side=tk.RIGHT, padx=10)
        false_button.pack(side=tk.LEFT, padx=10)

        self.root.mainloop()
        return self.value

    def finish(self, value):
        self.value = value
        self.root.destroy()


if __name__ == "__main__":
    print("getting ready to show dialog...")
    print("value:", Example().show())
