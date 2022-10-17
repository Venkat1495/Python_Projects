class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if (len(self.question_list) - 1) >= self.question_number:
            return True
        else:
            return False
    def q_text(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_ans = input(f"Q.{self.question_number} {self.current_question.text} (True/False)?: ")
        self.check_answer()


    def check_answer(self):
        if self.current_question.answer.lower() == self.user_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {self.current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
