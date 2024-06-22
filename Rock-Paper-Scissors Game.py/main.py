import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    user_choice = user_var.get()
    computer_choice = get_computer_choice()
    result = get_winner(user_choice, computer_choice)
    result_text.set(f"You chose {user_choice}, computer chose {computer_choice}. " + {
        "tie": "It's a tie!",
        "user": "You win!",
        "computer": "You lose!"
    }[result])

def play_again():
    play_again_var = tk.StringVar(root, "yes")
    tk.Label(root, text="Do you want to play again?").pack()
    tk.Radiobutton(root, text="Yes", variable=play_again_var, value="yes").pack()
    tk.Radiobutton(root, text="No", variable=play_again_var, value="no").pack()
    if play_again_var.get() == "yes":
        user_var.set("")
        result_text.set("")
        play_button.config(state="normal")
    else:
        root.quit()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("500x500")
root.configure(background="black")  # Set the background color to black

user_var = tk.StringVar(root, "rock")

tk.Label(root, text="Choose your weapon:", font=("Arial", 18), bg="black", fg="white").pack()
tk.Radiobutton(root, text="Rock", variable=user_var, value="rock", font=("Arial", 14), bg="black", fg="white").pack()
tk.Radiobutton(root, text="Paper", variable=user_var, value="paper", font=("Arial", 14), bg="black", fg="white").pack()
tk.Radiobutton(root, text="Scissors", variable=user_var, value="scissors", font=("Arial", 14), bg="black", fg="white").pack()

play_button = tk.Button(root, text="Play", command=play_game, font=("Arial", 18), bg="green", fg="white")
play_button.pack(pady=20)

result_text = tk.StringVar(root, "")

tk.Label(root, textvariable=result_text, font=("Arial", 20), bg="black", fg="white").pack(pady=20)

play_again_button = tk.Button(root, text="Play Again", command=play_again, font=("Arial", 18), bg="green", fg="white")
play_again_button.pack(pady=20)

root.mainloop()