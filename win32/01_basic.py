from typing import cast
import win32gui
import win32api
import win32con

# WM_CREATE가 안생겨서 만든 WM_CREATE 대용 메시지
UM_CREATE = win32con.WM_USER + 1


class WindowProcFunc:
    def __init__(self):
        pass

    def OnCreate(self, hwnd, iMsg, wParam, lParam):
        pass

    def OnDestroy(self, hwnd, iMsg, wParam, lParam):
        win32gui.PostQuitMessage(0)

    def OnPaint(self, hwnd, iMsg, wParam, lParam):
        hdc, ps = win32gui.BeginPaint(hwnd)

        # hPen = win32gui.CreatePen(win32con.PS_DOT, 1, win32api.RGB(255, 0, 0))
        lb = {'Style': win32con.BS_SOLID, 'Color': win32api.RGB(255, 0, 0), 'Hatch': None}
        hPen = win32gui.ExtCreatePen(win32con.PS_COSMETIC | win32con.PS_DOT, 1, lb, None)
        oldPen = win32gui.SelectObject(hdc, hPen)

        win32gui.SetArcDirection(hdc, win32con.AD_CLOCKWISE)

        # 1번
        # win32gui.Arc(hdc, 300, 10, 400, 100, 400, 10, 400, 100)

        # 2번
        # win32gui.MoveToEx(hdc, 350, 150)
        # win32gui.ArcTo(hdc, 300, 10, 400, 100, 400, 10, 400, 100)

        # 3번
        win32gui.MoveToEx(hdc, 300, 100)
        win32gui.AngleArc(hdc, 300, 100, 100, 30, 60)

        # 4번
        prePos = win32gui.MoveToEx(hdc, 10, 10)
        win32gui.LineTo(hdc, 50, 50)

        # 5번
        polygonPos = ((10, 75), (125, 30), (250, 75), (175, 150), (75, 150))
        win32gui.Polyline(hdc, polygonPos)

        # 6번
        # prePos = win32gui.MoveToEx(hdc, 400, 400)
        # win32gui.PolylineTo(hdc,polygonPos)

        # 7번
        bezierPos = ((55, 215), (75, 100), (200, 300), (275, 75))
        # win32gui.PolyBezier(hdc, bezierPos)

        # 8번
        bezierToPos = ((75, 100), (200, 300), (275, 75))
        prePos = win32gui.MoveToEx(hdc, 55, 215)
        win32gui.PolyBezierTo(hdc, bezierToPos)

        win32gui.SelectObject(hdc, oldPen)
        win32gui.DeleteObject(hPen)

        arcDirect = win32gui.GetArcDirection(hdc)
        print(f"Arc Direct : {'시계방향' if win32con.AD_CLOCKWISE == arcDirect else '반시계방향'}")

        win32gui.EndPaint(hwnd, ps)

    def OnClose(self, hwnd, iMsg, wParam, lParam):
        win32gui.DestroyWindow(hwnd)


wndProcFunc = WindowProcFunc()

wndProc = {
    UM_CREATE: wndProcFunc.OnCreate,
    win32con.WM_DESTROY: wndProcFunc.OnDestroy,
    win32con.WM_PAINT: wndProcFunc.OnPaint,
    win32con.WM_CLOSE: wndProcFunc.OnClose,
}


def winMain():
    hInstance = win32api.GetModuleHandle()

    className = 'SimpleWin32'

    wndClass = win32gui.WNDCLASS()
    wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
    wndClass.lpfnWndProc = wndProc
    wndClass.hInstance = hInstance
    wndClass.hIcon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
    wndClass.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
    wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
    wndClass.lpszClassName = className

    wndClassAtom = win32gui.RegisterClass(wndClass)

    hwnd = win32gui.CreateWindow(
        wndClassAtom,
        "title test",
        win32con.WS_OVERLAPPEDWINDOW | win32con.WS_VSCROLL | win32con.WS_HSCROLL,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        win32con.CW_USEDEFAULT,
        0,
        0,
        hInstance,
        None)

    win32gui.SendMessage(hwnd, UM_CREATE, 0, 0)

    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32gui.UpdateWindow(hwnd)

    win32gui.PumpMessages()
    return 0


if __name__ == "__main__":
    x = winMain()