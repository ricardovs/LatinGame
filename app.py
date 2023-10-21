import os
from game import DeclensionEndingGame

class App():
    def __init__(self):
        self.status = 'InitialPage'
        self.clear()

    def run(self):
        window = getattr(self, self.status)
        return window()

    def clear(self):
        # Clearing the Screen
        os.system('clear')

    def InitialPage(self):
        self.clear()
        print("Welcome to the Latin conjugation game !!")
        while True:
            print("Guess declension ending.")
            option = input("Press Enter to continue (or quit)...")
            self.status = "DeclensionPage"
            if option == 'quit':
                return False
            else:
                return True


    def DeclensionPage(self):
        self.clear()
        print("This is the declesion page !!")
        game = DeclensionEndingGame()
        game.newQuestion()
        while True:
            print("Give the declension ending for this case (or quit)")
            option = input("R: ")
            if option == "quit":
                self.status = 'InitialPage'
                return True

