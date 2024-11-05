import turtle

t = turtle.Turtle()
t.speed(0)
def trojkat(bok):
    if bok < 5:
        return None
    for i in range(3):
        t.forward(bok)
        t.left(120)
        trojkat(bok/2)

trojkat(200)
turtle.exitonclick()