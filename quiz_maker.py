# Quiz maker with application of oop 

class QuizMaker:
    def add__questions(self):
        while True:    

            # Chooses the subject the user wants to add questions to
            subjects = input('What subject would you like?(math, science, history, english)(enter quit to return)').lower()
            if subjects == "quit":      # Returns when 'quit' is used by user
                break
            try: 
                questions = open(f"{subjects}.txt", "a")            # Opens file
                questions.write(input('Enter a question: \n'))      # Adds or appends the questions, options, and answer to the end of the list
                questions.write(f"a) {input('Enter option a: ')}\n")
                questions.write(f"a) {input('Enter option b: ')}\n")
                questions.write(f"a) {input('Enter option c: ')}\n")
                questions.write(f"a) {input('Enter option d: ')}\n")
                questions.write(f"The correct answer is: {input('Enter the correct answer: ')}\n")
            finally:
                questions.close     # Closes the file
    
    def file_editor(self):
            while True:
        # Chooses the subject the user wants to add questions to
                subjects = input('What subject would you like?(math, science, history, english)(enter quit to return)').lower()
                if subjects == "quit":      # Returns when 'quit' is used by user
                    break
                try:

                    # Reads content on the text file
                    file_content = open(f"{subjects}.txt", "r")

                    # Reads each line in the file and enumerates it
                    lines = file_content.readlines()
                    for i, line in enumerate (lines, 1):
                        print(f"{i} {line.strip()}")
                    
                    # Prints the entire text file
                    print(file_content.read)
                    
                    # Allows user to choose what line to edit 
                    edit_line = int(input('Enter what line you want to edit(Enter 0 to quit): '))
                    if edit_line == "0":
                        break
                    # Asks user what they want to edit on the line
                    edited_statement = input(f"Enter new statement on line {edit_line}: \n")

                    # Replaces the line
                    lines[edit_line - 1] = f"{edited_statement}\n"

                    # Writes file again
                    updated_file_content = open(f"{subjects}.txt", "w")
                    updated_file_content.writelines(lines)

                finally:
                    updated_file_content.close()         # Closes file

    def view_questions():
        while True:
            subjects = input('What subject? (math, science, english, history) or enter "quit": ').lower()
            if subjects == "quit":
                break
            questionares = open(f"{subjects}.txt", 'r')
            print(questionares.read())  # Prints all the questions stored on the text file