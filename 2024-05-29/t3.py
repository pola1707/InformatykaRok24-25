import turtle


t = turtle.Turtle()

def slaczek(bok):
    if bok < 5:
        return None
    t.left(90)
    t.forward(bok)
    t.right(90)
    t.forward(bok)
    t.right(90)
    t.forward(bok)
    t.left(90)
    t.forward(bok)
    slaczek(bok/2)

slaczek(50)

turtle.exitonclick()