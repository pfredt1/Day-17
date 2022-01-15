from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
counter = 1
question_bank = []
for i in question_data:
    text = i['question']
    answer = i['correct_answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)
# print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() == True:
    quiz.next_question()



