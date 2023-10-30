# 각각의 Red, Green, Blue 가 있는 ScreenShot에서 각각 색별로 좌표를 찾아준다
# 그 후 해당위치의 RGB 값을 찾는다 
# Red -> (255,0,0) / Green -> (0,255,0) / Blue -> (0,0,255) 
# 위의 색상 표준 값을 이용
# 직접 코드에 사용한 값은
# Red -> (255, 49, 35) / Green -> (22, 157, 74) / Blue -> (61, 78, 208)
# 이다
# 이 값들을 이용해 각각의 색상을 구분하고 print를 이용해 출력해준다
# 그 후 메모장 (notepad)를 열어 print의 값을 입력해준다

from PIL import ImageGrab 
# 이미지 캡처를 위한 모듈
import pyautogui as pag
# 마우스 위치와 픽셀 색상을 가져오기 위한 모듈

screen = ImageGrab.grab()
# 화면을 캡처하여 이미지 객체를 만든다
pos = pag.position()
# 마우스 포인터의 현재 위치를 가져온다
print(pos)
# 마우스 포인터의 위치를 출력
screen.getpixel(pos)
# 이미지 객체인 'screen'에서 'pos' 변수에 저장된 좌표의 픽셀 색상을 가져온다


# In[110]:


import pyautogui
# 마우스 및 키보드 제어를 위한 모듈
from subprocess import Popen
# 외부 프로그램 실행을 위한 모듈
import time
# 시간 지연을 위한 모듈

def color_def():
# color_def() 함수 정의
    a = 0
    BLUE = (61, 78, 208)
    RED = (255, 49, 35)
    GREEN = (22, 157, 74)
    # 각각의 알맞는 RGB값 대입
    
    screen = ImageGrab.grab()
    # 화면의 스크린샷을 캡처
    pos = pag.position()
    # 현재 마우스 커서의 위치를 가져온다
    rgb = screen.getpixel(pos)
     # 마우스 커서 위치에서 픽셀의 RGB 색상 값을 가져온다
    if rgb == BLUE: 
        a = "blue"
    elif rgb == RED: 
        a = "red"
    elif rgb == GREEN:
        a = "green"
    else:
        a = "not found"
    # RGB 색상을 확인하여 'a' 변수에 결과를 할당
    return a
    # a값 반환
result = color_def()
# color_def() 함수를 호출하여 결과를 'result' 변수에 저장
print(result)
# 결과를 콘솔에 출력

notepad_process = Popen('notepad')
# 메모장 실행
time.sleep(1)
# 1초 동안 대기

pyautogui.write(result)
# 결과를 메모장에 입력
