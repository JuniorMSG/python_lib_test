import os
import time, win32con, win32api, win32gui
from io import BytesIO
import win32clipboard
from PIL import Image
import pyautogui
import pyperclip

# # 카톡창 이름, (활성화 상태의 열려있는 창)
kakao_opentalk_name = 'MS'

hwnd = win32gui.FindWindow(None, "카카오톡")
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)



def search_friend(name):
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.hotkey('esc')
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy(name)
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('enter')

def kakao_sendPy():
    # # 핸들 _ 채팅방

    pyperclip.copy('Hello, World!')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    for img in os.listdir('send_img/1'):
        filepath = 'send_img/1/' + img
        image = Image.open(filepath)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        send_to_clipboard(win32clipboard.CF_DIB, data)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.hotkey('enter')

    time.sleep(3)
    pyautogui.hotkey('alt', 'f4')

# # 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    # # 핸들 _ 채팅방
    hwndMain = win32gui.FindWindow(None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RICHEDIT50W", None)
    # hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)
    time.sleep(1)
    for img in os.listdir('send_img/1'):
        filepath = 'send_img/1/' + img
        image = Image.open(filepath)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        send_to_clipboard(win32clipboard.CF_DIB, data)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.hotkey('enter')
        SendReturn(hwndEdit)


# # 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# # 채팅방 열기
def open_chatroom():
    # 친구 검색
    # hwndkakao = win32gui.FindWindow(None, "카카오톡")
    # hwndkakao_edit1 = win32gui.FindWindowEx(hwndkakao, None, "EVA_ChildWindow", None)
    # hwndkakao_edit2_1 = win32gui.FindWindowEx(hwndkakao_edit1, None, "EVA_Window", None)
    # hwndkakao_edit3 = win32gui.FindWindowEx(hwndkakao_edit2_1, None, "Edit", None)

    # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

    win32gui.ShowWindow(hwndkakao_edit2_2, 5)
    win32gui.SetForegroundWindow(hwndkakao_edit2_2)

    # # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    # win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    # time.sleep(1)   # 안정성 위해 필요
    # SendReturn(hwndkakao_edit3)
    # time.sleep(1)


def main():
    # open_chatroom(kakao_opentalk_name)  # 채팅방 열기
    #
    # text = "test"
    # kakao_sendtext(kakao_opentalk_name, text)    # 메시지 전송
    data_lst = ['패스트캠퍼스', 'MS', '카카오프렌즈']
    for data in data_lst:
        open_chatroom()
        search_friend(data)
        kakao_sendPy()

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()




if __name__ == '__main__':
    main()