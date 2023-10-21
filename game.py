import json

class Game:
    def __init__(self):
        pass
    def getQuestion(self):
        return ""
    def check(self, awnser):
        pass
    def newQuestion(self):
        pass
    def isQuestionCompleted(self):
        pass

class DeclensionEndingGame(Game):
    def __init__(self):
        with open('data.json') as file:
            self.data = json.load(file)['declesionEnddings']
    def newQuestion(self):
        pass