import tkinter

window=tkinter.Tk()
window.title("SG")
window.geometry("640x400+100+100")
window.resizable(True, True)

def command_args(argument1, argument2, argument3):
    global arg1
    arg1 = argument1 * 2
    print(argument1, argument2, argument3)

arg1 = 1
arg2 = "alpha"
arg3 = "beta"

button = tkinter.Button(window, width=25, height=10, text="버튼", command=lambda: command_args(arg1, arg2, arg3))
button.pack(expand=True, anchor="center")

window.mainloop()



import tkinter

class windows_tkinter:
    def __init__(self, window):
        self.window = window
        self.window.title("SG")
        self.window.geometry("640x400+100+100")
        self.window.resizable(True, True)

        self.arg1 = 1
        self.arg2 = "alpha"
        self.arg3 = "beta"
        self.__main__()

    def command_args(self, argument1, argument2, argument3):
        print(argument1, argument2, argument3)
        self.arg1 = argument1 * 2

    def __main__(self):
        button = tkinter.Button(self.window, width=25, height=10, text="버튼", command=lambda: self.command_args(self.arg1, self.arg2, self.arg3))
        button.pack(expand=True, anchor="center")

if __name__ == '__main__':
    window = tkinter.Tk()
    windows_tkinter(window)
    window.mainloop()