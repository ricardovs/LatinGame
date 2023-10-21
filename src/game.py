import json
from random import sample

class DeclensionEndingGame:
    def __init__(self):
        with open('./data/data.json') as file:
            self.data = json.load(file)['declensionEnddings']
        self.questions = []
        self.waiting_answers = False

    def getQuestion(self):
        if not self.waiting_answers:
            return None
        return self.questions[-1]

    def getQuestionText(self):
        question = self.getQuestion()
        if question is None:
            return "NO QUESTION"
        text = " - Declension: "
        text += self.getDeclensionText(question['declension'])
        text += "\n - Case: %s\n" % question['case']
        text += ' - Number: %s\n' % question['number'].title()
        text += ' - Gender: %s' % question['gender'].title()
        return text

    def getDeclensionText(self, declension : int):
        if declension == 1:
            return "1st"
        elif declension == 2:
            return "2nd"
        elif declension == 3:
            return "3rd"
        else:
            return "%dth" % declension

    def newQuestion(self):
        question = sample(self.data, 1)[0]
        question['answers'] = []
        self.questions.append(question)
        self.waiting_answers = True

    def isWaiting(self):
        return self.waiting_answers

    def isLastAnswerCorrect(self):
        if not len(self.questions) > 0:
            return False
        if not len(self.questions[-1]['answers']) > 0:
            return False
        respose = self.questions[-1]['ending']
        answer = self.questions[-1]['answers'][-1]
        return answer == respose

    def addAnswers(self, answer):
        if not self.waiting_answers:
            return False
        if not answer or answer.isspace():
            return False
        question = self.questions[-1]
        question['answers'].append(answer)
        if self.isCompleteAnswer():
            self.waiting_answers = False
        return True

    def isCompleteAnswer(self):
        return self.isLastAnswerCorrect()
