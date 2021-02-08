from turtle import *

def drawShape(corners, length):
    for i in range(corners):
        forward(length)

        angles = (corners - 2.) * 180.
        angle = angles / corners

        right(180. + angle)

def clear():
    reset()
    hideturtle()


clear()
