from quiz_maker import QuizMaker

print('1. Make quiz \n2. Edit questions \n3. View questions')
user_input = input('What would you like to do?(Enter options 1-3)')

quiz = QuizMaker()
if user_input == '1':
    quiz.add__questions()
elif user_input == '2':
    quiz.file_editor()
elif user_input == '3':
    quiz.view_questions()
else:
    print('Invalid option')