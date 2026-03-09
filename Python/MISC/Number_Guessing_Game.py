import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.config(bg="#f0f8ff")


        #Initialize game
        self.secret_number = random.randint(1, 50)
        self.attempts = 0


        #Title Label
        self.title_label = tk.Label(
            root,
            text ="Guess the Number between 1 and 100",
            font=("Arial", 14, "bold"),
            bg="#f0f8ff"
        )
        self.title_label.pack(pady=20)


        # Entry for guesses
        self.guess_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.guess_entry.pack(pady=100)

        # Guess Button
        self.guess_button = tk.Button(
            root,
            text="Guess",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=self.check_guess
        )
        self.guess_button.pack(pady=10)

        # Feedbakc Label
        self.feedback_label = tk.Label(
            root,
            text="",
            font=("Arial", 14),
            bg="#f0f8ff",
        )

        self.feedback_label.pack(pady=10)

        # Attempts Label
        self.attempts_label = tk.Label(
            root,
            text="Attempts: 0",
            font=("Arial", 12),
            bg="#f0f8ff"
        )
        self.attempts_label.pack(pady=10)

        # Restart Button
        self.restart_button = tk.Button(
            root,
            text="Restart Game",
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            command=self.restart_game
        )
        self.restart_button.pack(pady=10)


    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")

            if guess < self.secret_number:
                self.feedback_label.config(text="Too Low!", fg="blue")
            elif guess > self.secret_number:
                self.feedback_label.config(text="Too High!", fg="red")
            else:
                messagebox.showinfo(
                    "Correct!",
                    f"You guessed {guess}.\nand the number was {self.secret_number}.\nThe number of Attempts was {self.attempts}"
                )
                self.restart_game()

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number")


    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()






