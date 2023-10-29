```python
import turtle as t
import random

# 터틀 초기 설정
t.speed(1)
t.bgcolor("black")
t.hideturtle()
t.color("white")

# 반짝이는 별 그리기 함수
def draw_star(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(random.randint(1, 3), "white")

# 카시오페이아 별자리 그리기 함수
def draw_cassiopeia():
    # 카시오페이아 좌표
    w_coords = [(-60, 0), (-30, 30), (-15, 60), (0, 0), (15, 60), (30, 30), (60, 0)]

    # 별자리 점 그리기
    for x, y in w_coords:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(5)  # 작은 점으로 별자리 점 그리기

    # 별자리 선 그리기
    for i in range(len(w_coords) - 1):
        x1, y1 = w_coords[i]
        x2, y2 = w_coords[i + 1]
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

# 배경에 반짝이는 별 추가하기
for _ in range(100):
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    draw_star(x, y)

# 카시오페아  그리기 함수 호출 (크게 그리기)
t.penup()
t.goto(0, -50)
t.pendown()
draw_cassiopeia()

# 작업 완료 후 창 유지
t.done()
```

결과 화면  

<img width="531" alt="image" src="https://github.com/ces0o/Python/assets/127365253/a416cb93-3c7e-466b-a315-10c9aa225922">  

<카시오페이아 별자리>

