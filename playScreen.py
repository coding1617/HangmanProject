from tkinter import *
import turtle
class Play_screen(Frame):

    def __init__(self, master, choice):
        """Initialize Frame."""
        self.choice = choice
        super(Play_screen, self).__init__(master)
        master.title("Play Screen!")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        column = 0
        column2 = 0

        for letter in alphabet:
            if column <= 25:
                self.letter = Button(self, text=letter, fg="white", bg="navy",
                                    command=self.letter_click
                                    ).grid(row=20, column=column, sticky=N)

                Label(self, text=""
                    ).grid(row=20, column=column + 1, sticky=N)
                column += 2
            else:
                self.letter = Button(self, text=letter, fg="white", bg="navy",
                                     command=self.letter_click
                                     ).grid(row=22, column=column2, sticky=N)

                Label(self, text=""
                      ).grid(row=22, column=column2 + 1, sticky=N)

                column2 += 2
        Label(self, text=""
              ).grid(row=21, sticky=N)

# Is there now way to make a function called def letters(self): and have it work on each button as specified.
# Maybe name the buttons like self.a, self.b, etc.?
# Cause this is REALLY long


    def letter_click(self):
        pass
