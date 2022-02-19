import ctypes
import os
import subprocess
import time

proc = subprocess.Popen(
    ['1.exe', '1'],
    stdout=subprocess.PIPE
)
#
# while proc.poll() is None:
#     print('Working...')
#     # 시간이 걸리는 작업을 몇 개 수행

print('Exit status', proc.poll())

calc = ("c:\windows\system32\\calc.exe")
notepad = ("c:\windows\system32\\notepad.exe")
paint = ("c:\windows\system32\\mspaint.exe")

ctypes.windll.shell32.ShellExecuteA(0, 'open', calc, None, None, 1)
ctypes.windll.shell32.ShellExecuteA(0, 'open', notepad, None, None, 1)
ctypes.windll.shell32.ShellExecuteA(0, 'open', paint, None, None, 1)