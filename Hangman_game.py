import tkinter as tk
import random

# ================== GAME SETUP ==================
words = ["python", "developer", "hangman", "keyboard", "laptop", "college"]
random.shuffle(words)

word_index = 0
chosen_word = words[word_index]
guessed_letters = []
wrong_guesses = 0
max_wrong = 6
score = 0

# ================== HANGMAN STAGES ==================
hangman_stages = [
"""
  -----
  |   |
      |
      |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
      |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
  |   |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\\  |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
---------
"""
]

# ================== WINDOW ==================
root = tk.Tk()
root.title("Hangman Game SoftGrow internship program")
root.geometry("850x750")
root.configure(bg="#1e1e2f")

# ================== FUNCTIONS ==================

def update_display():
    display_word = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    word_label.config(text=display_word)
    hangman_label.config(text=hangman_stages[wrong_guesses])

    # WIN
    if "_" not in display_word:
        result_label.config(text="🎉 Correct! Next Word...", fg="#00ff99")
        update_score(10)
        entry.config(state="disabled")
        root.after(2000, next_word)

    # LOSE
    if wrong_guesses >= max_wrong:
        result_label.config(text=f"😢 Wrong! Word was: {chosen_word}", fg="red")
        update_score(-5)
        entry.config(state="disabled")
        root.after(2000, next_word)


def guess_letter():
    global wrong_guesses

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if guess and guess not in guessed_letters:
        guessed_letters.append(guess)

        if guess not in chosen_word:
            wrong_guesses += 1

        update_display()


def update_score(points):
    global score
    score += points
    score_label.config(text=f"Score: {score}")


def next_word():
    global word_index, chosen_word, guessed_letters, wrong_guesses

    word_index += 1

    if word_index >= len(words):
        result_label.config(text="🏆 Game Finished!", fg="#00ff99")
        entry.config(state="disabled")
        return

    chosen_word = words[word_index]
    guessed_letters = []
    wrong_guesses = 0

    result_label.config(text="")
    entry.config(state="normal")
    update_display()


def restart_game():
    global words, word_index, chosen_word, guessed_letters, wrong_guesses, score

    random.shuffle(words)
    word_index = 0
    chosen_word = words[word_index]
    guessed_letters = []
    wrong_guesses = 0
    score = 0

    score_label.config(text="Score: 0")
    result_label.config(text="")
    entry.config(state="normal")
    update_display()


# ================== UI ==================

title_label = tk.Label(root, text="HANGMAN Game SoftGrow internship program",
                       font=("Arial", 26, "bold"),
                       bg="#1e1e2f", fg="#00bfff")
title_label.pack(pady=15)

hangman_label = tk.Label(root, text=hangman_stages[0],
                         font=("Courier", 14),
                         bg="#2a2a40", fg="white",
                         width=25, height=8)
hangman_label.pack(pady=10)

word_label = tk.Label(root, text="",
                      font=("Arial", 30, "bold"),
                      bg="#1e1e2f", fg="white")
word_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 18), justify="center")
entry.pack(pady=5)

guess_btn = tk.Button(root, text="Guess",
                      font=("Arial", 14, "bold"),
                      bg="#00bfff", fg="black",
                      width=10,
                      command=guess_letter)
guess_btn.pack(pady=5)

result_label = tk.Label(root, text="",
                        font=("Arial", 14, "bold"),
                        bg="#1e1e2f")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: 0",
                       font=("Arial", 18, "bold"),
                       bg="#1e1e2f", fg="#ffd700")
score_label.pack(pady=10)

restart_btn = tk.Button(root, text="Restart Game",
                        font=("Arial", 12, "bold"),
                        bg="#ff4d4d", fg="white",
                        command=restart_game)
restart_btn.pack(pady=15)

update_display()
root.mainloop()