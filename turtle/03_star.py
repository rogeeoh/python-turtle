import turtle as t
import time

FORWARD = 80
EDGE = 140

# t.shape("turtle")
t.color("blue")

for i in range(0, 5):
    t.left(70)
    t.forward(FORWARD)
    t.right(EDGE)
    t.forward(FORWARD)

time.sleep(1000)