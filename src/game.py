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
        text += "\n - Case: %s\n" % question['case'].title()
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
        question = sample(self.data, 1)[0].copy()
        question['answers'] = []
        question['endings'] = [question.pop('ending')]
        for value in self.data:
            if value['case'] != question['case']:
                continue
            if value['declension'] != question['declension']:
                continue
            if value['gender'] != question['gender']:
                continue
            if not value['ending'] in question['endings']:
                question['endings'].append(value['ending'])
        self.questions.append(question)
        self.waiting_answers = True

    def isWaiting(self):
        return self.waiting_answers

    def isLastAnswerCorrect(self):
        if not len(self.questions) > 0:
            return False
        if not len(self.questions[-1]['answers']) > 0:
            return False
        resposes = self.questions[-1]['endings']
        answer = self.questions[-1]['answers'][-1]
        return answer in resposes

    def addAnswer(self, answer):
        if not self.waiting_answers:
            return False
        if not self.isValidAnswer(answer):
            return False
        question = self.questions[-1]
        if not answer in question['answers']:
            question['answers'].append(answer)
        if self.isCompleteAnswer():
            self.waiting_answers = False
        return True

    def isValidAnswer(self, answer):
        return type(answer) is str and (not answer.isspace())

    def wasAnswerTried(self, answer):
        if not self.isValidAnswer(answer):
            return False
        if not len(self.questions) > 0:
            return False
        return answer in self.questions[-1]['answers']

    def isCompleteAnswer(self):
        if not len(self.questions) > 0:
            return False
        question = self.questions[-1]
        for ending in question['endings']:
            if ending not in question['answers']:
                return False
        return True
