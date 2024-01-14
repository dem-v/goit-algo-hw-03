# https://python-with-science.readthedocs.io/en/latest/koch_fractal/koch_fractal.html
# Draw a Koch snowflake
from turtle import *
from time import sleep
from sys import argv

size = 500
order = 3


def init():
    # Choose colours and size
    color("sky blue", "white")
    bgcolor("black")
    pensize(2)

    # Ensure snowflake is centred
    penup()
    backward(size / 1.732)
    left(30)
    pendown()


def koch(a, d):
    if d > 0:
        for t in [60, -120, 60, 0]:
            koch(a / 3, d - 1)
            left(t)
    else:
        forward(a)


def draw_it(n=-1):
    n = n if n >= 0 else order
    # Make it fast
    tracer(10 ** min(n, 5))
    hideturtle()

    begin_fill()

    # Three Koch curves
    for i in range(3):
        koch(size, n)
        right(120)

    end_fill()

    # Make the last parts appear
    update()


if __name__ == "__main__":
    if len(argv) > 1:
        n = int(argv[1])
    else:
        n = -1

    init()
    draw_it(n)
    sleep(2)
