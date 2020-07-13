from tkinter import *

if __name__ == "__main__":
    root = Tk()

    mainFrame = Frame(root, height= 400, width=600)
    mainFrame.pack()

    topRow = Frame(mainFrame, height=200, width=600)
    topRow.pack(side=TOP)

    bottomRow  = Frame(mainFrame, height=200, width=600)
    bottomRow.pack(side=BOTTOM)

    leftTopFrame = Frame(topRow, height=200, width=300)
    leftTopFrame.pack(side=LEFT)

    rightTopFrame = Frame(topRow, height=200, width=300)
    rightTopFrame.pack(side=RIGHT)

    leftBottomFrame = Frame(bottomRow, height=200, width=300)
    leftBottomFrame.pack(side=LEFT)

    rightBottomFrame = Frame(bottomRow, height=200, width=300)
    rightBottomFrame.pack(side=RIGHT)

    root.mainloop()


