from tkinter import *
from tkinter import messagebox
import os
import sys
import Words as words


root = Tk()
x = words.choose_word()
MaxGuess = 6

BLACK = "#000000"
GREEN = "#6ca965"
YELLOW = "#c8b653"
GRAY = "#FFFFFF"

root.config(bg=BLACK)

num = 1

WI = Entry(root)
WI.grid(row=999, column=0, padx=10, pady=10, columnspan=3)



def Guess():
    global x
    guess = WI.get()

    global num
    num += 1

    if num <= MaxGuess:

        if len(guess) == 5:

            if x == guess:
                messagebox.showinfo("C", f"Correct! The word was {x.title()}")
            else:
                for i, letter in enumerate(guess):

                    label = Label(root, text=letter.upper())
                    label.grid(row=num, column=i, padx=10, pady=10)

                    if letter == x[i]:
                        label.config(bg=GREEN, fg=BLACK)

                    if letter in x and not letter == x[i]:
                        label.config(bg=YELLOW, fg=BLACK)

                    if letter not in x:
                        label.config(bg=BLACK, fg=GRAY)

        else:
            messagebox.showerror("5 chars", "The word must be 5 characters exactly")

    else:
        for i, letter in enumerate(guess):

            label = Label(root, text=letter.upper())
            label.grid(row=num, column=i, padx=10, pady=10)

            if letter == x[i]:
                label.config(bg=GREEN, fg=BLACK)

            if letter in x and not letter == x[i]:
                label.config(bg=YELLOW, fg=BLACK)

            if letter not in x:
                label.config(bg=BLACK, fg=GRAY)
        messagebox.showerror("F", f"Wrong! The correct word was {x}")

        if messagebox.askyesno("N", f"New Game?") == FALSE:
            quit()
        else:
                root.destroy()
                os.startfile("Frontend.pyw")


GuessButton = Button(root, text="Guess", command=Guess)
GuessButton.grid(row=999, column=3, columnspan=2)

root.mainloop()