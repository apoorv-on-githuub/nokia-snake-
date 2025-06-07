from turtle import Turtle
ALIGNMENT = "center"
FONT_SCORE = ("Arial", 15, "normal")
FONT_GAME_OVER =  ("Arial", 25, "normal")

class Score(Turtle):
    def __init__(self):
        super(). __init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.write_score()
        
        
    def write_score(self):
        self.goto(0,278)
        self.write(f"Score: {self.score}",True,ALIGNMENT,FONT_SCORE)

        
    def update_score(self):
        '''add +1 to the score board'''
        self.clear()
        self.score += 1
        self.write_score()
       
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER",True,ALIGNMENT,FONT_GAME_OVER)