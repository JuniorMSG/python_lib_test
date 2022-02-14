import keyboard
import threading
import pyautogui
from time import sleep



class Hook(threading.Thread):
    def __init__(self):
        super(Hook, self).__init__()  # parent class __init__ 실행
        self.daemon = True  # 데몬쓰레드로 설정
        self.event = False  # f4가 눌리면 event 발생
        keyboard.unhook_all()  # 후킹 초기화
        keyboard.add_hotkey('f4', print, args=['\nf4 was pressed'])  # f4가 눌리면 print 실행

    def run(self):  # run method override
        print('Hooking Started')
        while True:
            key = keyboard.read_hotkey(suppress=False)  # hotkey를 계속 읽음
            if key == 'f4':  # f4 받은 경우
                self.event = True  # event 클래스 변수를 True로 설정
                break  # 반복문 탈출



def track_pos():
    h = Hook()  # 훅 쓰레드 생성
    h.start()  # 쓰레드 실행
    print('size:', pyautogui.size())

    while True:
        if h.event == True:  # h.event가 True이면(f4 입력받은경우) 종료
            break
        position = pyautogui.position()
        print(f'\r{position.x:4}, {position.y:4}', end='')
        sleep(0.05)
    h.join()
    keyboard.unhook_all()  # 후킹해제


track_pos()