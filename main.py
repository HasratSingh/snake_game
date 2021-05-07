from turtle import Screen
import snake
import time
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()
screen.listen()
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")
screen.onkey(snake.turn_up, "w")
screen.onkey(snake.turn_down, "s")
game = True
while game:
    time.sleep(0.1)
    screen.update()
    snake.move()
    # on collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.swap()
        score.update_score()
    # on collision with boundary
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        score.game_over()
    # on collision with tail
    for s in snake.snake[1:]:
        if snake.head.distance(s) < 15:
            game = False
            score.game_over()
screen.exitonclick()
