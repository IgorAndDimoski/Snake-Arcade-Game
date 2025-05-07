from turtle import Turtle, Screen
ALIGEMENT = "center"
FONT = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 250)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGEMENT, font=FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", move=False, align=ALIGEMENT, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGEMENT, font=('Courier', 60, 'normal'))

