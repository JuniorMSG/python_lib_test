import tkinter

window=tkinter.Tk()
window.title("SG")
window.geometry("640x400+100+100")
window.resizable(True, True)

image=tkinter.PhotoImage(file="21_.png")

label=tkinter.Label(window, image=image)
label.pack()

window.mainloop()