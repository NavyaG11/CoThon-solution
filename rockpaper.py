import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    computer_choice_var.set(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_var.set(result)

# Set up the GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x300")

# Variables to display choices and result
computer_choice_var = tk.StringVar()
result_var = tk.StringVar()

# GUI elements
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

choices_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 12))
choices_label.pack(pady=10)

# Buttons for user choices
button_rock = tk.Button(root, text="Rock", command=lambda: determine_winner("Rock"), font=("Helvetica", 12))
button_rock.pack(pady=5)

button_paper = tk.Button(root, text="Paper", command=lambda: determine_winner("Paper"), font=("Helvetica", 12))
button_paper.pack(pady=5)

button_scissors = tk.Button(root, text="Scissors", command=lambda: determine_winner("Scissors"), font=("Helvetica", 12))
button_scissors.pack(pady=5)

# Display computer's choice
computer_choice_label = tk.Label(root, textvariable=computer_choice_var, font=("Helvetica", 12))
computer_choice_label.pack(pady=10)

# Display the result of the game
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

# Play again button
play_again_button = tk.Button(root, text="Play Again", command=lambda: [computer_choice_var.set(""), result_var.set("")], font=("Helvetica", 12), bg="blue", fg="white")
play_again_button.pack(pady=10)

# Run the GUI
root.mainloop()
