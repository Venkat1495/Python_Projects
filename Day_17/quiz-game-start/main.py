from question_model import Question
from data import question_data

question_bank = []

for question_dic in question_data:
    temp_question = Question(question_dic["text"], question_dic["answer"])
    question_bank.append(temp_question)
