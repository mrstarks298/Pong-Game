

<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=28&duration=3000&pause=1000&color=FFFFFF&center=true&vCenter=true&width=580&height=50&lines=Classic+Pong+Game;Paddle+%F0%9F%8F%93+Ball+%F0%9F%8F%90+Score+%F0%9F%8F%86" alt="Typing SVG" />
</h1>

## 📖 Description

This is a classic implementation of the Pong game using Python's Turtle graphics library. Two players control paddles on opposite sides of the screen, trying to hit a ball back and forth. The game keeps track of scores and increases in difficulty as play continues.

## 🎮 Features

- Two-player gameplay
- Increasing ball speed for added challenge
- Score tracking
- Responsive paddle controls

## 🛠 Requirements

- Python 3.x
- Turtle graphics library (comes pre-installed with Python)

## 🚀 Installation

1. Clone this repository or download the source code.
2. Ensure you have Python 3.x installed on your system.
3. No additional installation is required as the game uses the built-in Turtle graphics library.

## 🕹 How to Play

1. Run the `main.py` file:
2. Player 1 (left paddle) uses 'W' and 'S' keys to move up and down.
3. Player 2 (right paddle) uses 'Up' and 'Down' arrow keys to move up and down.
4. The ball will start moving automatically.
5. Try to hit the ball with your paddle to send it to the opponent's side.
6. If a player misses the ball, the opponent scores a point.
7. The game continues indefinitely - compete for the highest score!

## 🗂 Project Structure

- `main.py`: The main game loop and setup
- `paddle.py`: Contains the Paddle class for creating and controlling paddles
- `ball.py`: Contains the Ball class for creating and controlling the ball movement
- `scoreboard.py`: Contains the Scoreboard class for keeping and displaying scores

## 🛠 Customization

You can customize various aspects of the game by modifying constants in the respective files:

- Change the game window size in `main.py`
- Adjust ball speed by modifying the `move_speed` in `ball.py`
- Change paddle size by adjusting `stretch_wid` and `stretch_len` in `paddle.py`
- Modify scoreboard position and font in `scoreboard.py`

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
