import random


class NumberGuessingGame:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.again = "y"
        # to avoid 'Instance attribute guess defined outside __init__' warning
        self.number_to_guess = 0
        self.guess = 0
        self.tries = 0

        greeting = input("Would you like to play a number guessing game? (y/n)")
        if greeting.lower() == "y":
            self.play_guessing_game()
        else:
            print("Thank you anyway")

    def play_guessing_game(self):
        while self.again.lower() == "y":
            # number_to_guess, guess & tries müssen neu in der Methode belegt werden, damit bei wiederholten runden
            # die Werte neu generiert/ zurückgesetzt werden
            self.number_to_guess = random.randrange(self.start, self.stop)
            self.guess = 0
            self.tries = 1
            while self.guess != self.number_to_guess:
                try:
                    self.guess = int(input("Guess the number: "))
                    if self.guess == self.number_to_guess:
                        print("You've won. The number to guess was {} and you needed {} trie(s)."
                              .format(self.number_to_guess, self.tries))
                    else:
                        print("You need to try again")
                        self.tries += 1
                except ValueError as e:
                    print("Only int numbers are allowed. You typed", e)
            self.again = input("Would you like to play again?: (y/n)")
        print("Thank you for playing.")


# Beispielaufruf des Spiels: range der Zahl in Klammern (start, stop)
start_intervall = int(input("Startintervall: "))
stop_intervall = int(input("Grenze (exklusiv): "))
NumberGuessingGame(start_intervall, stop_intervall)
