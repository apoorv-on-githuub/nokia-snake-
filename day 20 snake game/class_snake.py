from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        xcor = 0
        for i in range(3):

            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(xcor, 0)
            xcor -= 20
            self.segments.append(new_segment)

    def extend_snake(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        xcor = self.segments[-1].xcor()
        ycor = self.segments[-1].ycor()
        new_segment.goto(xcor, ycor)
        self.segments.append(new_segment)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_snake(self):
        for segment in range(len(self.segments) - 1, 0, -1):

            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.snake_head.forward(20)

    def snake_touches_boundary(self):
        xcor = self.snake_head.xcor()
        ycor = self.snake_head.ycor()
        if self.snake_head.xcor() > 275:
            self.snake_head.goto(-280, ycor)
        elif self.snake_head.xcor() < -280:
            self.snake_head.goto(280, ycor)

        elif self.snake_head.ycor() > 275:
            self.snake_head.goto(xcor, -280)
        elif self.snake_head.ycor() < -280:
            self.snake_head.goto(xcor, 280)

    def sanke_touches_itself(self):
        for snake_segment in self.segments[1:]:
            if self.snake_head.distance(snake_segment) < 15:
                return True
