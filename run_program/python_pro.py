import psutil # python filename.py로 실행된 프로세스를 찾음

for proc in psutil.process_iter():
    try: # 프로세스 이름, PID값 가져오기
        processName = proc.name()
        processID = proc.pid
        # print(processName, processID)

        if self.end_prog_name[0] in processName:
            print(processName, proc.pid)
        # if 'chrome.exe'

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  # 예외처리
        pass
        if processName[:6] == "python": # 윈도우는 python.exe로 올라옴
            commandLine = proc.cmdline() # 동일한 프로세스 확인. code 확인 if 'filename.py' in commandLine: parent_pid = processID #PID parent = psutil.Process(parent_pid) # PID 찾기 for child in parent.children(recursive=True): #자식-부모 종료 child.kill() parent.kill() else: print(processName, ' ', commandLine, ' - ', processID) except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): #예외처리 pass print('동일 프로세스 확인 완료....')
