class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q. {self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.increase_score()
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is {self.check_score()}.")
        print(f"The correct answer was: {correct_answer}.\n")

    def check_score(self):
        return f'{self.score}/{self.question_number}'

    def increase_score(self):
        self.score += 1