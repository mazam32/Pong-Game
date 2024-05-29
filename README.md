# Pong-Game

Welcome to the Pong Game! This is a classic arcade game implemented in Python using the Turtle graphics package. In this game, two players control paddles and try to hit a ball back and forth across the screen. The objective is to score points by making the ball pass the opponent's paddle.

## Features

- Two-player mode: Each player controls a paddle using keyboard inputs.
- Realistic ball movement and collision detection.
- Score tracking for both players.
- Simple and intuitive graphics using the Turtle package.

## Installation

To run this game, you need to have Python installed on your system. Additionally, you need the Turtle package, which is included in the standard Python library.

## How to Play

1. Clone or download the repository to your local machine.
2. Open a terminal and navigate to the directory containing the game files.
3. Run the game by executing the following command:

   ```bash
   python pong_game.py
   ```

### Controls

- **Player 1 (Left Paddle)**
  - Move Up: `W` key
  - Move Down: `S` key

- **Player 2 (Right Paddle)**
  - Move Up: `Up Arrow` key
  - Move Down: `Down Arrow` key

### Objective

- The objective of the game is to score points by hitting the ball past the opponent's paddle.
- The first player to reach a predetermined score wins the game.

## Code Overview

The game consists of several main components:

- `pong_game.py`: The main script that initializes the game and runs the game loop.
- `paddle.py`: Contains the Paddle class, responsible for creating and controlling the paddles.
- `ball.py`: Contains the Ball class, responsible for creating the ball and handling its movement and collision detection.
- `scoreboard.py`: Contains the Scoreboard class, responsible for displaying and updating the score.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This game was created using the Turtle graphics package, a standard Python library for creating graphics.
- Inspired by the original Pong game developed by Atari.

Enjoy playing the Pong Game! Feel free to report any issues or suggest enhancements.