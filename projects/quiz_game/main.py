from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    question_bank.append(Question(question_text, question_answer))

# print(question_bank[0].text)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions(): # while loop to keep going if the quiz still has questions
    quiz.next_question()