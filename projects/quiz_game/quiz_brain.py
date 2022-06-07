
# TODO: ask questions
# TODO: check answer is correct
# TODO: check if the quiz is over

# two attributes: question number = 0 and questions list 

from mimetypes import init
import iniconfig


class QuizBrain:
    
    def __init__(self, q_list):
        # Constructor for QuizBrain.
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # Checks to see if there are questions left in the question list.
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Progresses and prints the next question.
        curr_question = self.question_list[self.question_number]
        self.question_number += 1 # increment the question number
        user_answer = input(f"Q.{self.question_number+1}: {curr_question.text} (True/False)?: ")
        # for item in question_list:
        #     answer = input(f"Q {item+1}: {question_list.q_text}. (True/False)?: ").lower
        self.check_answer(user_answer, curr_question.answer)
    
    def check_answer(self, u_answer, c_answer):
        # Checks the answer from user input to the correct answer in the question list.
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"The correct answer was: {c_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("You got it wrong.")
            print(f"The correct answer was: {c_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")