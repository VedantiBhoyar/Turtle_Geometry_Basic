from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        timmy.color(c)
        timmy.forward(steps)
        timmy.right(30)




my_screen = Screen()
my_screen.exitonclick()

