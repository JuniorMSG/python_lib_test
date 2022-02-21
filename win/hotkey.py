from pynput.keyboard import Listener, Key, KeyCode
import win32api
import win32gui
import win32con

store = set()

HOT_KEYS = {
    'print_hello': set([Key.alt_l, KeyCode(char='1')])
    , 'open_notepad': set([Key.alt_l, KeyCode(char='2')])
}



def print_hello():
    print('hello, World!!!')


def open_notepad():
    print('open_notepad')
    try:
        win32api.WinExec('notepad.exe')
    except Exception as err:
        print(err)


def handleKeyPress(key):
    store.add(key)

    for action, trigger in HOT_KEYS.items():
        CHECK = all([True if triggerKey in store else False for triggerKey in trigger])

        if CHECK:
            try:
                action = eval(action)
                if callable(action):
                    action()
            except NameError as err:
                print(err)


def handleKeyRelease(key):
    if key in store:
        store.remove(key)

    # 종료
    if key == Key.esc:
        return False


with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()


if __name__ == "__main__":
    # 마우스의 위치 좌표 알아내기
    win32api.GetCursorPos()


    # 마우스의 위치를 지정하여 옮기기
    win32api.SetCursorPos((100, 200))

    # 특정 위치의 픽셀의 색상 알아내기
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 1000, 777)
    print(hex(color))

    # 마우스 클릭 & 드래그
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -100, -100, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    hwnd = win32gui.FindWindow(None, "계산기")
    print(hwnd)
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)