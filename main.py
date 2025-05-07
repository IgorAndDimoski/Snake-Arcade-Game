import turtle
from food import Food
from turtle import Turtle, Screen
import time
from snake import Snake
from score_board import ScoreBoard
screen = Screen()
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.setup(600,600)
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        game_on = False

screen.exitonclick()