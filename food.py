from turtle import Turtle
import random


class Food(Turtle):
    """defines the food by inheriting from the Turtle class"""

    def __init__(self):
        """defines the Food class which inherits from the Turtle class to create a food for the snake"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """update the food to a random location once eaten by the snake"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)