from turtle import Turtle
MOVE = 20


class Snake:
    length = 3
    snake = []

    def __init__(self):
        for i in range(0, self.length):
            x = -i*20
            pos = (x, 0)
            self.create_snake(pos)
        self.head = self.snake[0]

    def create_snake(self, position):
        square = Turtle("square")
        square.pu()
        square.color("white")
        square.goto(position)
        self.snake.append(square)

    def reset_snake(self):
        # Deletes previous snake
        for snake_obj in self.snake:
            snake_obj.hideturtle()
        self.snake.clear()
        # Creates new snake
        for i in range(0, self.length):
            x = -i * 20
            pos = (x, 0)
            self.create_snake(pos)
        self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.fd(MOVE)

    def extend(self):
        self.create_snake(self.snake[-1].position())

    def turn_left(self):
        self.head.heading() == 0 or self.head.setheading(180)

    def turn_right(self):
        self.head.heading() == 180 or self.head.setheading(0)

    def turn_up(self):
        self.head.heading() == 270 or self.head.setheading(90)

    def turn_down(self):
        self.head.heading() == 90 or self.head.setheading(270)

