class QuizBrain:
    def __init__(self, q_list): # Init method
        self.question_number = 0  # Attribute
        self.question_list = q_list # Attribute
        self.score = 0

    def still_has_questions(self):  # Method
        return self.question_number < len(self.question_list) # will return True or False


    def next_question(self): # Method
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score} out of {self.question_number} questions.")
        print("\n")