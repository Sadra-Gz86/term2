import turtle

t = turtle.Pen()
a=1
while a!=0:
    a=int(turtle.textinput("?", "Enter a: "))
    for i in range(4):
        t.fd(a)
        t.lt(90)

turtle.done()

