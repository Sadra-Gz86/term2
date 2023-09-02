from turtle import *
def colored_square(p: Pen, length, c):
    p.fillcolor(c)
    square(p, length)
def square(p:Pen, length):
    p.begin_fill()
    for i in range(4):
        p.fd(length)
        p.lt(90)
    p.end_fill()
def teleport(p:Pen, x, y):
    p.up()
    p.goto(x, y)
    p.down()
p=Pen()
for i in range(5):
    length = int(textinput("Length", "Enter length of square: "))
    p.fd(0)
    x = int(textinput("X", "Enter x position: "))
    p.fd(0)
    y = int(textinput("Y", "Enter y position: "))
    p.fd(0)
    c = textinput("C", "Enter Color of square: ")
    teleport(p, x, y)
    colored_square(p, length, c)
done()