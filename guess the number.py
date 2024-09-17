import tkinter as tk
import random
import time
from tkinter import messagebox

try:
    import winsound  # For Windows sound effects
except ImportError:
    import os
    def winsound_beep(freq, dur):
        os.system(f'play -nq -t alsa synth {dur / 1000} sine {freq}')
    winsound.Beep = winsound_beep

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game with Effects")
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        
        # GUI Layout
        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        self.attempts += 1

        if guess < self.number_to_guess:
            self.flash_feedback("Too low!", "blue")
        elif guess > self.number_to_guess:
            self.flash_feedback("Too high!", "red")
        else:
            self.flash_feedback("Correct!", "green")
            messagebox.showinfo("Congratulations!", f"You guessed the number {self.number_to_guess} in {self.attempts} attempts!")
            self.play_sound(440)  # Play a winning sound
            self.reset_game()

    def flash_feedback(self, message, color):
        #Show feedback with a color flash effect
        self.result_label.config(text=message, fg=color)
        self.root.update()  # Ensure UI updates immediately
        self.play_sound(300 if color == "red" else 200)  # Play sound effect based on wrong or right guess
        
        # Flash the background color for effect
        self.root.config(bg=color)
        self.root.after(200, lambda: self.root.config(bg="white"))

    def play_sound(self, frequency):
            #Play a beep sound with the given frequency (optional, depends on OS)
        try:
            winsound.Beep(frequency, 150)  # Duration set to 150ms
        except:
            print("Sound effect not supported on this platform.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

# Create the GUI window
root = tk.Tk()
game = GuessingGame(root)

# Run the application
root.mainloop()
