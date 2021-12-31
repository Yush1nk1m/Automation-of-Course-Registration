import pyautogui as pag
import time

file = open("location.txt", "wt")

print("수강신청 페이지의 'login' 버튼 위에 마우스를 올려 놓으십시오.")
print("마우스 좌표는 'location.txt' 파일에 저장됩니다.")
print("3초 뒤에 마우스 위치를 캡쳐합니다.")
time.sleep(1)
print("2초 뒤에 마우스 위치를 캡쳐합니다.")
time.sleep(1)
print("1초 뒤에 마우스 위치를 캡쳐합니다.")
time.sleep(1)

x, y = pag.position()
print("%d %d\n"%(x, y))

file.write("%d %d"%(x, y))

file.close()