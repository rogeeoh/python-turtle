import turtle as t


def turn_right():
    t.setheading(0)
    t.forward(10)


def turn_left():
    t.setheading(180)
    t.forward(10)


t.shape('turtle')
t.speed(0)

# 오른쪽 키보드 버튼을 눌렀을 때 turn_right 함수를 실행
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")

t.listen()
t.mainloop()
