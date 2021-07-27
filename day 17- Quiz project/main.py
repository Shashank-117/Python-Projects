from data import question_data
from question_model import question
from quiz_brain import QuizBrain
question_bank = []

for q in question_data:
    ques_text = q["text"]
    ques_answer = q["answer"]
    new_question = question(ques_text, ques_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions() == True:
    quiz.new_question()

print("You've completed the quiz !!! Congratulations !!!")
print(f"Your final score was {quiz.score}/ {quiz.question_number}")
