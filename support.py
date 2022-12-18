# This program is to quiz a person on their knowledge of the demerit point system.
# ~ Perhaps make it so that the user runs through all the questions before giving duplicate questions
import random
from dataclasses import dataclass


@dataclass()
class Offence:
    """
    This class handles the values of an offence and checks if a value is corrected based on the number of points
    """
    value: int
    name: str

    # Other methods
    def is_value(self, value):
        return self.value == value

    def __repr__(self):
        return f'{self.name} is an offence costing {self.value} points'


def get_offences_info():
    """Gets the info related to the offences"""
    # Values
    list_of_offences = []
    value = 0

    with open('Demerit-Points.txt') as f:
        for i in f:
            # Checks if the first character of the line is an int, if it is, the val is assigned to value
            if i[0].isnumeric():
                value = i[0]
            else:
                # An offence obj is created and appended to the list of offences to be used in the next section
                offence = Offence(int(value), i[:-1])
                list_of_offences.append(offence)

    return list_of_offences


def main():
    # Values
    correct = 0
    total = 0
    list_of_offences = get_offences_info()
    list_used_during_loop = []

    # Input and output and processing
    while True:
        # Makes sure the list of violations used in the program doesn't repeat until all violations have been used
        if len(list_used_during_loop) == 0:
            list_used_during_loop = list_of_offences[:]

        # Gets an offence, prints the name of the offence and asks for user input
        violation = list_used_during_loop.pop(random.randint(0, len(list_used_during_loop) - 1))

        # Stays the same
        print(str(total + 1) + '.', violation.name)
        choice = int(input('Enter the value of the offence (2-7) or -1 to exit: '))

        # Processes input and updates correct and total values
        # Exits out the program
        if choice == -1:
            # Prints out the results if there was at least 1 questions answered
            if total != 0:
                print('Your average is ' + str(round(correct / total * 100)) + '% or ' + str(
                    correct) + ' correct answers out of ' + str(total) + ' total answers')
            break
        # Checks if the answer is correct and adds 1 point to correct if it is
        elif violation.is_value(choice):
            print('You are correct')
            correct += 1
        else:
            print(f'You are wrong, this offence is valued at {violation.value}')
        total += 1

        # Remove after testing
        print(list_used_during_loop)
        print(len(list_used_during_loop))

        print()


if __name__ == '__main__':
    main()
