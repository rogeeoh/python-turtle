import turtle as t

# 오른쪽으로 90도 회전하는 함수
def turn_right():
    t.right(90)


t.shape('turtle')

# 특정 시간에 지정한 작업을 한 번만 수행
# 1초 == 1000밀리세컨
t.ontimer(turn_right, 1000 * 10)

t.mainloop()
