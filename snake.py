
from turtle import Turtle
snakes=[] #empty list for creating ac snake
positions=[(0,0),(-20,0),(-40,0)] #Tuple
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.snakes=[]
        self.snake_position()
        self.head=self.snakes[0]
    def snake_position(self):
        for position in positions:
            self.add_segment(position)


    def add_segment(self,position):
        new_snake=Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    '''to turn off the tracer for the snakes because without using it if we use the 
    game, it will show us three blocks moving rather than a snake. now this will create a blank screen only but we will use another
    function names screen.update for seeing teh snake'''
    def move(self):
        for snake_num in range(len(self.snakes)-1,0,-1):
            new_x=self.snakes[snake_num-1].xcor()
            new_y=self.snakes[snake_num-1].ycor()
            self.snakes[snake_num].goto(new_x,new_y)
        self.snakes[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        '''in this code, in range, first variable is start=which is teh length of the snake. here teh snake is 3 units long so we will take 2(0,1,2). Then is stop which is 0 and step, it is going from 2 to 1 and 1 to 0 HEnce, step will be 0
        In our current code, we have taken it as length of the snake so that when it gets long, we dont get any error.'''
    def reset(self):
        for segment in self.snakes:
            segment.goto(1000, 1000)
        self.snakes.clear()
        self.snake_position()
        self.head = self.snakes[0]


    def extend(self):
        self.add_segment(self.snakes[-1].position())



