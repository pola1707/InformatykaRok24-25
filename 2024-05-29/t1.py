import turtle

t = turtle.Turtle()

def spirala(bok):
    if bok < 10:
       return None

    t.forward(bok)
    t.right(90)
    spirala(bok-5)

spirala(200)




turtle.exitonclick()