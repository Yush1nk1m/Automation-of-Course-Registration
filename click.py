import pyautogui
import datetime as dt
import time

print("[로그인 버튼 클릭]\n")
print("이 프로그램은 사용자에게 서버 시간과 시스템 시간 간 시차 측정을 요구합니다.")
print("파일을 여러 번 실행하며 시스템 시간과 서버 시간을 미리 측정해 주시기 바랍니다.\n")
print("반드시 해상도 1920 * 1080 설정 및 인터넷 창을 전체 화면으로 설정해 주시기 바랍니다.")
print("또는 다시 로그인 버튼을 화면의 (x, y) = (1200, 330) 좌표에 위치시키면 됩니다.\n")

sec = input("매분 x.x초에 클릭합니다. x.x를 입력하십시오. (ex : 1.2) : ")

s, ms = sec.split('.')
s = int(s)
ms = int(ms) * 100000

endbool = False
while not endbool :
    t = dt.datetime.now()
    if t.second == s and t.microsecond > ms :
        pyautogui.click(1200, 330) #로그인 버튼
        #pyautogui.click(726, 467) #다시 로그인 버튼 (서버 시간 확인)
        endbool = True
    else :
        time.sleep(0.01)