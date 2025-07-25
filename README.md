### Bulls and Cows – Bot Simulation Game

We implemented the classic **Cows and Bulls** game using a positive four-digit integer.

The game is simulated by **two bots** that take turns guessing each other's numbers, receiving feedback in terms of "bulls" (correct digit in correct place) and "cows" (correct digit in wrong place), until one of them wins.

### How It Works
- Each bot generates a unique 4-digit number (no repeated digits).
- The bots alternate turns, making guesses and receiving feedback.
- The simulation continues until one bot correctly guesses the other's number.

### Technologies Used
- Python 3
- Standard libraries only (no external dependencies)

### Run the Project
To run the game locally, simply execute the main script:
```bash
python bulls_and_cows.py
