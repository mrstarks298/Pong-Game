from turtle import Turtle

# Creating a Paddle class that inherits from the Turtle class
class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()  # Initialize the Turtle superclass
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle to make it wider and thinner
        self.penup()  # Lift the pen to avoid drawing lines when moving
        self.goto(position)  # Move the paddle to the specified position

    # Method to move the paddle up
    def go_up(self):
        new_y = self.ycor() + 20  # Calculate the new y-coordinate (move up by 20 units)
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position

    # Method to move the paddle down
    def go_down(self):
        new_y = self.ycor() - 20  # Calculate the new y-coordinate (move down by 20 units)
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position
