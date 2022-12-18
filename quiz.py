# New version of the demerit points quiz
# Uses button instead of keyboard input
import time
import support
import tkinter as tk
from tkinter import ttk, messagebox
import random


class QuizWindow(ttk.Frame):
    def __init__(self, master):
        """
        This class creates a window for the demerit point quiz program. It can't be used to create a program with both
        demerit points and other problems sets.
        :param master: Root ttk.Frame object
        """
        super().__init__(master)
        # Offences
        self.constant_list_offences = support.get_offences_info()
        self.list_offences = self.constant_list_offences[:]

        # Problem
        self.current_problem = None
        self.text_variable_problem = tk.StringVar()

        # Points
        self.score = 0
        self.total = 0

        # Output
        self.label_problem = ttk.Label(self, textvariable=self.text_variable_problem)
        self.buttons = [self.create_button(i) for i in range(2, 8)]

        # Score
        self.text_variable_score = tk.StringVar()
        self.label_score = ttk.Label(self, textvariable=self.text_variable_score)

        # Total
        self.text_variable_total = tk.StringVar()
        self.label_total = ttk.Label(self, textvariable=self.text_variable_total)

        self.init_ui()

    def init_ui(self):
        """Initializes the ui"""
        self.get_new_problem()
        self.label_problem.grid(row=0, columnspan=6, pady=20)

        # Place buttons
        for i, val in enumerate(self.buttons):
            val.grid(row=1, column=i, padx=10, pady=20)

        # Text label for score
        self.label_score.grid(row=2, columnspan=6, pady=20)
        self.set_text_score()

        # Text label for total
        self.label_total.grid(row=3, columnspan=6, pady=20)
        self.set_text_total()

        self.pack()

    def set_text_score(self):
        self.text_variable_score.set(f'Your score is {self.score}')

    def set_text_total(self):
        self.text_variable_total.set(f'Your total attempts is {self.total}')

    def create_button(self, value):
        return ttk.Button(self, command=lambda: self.check_answer(value), text=str(value))

    def check_answer(self, value):
        """
        This method checks if the value (of the button) is the same as the value of the problem or offence. If they are
        equal then it generates a new problem and updates the corresponding info.
        :param value:
        """
        self.total += 1
        self.set_text_total()

        # Checks to make sure the value of the button and problem are equal
        if self.current_problem.is_value(value):
            self.score += 1
            self.get_new_problem()
            self.set_text_score()

    def get_new_problem(self):
        """Gets a new problem from the list of offences. Makes sure that there is no duplicates in the list of problems
        given to user."""
        if not self.list_offences:
            self.list_offences = self.constant_list_offences[:]

        self.current_problem = self.list_offences.pop(random.randint(0, len(self.list_offences)-1))
        self.text_variable_problem.set(self.current_problem.name)

    def close(self):
        """Asks the user if they want to close the window, saves the score and total (if they exist)
         to the demerit-points results.txt file and closes the window"""
        if not tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            return

        if self.total:
            with open('Results.txt', 'a+') as f:
                f.seek(0)
                info = f.read(10)

                if info:
                    f.write('\n')
                f.write(f'Your average is {round(self.score/self.total*100)}% or {self.score} correct answers out of '
                        f'{self.total} total attempts. \n')
                f.write(str(time.ctime()))
        self.destroy()


def main():
    root = tk.Tk()
    root.state('zoomed')
    window = QuizWindow(root)

    def on_close():
        """Operation to be performed when closing the window and root objects"""
        window.close()
        root.destroy()

    root.protocol('WM_DELETE_WINDOW', on_close)
    root.mainloop()


if __name__ == '__main__':
    main()
