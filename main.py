from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
snake1=Snake()
food=Food()

scoreboard=Scoreboard()
#setting up teh screen size for the game
screen.setup(width=600, height=600)
#colour of teh screen or teh background colour


screen.tracer(0)
#keys for control
screen.listen()
screen.onkey(snake1.up,"Up")
screen.onkey(snake1.down,"Down")
screen.onkey(snake1.left,"Left")
screen.onkey(snake1.right,"Right")

#for title of teh game
screen.title("Feed the snake")
snake1.snake_position()

    
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()

#Detect collision with food
    if snake1.head.distance(food)<15:
        food.refresh()
        snake1.extend()
        scoreboard.increase_score()


# detect collision with wall
    if snake1.head.xcor()>280 or snake1.head.xcor()<-280 or snake1.head.ycor()>280 or snake1.head.ycor()<-280:
        scoreboard.reset_game()
        snake1.reset()

#detect collision with tail
    for segment in snake1.snakes[1:]:
        if snake1.head.distance(segment)<10:
            scoreboard.reset_game()
            snake1.reset()


screen.exitonclick()

