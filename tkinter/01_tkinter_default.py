from tkinter import *

win = Tk()
win.geometry("1000x500")
win.title("python-gui-coding")
win.option_add("*Font", "맑은고딕 25")
win.configure(bg="red")

btn = Button(win, text="버튼")
btn.pack()



"""
    "__main__"
"""
if __name__ == "__main__":
    win.mainloop()