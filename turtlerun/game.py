import random
import turtle as t

# 악당 거북이
bad_turtle = t.Turtle()
bad_turtle.shape("turtle")
bad_turtle.color("red")
bad_turtle.speed(0)
bad_turtle.up()
bad_turtle.goto(0, 200)

# 먹이 (초록색 동그라미)
food = t.Turtle()
food.shape("circle")
food.color("green")
food.speed(0)
food.up()
food.goto(0, -200)


def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)


# 플레이어가 움직일 거북이를 만든다!
t.setup(500, 500)
t.bgcolor("orange") # 게임 백그라운드 색
t.shape("turtle")
t.speed(0)
t.up()
t.color("white") # 거북이색

# 오른쪽 버튼을 누르면 turn_right 함수 실행
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()


def play():
    t.forward(20)

    ang = bad_turtle.towards(t.pos()) # 악당거북이가 플레이어를 보기 위한 각도
    bad_turtle.setheading(ang) # 악당거북이의 방향을 전환!
    bad_turtle.forward(9)

    # 게임 시작!
    if t.distance(food) < 12: # 음식이 12보다 가까운 거리에 있으면
        star_x = random.randint(-230, 230) # 랜덤 x좌표 생성
        star_y = random.randint(-230, 230) # 랜덤 y좌표 생성
        food.goto(star_x, star_y) # 랜덤 좌표로 이동

    # 게임오버
    if t.distance(bad_turtle) >= 12:
        t.ontimer(play, 100)


play()

# 항상 실행
print("게임을 시작하지")
t.mainloop()
