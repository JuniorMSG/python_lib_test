from tkinter import *
from datetime import datetime
"""
    버튼(Btn)
        생성       btn = Button(win)
        옵션추가    btn.config(="현재 시각", width=30)
            text    | 버튼 텍스트
            width   | 가로 사이즈
            command | 기능 실행
        배치       btn.pack() 
"""
win = Tk()
win.geometry("1000x500")
win.title("python-gui-coding")
win.option_add("*Font", "맑은고딕 25")
win.configure(bg="red")


def btn_click_print():
    d_time = datetime.now()
    btn.config(text=d_time)


# Btn 생성
btn = Button(win)

# Btn 옵션
btn.config(text="현재 시각", width=30)
btn.config(comman=btn_click_print)

btn.pack()

if __name__ == "__main__":
    win.mainloop()