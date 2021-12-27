from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


if __name__ == '__main__':
    question_bank = []
    for question in question_data["results"]:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions(): #if quiz still has questions remaining
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.check_score()}")


# from prettytable import PrettyTable
# import itertools
#
#
# class User:
#     id_iter = itertools.count()
#     def __init__(self, user_id, username):
#         self.id = next(self.id_iter)
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "angela")
# user_2 = User("002", "jack")
#
# table = PrettyTable()
# table.field_names = ['user_id', 'username']
# table.add_row([user_1.id, user_1.username])
# table.add_row([user_2.id, user_2.username])
# print(table)
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)
