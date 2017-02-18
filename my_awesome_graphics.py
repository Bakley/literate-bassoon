import turtle


def func(what_to_do):
    for i in range(1, 5):
        what_to_do.forward(100)
        what_to_do.left(90)


def graphic_illustrations():
    # create a windows screen
    window = turtle.Screen()
    window.bgcolor("red")
    # create a turtle Tod who draws a square
    tod = turtle.Turtle()
    tod.color('green')
    tod.shape('turtle')
    tod.speed(10000)
    for i in range(1, 37):
        func(tod)
        tod.left(10)
    # create a turtle Angela who draws a circle
    # angela = turtle.Turtle()
    # angela.color("blue")
    # angela.circle(100)
    # create a turtle Brad who draws a Triangle
    # brad = turtle.Turtle()
    # brad.color("blue")
    # brad.shape("classic")

    window.exitonclick()


graphic_illustrations()
