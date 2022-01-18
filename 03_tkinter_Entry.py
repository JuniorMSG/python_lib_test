from tkinter import *
import requests
from bs4 import BeautifulSoup

"""
    입력창(Entry)
        생성       ent = Entry(win)
        내용 추출   ent.get()
        배치       ent.pack() 
    pip3 freeze > requirements.txt
"""
win = Tk()
win.geometry("1000x500")
win.title("python-gui-coding")
win.option_add("*Font", "맑은고딕 20")

ent = Entry(win)
ent.pack()

def ent_item():
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=996"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs={"class", "ball_645"}).get_text()

    a = ent.get()
    print(a)

btn = Button(win)
btn.config(text="버튼")
btn.config(command=ent_item)
btn.pack()


"""
    "__main__"
"""
if __name__ == "__main__":
    win.mainloop()