# python_gui

![image](https://user-images.githubusercontent.com/22822369/149247449-6378c9f8-9c9e-4c6d-a846-e7a78aef1925.png)


![image](https://user-images.githubusercontent.com/22822369/149247503-26d3db3c-73b9-4034-bd54-8a570b5b45cb.png)

## :hammer: Tech Stack
![Stack](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)

PyQt5 vs tkinter
### :hammer: etc Error List
pyinstaller 사용시 exe파일에서 크롬드라이버 뜨는 에러 <br>
https://codechacha.com/ko/python-selenium-remove-chromedriver-console-with-pyinstall/

### :fire: Project description
    파이썬의 tkinter or pyqt5 GUI를 구현하고 
    자주 구현하는 GUI에 대한
    개인 라이브러리용 repo



### use tkinter 
```
from tkinter import *
win = Tk()

# Size
win.geometry("1000x500")

# Title
win.title("python-gui-coding")

# Font
win.option_add("*Font", "맑은고딕 25")

# BackGroud Color
win.configure(bg="red")

win.mainloop()
```
