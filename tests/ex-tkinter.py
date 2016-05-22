import os
import tkinter


def main():
    msg = 'hello world'

    def show(n):
        m = "%s: %s" % (n, os.environ.get(n))
        print(m)
        return m

    msg += "\n" + show("TCL_LIBRARY")
    msg += "\n" + show("TK_LIBRARY")

    root = tkinter.Tk()
    tkinter.Label(root, text=msg).grid(column=0, row=0)
    root.mainloop()

if __name__ == '__main__':
    main()
