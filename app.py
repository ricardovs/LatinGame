import os
from game import DeclensionEndingGame

class App():
    def __init__(self):
        self.status = 'InitialPage'
        self.game = None
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
        print("Guess declension ending.")
        option = input("Press Enter to new game or quit ...\n")
        if option == 'quit':
            return False
        self.status = "DeclensionPage"
        self.game = DeclensionEndingGame()
        self.clear()
        return True

    def DeclensionPage(self):
        if not self.game.isWaiting():
            self.game.newQuestion()
            self.clear()
        print("This is the guessing page !!")
        print("Give the declension ending for this case (or quit)")
        print(self.game.getQuestion())
        option = input("R: ")
        if option == "quit":
            self.status = 'InitialPage'
            return True
        self.game.addAnswers(option)
        input("Press Enter to continue (or quit)...")
        return True