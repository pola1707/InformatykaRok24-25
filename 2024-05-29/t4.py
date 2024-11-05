import turtle

t = turtle.Turtle()

def fraktal(bok):
    if bok < 5:
        return None
    for i in range(4):
        t.forward(bok)
        t.left(125)
        fraktal(bok/3)

fraktal(200)
turtle.exitonclick()