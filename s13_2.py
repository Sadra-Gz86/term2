from turtle import *
from random import randint
def teleport(x, y):
    up()
    goto(x, y)
    down()
def star(color1, color2, size, number, sp, d):
    speed(sp)
    pencolor(color1)
    fillcolor(color2)
    for j in range(number):
        teleport(randint(-300, 300), randint(-200, 200))
        begin_fill()
        for i in range(5):
            fd(size)
            rt(144)
        if d=='y':
            end_fill()
        up()
        fd(size/2)
        rt(90)
        fd(size/2)
        down()
        write('🗿', font=('', 60))
        up()
        bk(size/2)
        lt(90)
        bk(size/2)
        down()
# write("✊", font=('', 60))

c1=textinput("line color", "Enter color1:")
d = textinput("inner line", "Do you want to use fillcolor?(y/n)")
if d=='y':
    c2=textinput("inner color", "Enter color2:")
else:
    c2 = 'black'
s=int(textinput("size", "Enter size:"))
n=int(textinput("number", "Enter number:"))
sp=int(textinput("speed", "Enter speed:"))
star(color1=c1, color2=c2, size=s, number=n, sp=sp, d=d)
done()