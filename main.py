from turtle import Screen, pos, screensize, Turtle
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake
score = Scoreboard()
screen = Screen()  # screen setup
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkey(snake.up, "Up")  # key bindings
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()

is_game_on = True  # game
while is_game_on:
    score.score_on_screen()
    screen.update()  # no animation for updating snake until this
    time.sleep(0.1)
    snake.move()  # snake movement

    if snake.head.distance(food) < 16:  # collision with food
        snake.extend()
        food.new_food_position()
        score.score += 1

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:  # collision with wall
        score.reset()
        snake.reset()
    for part in snake.all_snake_parts[1:]:
        if snake.head.distance(part) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
