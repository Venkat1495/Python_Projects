from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_dic in question_data:
    temp_question = Question(question_dic["text"], question_dic["answer"])
    question_bank.append(temp_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.q_text()

print(f"You completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")
