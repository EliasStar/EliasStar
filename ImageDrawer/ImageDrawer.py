from turtle import *
from PIL import Image

print("I can draw:\n")

print("bucket")
print("female")
print("male")
print("youtube")

name = input("\nWhat Image should I draw?" + "\n" + "|>")

scale = 20.

reset()
hideturtle()
shape("square")
resizemode("user")
shapesize(scale / 20, scale / 20, 0)
speed(0)
penup()

img = Image.open("imgs/" + name + ".png")
xAxis, yAxis = img.size
pixels = img.load()

for y in range(yAxis):
    for x in range(xAxis):
        r, g, b, a = pixels[x, y]
        if a != 0:
            _, red = hex(r).split("x")
            _, blue = hex(b).split("x")
            _, green = hex(g).split("x")

            if len(red) == 1:
                red = "0" + red

            if len(blue) == 1:
                blue = "0" + blue

            if len(green) == 1:
                green = "0" + green

            hexCode = "#" + red + green + blue

            color(hexCode)
            setposition((x * (scale - 1)) - (xAxis/2) * scale, (-y * (scale - 1)) + (yAxis/2) * scale)
            stamp()
