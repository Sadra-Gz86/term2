import turtle
my_colors = 'purple', 'cyan', 'blue', 'green', 'yellow', 'orange', 'red'
i2 = 0
t=turtle.Pen()
t.speed(0)
for k in range(200, 0, -2):
    t.penup()
    t.goto(-k, -k)
    t.pendown()
    t.color(my_colors[i2])
    i2 = i2+1
    i2 = i2%7
    for i in range(4):
        t.fd(k*2)
        t.lt(90)


turtle.done()