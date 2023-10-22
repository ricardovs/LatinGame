import os
from .game import DeclensionEndingGame

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
        print("LATIN GAME")
        print("Welcome to the Latin conjugation game !!")
        print("Guess declension ending. Choose command: ")
        print("  - play      : Start a new game")
        print("  - report    : Report previous game statistics.")
        print("  - configure : Configure game options.")
        print("  - quit      : End game and clear all data.")
        option = input("Please enter one comand ...\n- ")
        if option == 'quit':
            return False
        elif option == 'report':
            self.status = "ReportPage"
        elif option == 'configure':
            self.status = "ConfigPage"
        elif option == 'play':
            self.status = "DeclensionPage"
            self.game = DeclensionEndingGame()
        else:
            print("INVALID COMMAND")
            print("Please try again.")
            input("Please press Enter to continue ...\n")
        self.clear()
        return True

    def ConfigPage(self):
        self.clear()
        print("CONFIGURATION PAGE")
        print("Sorry! :(")
        print("Page under construction ...")
        input("Please press Enter to continue ...\n")
        self.status = 'InitialPage'
        return True

    def ReportPage(self):
        self.clear()
        print("REPORT PAGE")
        print("Sorry! :(")
        print("Page under construction ...")
        input("Please press Enter to continue ...\n")
        self.status = 'InitialPage'
        return True

    def DeclensionPage(self):
        self.clear()
        print("GUESSING PAGE")
        if not self.game.isWaiting():
            self.game.newQuestion()
        print("Give the declension ending for this case (or 'back' or 'answer')")
        print(self.game.getQuestionText())
        option = input("R: ")
        if option == "back":
            self.status = 'InitialPage'
            return True
        elif option == 'answer':
            print(" Answer: " + str(self.game.getAnswers()))
            self.game.setWaiting(False)
        elif not self.game.isValidAnswer(option):
            print("INVALID ANSWER")
        elif self.game.wasAnswerTried(option):
            print("ALREADY TRIED")
        elif not self.game.addAnswer(option):
            print("NOT ADDED")
        elif self.game.isLastAnswerCorrect():
            print("CORRECT ANSWER")
            if not self.game.isCompleteAnswer():
                print("An alternative answer is available.")
                print("Please try a new guess for complete answer.")
        else:
            print("WRONG ANSWER")
            print("Try again!")
        option = input("Press Enter to continue (or send 'back' command)...\n")
        if option == "back":
            self.status = 'InitialPage'
            return True
        return True
