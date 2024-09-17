# Guess-the-number-SkillCraft-Technology
Build a program that generates a random number and challenges the user to guess it. The program should  prompt the user to input their guess, compare it to the generated number 
**Number Guessing Game with GUI and Special Effects**

This is a simple number guessing game implemented in Python using the tkinter library. The game generates a random number between 1 and 100, and the user is challenged to guess the number. The game provides feedback in the form of color changes and sound effects to enhance the user experience.

Features
Random Number Generation: The game randomly selects a number between 1 and 100 at the start.
User Input: The player inputs their guesses through a GUI.

Color Feedback:
Blue text for guesses that are too low.
Red text for guesses that are too high.
Green text and a congratulatory message for the correct guess.
Flash Effects: The background color flashes with blue, red, or green, depending on the user's guess.
Sound Effects: Beep sound effects play on each guess (supported on some platforms).

Requirements:
Python 3.x
tkinter (included with most Python installations)
winsound (for sound effects on Windows)
On non-Windows systems (like Linux or macOS), sound effects may require the play command-line utility (optional).
