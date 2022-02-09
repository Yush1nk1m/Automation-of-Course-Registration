import pyautogui
import time
import datetime as dt
try :
    file = open("location.txt", "rt")
    x, y = file.readline().split()
    x = int(x)
    y = int(y)
    file.close()
except :
    print("'location.txt' 파일이 존재하지 않거나, 좌표값이 제대로 입력돼있지 않습니다.\nlocation 프로그램을 먼저 실행해 주십시오.")
    exit()

while True :
    try :
        sec = input("돌아오는 'OO.OO'초에 클릭합니다.\n입력하십시오(ex : 59.91) : ")
        s, ms = sec.split('.')
        if (s[:1] == '-') :
            print("음수를 입력할 수 없습니다. 다시 입력해 주십시오.")
            continue
        s = int(s)
        ms2 = int(ms)
        if (s >= 60) :
            print("초는 60 이하여야 합니다. 다시 입력해 주십시오.")
            continue
        if (len(ms) != 2) :
            print("초는 무조건 소수점 아래 두 자리로 입력해야 합니다. 다시 입력해 주십시오.")
            continue
        if (s < 0 or ms2 < 0) :
            print("음수를 입력할 수 없습니다. 다시 입력해 주십시오.")
            continue
        break
    except :
        print("숫자를 잘못 입력하셨습니다. 다시 입력해 주십시오.")
hour = dt.datetime.now().hour
minute = dt.datetime.now().minute
if dt.datetime.now().second > s :
    minute = (minute + 1) % 60
if (minute == 0) :
    hour = (hour + 1) % 24

print("%s시 %s분 %d.%s초에 (%d, %d)를 클릭합니다."%(hour, minute, s, ms, x, y))
ms2 *= 10000
while True :
    t = dt.datetime.now()
    if t.second == s and t.microsecond > ms2 :
        pyautogui.click(x, y) #로그인 버튼
        break
    else :
        time.sleep(0.0001)
        continue
