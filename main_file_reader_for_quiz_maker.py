from file_reader_for_quiz_maker import FileReader

print('1. Start quiz \n2. View top scorers')
user_input = input('What would you like to do?')

file_reader = FileReader()
if user_input == '1':
    file_reader.quiz_file_reader()
if user_input == '2':
    file_reader.score_viewer()
else:
    print('Invalid input')