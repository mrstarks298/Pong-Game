from turtle import Turtle

# Creating a Ball class that inherits from the Turtle class
class Ball(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.color("white")  # Set the color of the ball to white
        self.shape("circle")  # Set the shape of the ball to a circle
        self.penup()  # Lift the pen to avoid drawing lines when moving
        self.x_move = 3  # Set the ball's horizontal movement speed
        self.y_move = 3  # Set the ball's vertical movement speed
        self.move_speed = 0.1  # Set the initial speed of the ball

    # Method to move the ball
    def move(self):
        new_x = self.xcor() + self.x_move  # Calculate the new x-coordinate
        new_y = self.ycor() + self.y_move  # Calculate the new y-coordinate
        self.goto(new_x, new_y)  # Move the ball to the new position

    # Method to bounce the ball off the top or bottom walls
    def bounce_y(self):
        self.y_move *= -1  # Reverse the direction of vertical movement

    # Method to bounce the ball off the paddles
    def bounce_x(self):
        self.x_move *= -1  # Reverse the direction of horizontal movement
        self.move_speed *= 0.9  # Increase the ball's speed slightly

    # Method to reset the ball to the center of the screen
    def reset_position(self):
        self.goto(0, 0)  # Move the ball to the center
        self.move_speed = 0.1  # Reset the ball's speed to the initial value
        self.bounce_x()  # Reverse the direction of horizontal movement to continue the game
