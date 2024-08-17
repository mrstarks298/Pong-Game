from turtle import Turtle

# Creating a Scoreboard class that inherits from the Turtle class
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.color("white")  # Set the text color to white
        self.penup()  # Lift the pen to prevent drawing lines when moving
        self.hideturtle()  # Hide the turtle cursor
        self.l_score = 0  # Initialize the left side score
        self.r_score = 0  # Initialize the right side score
        self.update_scoreboard()  # Display the initial scoreboard

    # Method to update the scoreboard display
    def update_scoreboard(self):
        self.clear()  # Clear the previous scoreboard display
        self.goto(-100, 200)  # Position the turtle for the left score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))  # Display the left score
        self.goto(100, 200)  # Position the turtle for the right score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))  # Display the right score

    # Method to increase the left side score and update the display
    def l_point(self):
        self.l_score += 1  # Increment the left score
        self.update_scoreboard()  # Update the scoreboard display

    # Method to increase the right side score and update the display
    def r_point(self):
        self.r_score += 1  # Increment the right score
        self.update_scoreboard()  # Update the scoreboard display
