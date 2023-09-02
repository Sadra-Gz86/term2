import turtle

t = turtle.Pen()
my_colors = 'red', 'blue', 'green', 'cyan', 'orange', 'purple'
t.speed(0)
t.fd(100)
for j in range(6):
    t.up()
    t.fd(150)
    t.down()
    t.color(my_colors[j])
    # t.pencolor(my_colors[j])
    # t.fillcolor(my_colors[j])
    t.dot(60)
    t.up()
    t.bk(150)
    t.lt(60)

turtle.done()