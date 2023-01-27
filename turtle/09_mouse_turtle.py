import turtle as t

t.shape('turtle')
t.speed(0)
t.pensize(2)    # 펜 굵기
# t.hideturtle()  # 거북이 숨기기

# 화면을 클릭했을 때 무엇을 할 것인지?
t.onscreenclick(t.goto)

t.mainloop()