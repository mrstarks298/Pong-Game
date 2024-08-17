from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")  # Set the background color to black
screen.setup(width=800, height=600)  # Set the dimensions of the screen
screen.title("Pong")  # Set the title of the screen
screen.tracer(0)  # Turn off screen updates for smoother animation

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))  # Right paddle at position (350, 0)
l_paddle = Paddle((-350, 0))  # Left paddle at position (-350, 0)
ball = Ball()  # Create the ball
scoreboard = Scoreboard()  # Create the scoreboard

# Keyboard bindings for paddle movement
screen.listen()  # Start listening for keyboard inputs
screen.onkey(r_paddle.go_up, "Up")  # Move the right paddle up with the "Up" key
screen.onkey(r_paddle.go_down, "Down")  # Move the right paddle down with the "Down" key
screen.onkey(l_paddle.go_up, "w")  # Move the left paddle up with the "W" key
screen.onkey(l_paddle.go_down, "s")  # Move the left paddle down with the "S" key

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen to reflect changes
    ball.move()  # Move the ball

    # Detect collision with the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Bounce the ball off the wall

    # Detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()  # Bounce the ball off the paddle

    # Detect if the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()  # Reset the ball to the center
        scoreboard.l_point()  # Award a point to the left paddle

    # Detect if the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()  # Reset the ball to the center
        scoreboard.r_point()  # Award a point to the right paddle

# Exit the game on click
screen.exitonclick()
