# Slot Machine Game
A simple slot machine game written in Python.

## Features
- Play a game of slots with a virtual balance
- Auto spin feature to play multiple rounds quickly
- Save and load balance to continue playing later
- Simple text-based interface

## Requirements
- Python 3.x

## How to Play
1. Run the game by executing `main.py`
2. Choose to play or exit the game
3. If playing, you can choose to spin the slot machine, enable auto spin, change your bet, or exit the game
4. The game will display your balance and the result of each spin

## Notes
- The game saves your balance to a file named `balance.json` in a directory named `SaveData`
- If the save file does not exist, the game will create it with a default balance of $100
- The game will automatically save your balance when you exit
