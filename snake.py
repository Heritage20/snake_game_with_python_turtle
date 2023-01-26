from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """this class initiates the snake and all the methods to call on the snake """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ CREATE THE SNAKES BODY"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """ ADD SEGMENT TO THE SNAKE"""
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """ ADD A NEW SEGMENT TO THE SNAKE"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ CONTROLS THE MOVEMENT AND COORDINATE OF THE SNAKE AUTOMATICALLY"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # changes the head of the snake
        # self.head.shapesize(0.5, 1)

    def up(self):
        """ TO MOVE THE SNAKE DOWN"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ TO MOVE THE SNAKE UP"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ TO MOVE THE SNAKE RIGHT"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ TO MOVE THE SNAKE LEFT"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


