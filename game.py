import json

class DeclensionEndingGame:
    def __init__(self):
        with open('data.json') as file:
            self.data = json.load(file)['declesionEnddings']
        self.questions = []
        self.waiting_answers = False

    def getQuestion(self):
        if not self.waiting_answers:
            return ""
        return self.questions[-1]['question']

    def check(self, answer):
        pass

    def newQuestion(self):
        question = {
            'question':'1st Declension, Genitive, Singular, Feminine',
            'answers' : []
        }
        self.questions.append(question)
        self.waiting_answers = True

    def isQuestionCompleted(self):
        return not self.waiting_answers

    def isWaiting(self):
        return self.waiting_answers

    def addAnswers(self, answer):
        if not self.waiting_answers:
            return False
        if not answer or answer.isspace():
            return False
        question = self.questions[-1]
        question['answers'].append(answer)
        return True

