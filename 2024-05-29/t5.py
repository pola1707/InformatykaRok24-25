import turtle

t = turtle.Turtle()
t.speed(0)
def fraktal(bok):
    if bok < 3:
        return None
    for i in range(5):
        t.forward(bok)
        t.left(30)
        t.forward(bok)
        t.right(60)
        t.forward(bok)
        fraktal(bok/2)

fraktal(30)

turtle.exitonclick()