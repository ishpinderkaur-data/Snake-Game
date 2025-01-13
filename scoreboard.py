import turtle
from turtle import Turtle
Alignment="center"
Font=('Arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score=0
        self.highscore=self.read_from_file()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score= {self.score} High Score={self.highscore}", align=Alignment, font=Font)

    '''def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write( "GAME OVER", align="center", font=Font)'''

    def reset_game (self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_scoreboard()
        with open("file.txt",mode="w") as file:
            file.write(f"{self.highscore}")


    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def read_from_file(self):
        with open("file.txt","r") as file:
            return int(file.read())


