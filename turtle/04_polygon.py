import turtle as t
import time

n = input("몇 각형을 그리겠습니까? : ")
n = int(n)

t.color("purple")
t.begin_fill()

for i in range(n):
    t.forward(50)
    t.left(360 / n)

t.end_fill()

time.sleep(1000)