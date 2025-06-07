from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food = Turtle(shape="circle")
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.create_new_food()

    def create_new_food(self):
        """create new food for snake"""
        self.food.color("blue")
        self.food.penup()
        x_cor = random.randint(-275, +275)
        y_cor = random.randint(-275, +275)
        self.food.goto(x_cor, y_cor)
