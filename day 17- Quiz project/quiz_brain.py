class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        a = len(self.question_list)
        if self.question_number < a:
            return True
        else:
            return False

    def new_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} type (true/false) :")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print('You got it right !!!')
            self.score += 1
            print(f"The correct answer was {current_answer}")
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("That's wrong")
            print(f"The correct answer was {current_answer}")
            print(f"Your current score is {self.score}/{self.question_number}")


