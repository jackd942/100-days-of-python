from turtle import Turtle, Screen


def draw_square():
    kurt = Turtle()
    kurt.shape("turtle")
    kurt.color("red")
    kurt.forward(50)
    kurt.right(90)
    kurt.forward(100)
    kurt.right(90)
    kurt.forward(100)
    kurt.right(90)
    kurt.forward(100)
    kurt.right(90)
    kurt.forward(50)


if __name__ == '__main__':

    draw_square()

    screen = Screen()
    screen.exitonclick()
