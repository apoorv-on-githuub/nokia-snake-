from turtle import Screen
import time
from class_snake import Snake
from class_food import Food
from class_score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

food = Food()
score_board = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    snake.snake_touches_boundary()
    if snake.sanke_touches_itself() is True:
        score_board.game_over()
        game_is_on = False
    if snake.snake_head.distance(food.food) < 18: 
        
        food.create_new_food()
        score_board.update_score()
        snake.extend_snake()

screen.exitonclick()
