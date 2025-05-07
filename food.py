import random
from turtle import Turtle
from snake import Snake
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.refresh()


    def refresh(self):
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.goto(random.randint(-230, 230), random.randint(-230, 230))



