from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
screen.setup(500, 500)
tim.write("HELLO", move=False, align='left', font=('Arial', 20, 'normal'))



screen.exitonclick()