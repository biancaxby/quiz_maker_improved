# Quiz maker with application of oop format

class FileReader:
    def __init__(self, usernames):
         self.usernames = usernames
         
    def quiz_file_reader(self):
        while True:

            subjects = input("What subject would you like to do?(math, science, history, english)(Enter quit to exit): ")
            if subjects == "quit":
                break
            try:
                quiz = open(f"{subjects}.txt", "r")
                start_quiz = quiz.readlines()
                count_line = 0         # Counts how many lines 
                correct_answers = 0    # Counts how many correct answers 
                question_counter = 0 
               
                while count_line < len(start_quiz):
                    for _ in range(5):      # Prints 5 lines of the text file
                        if count_line >= len(start_quiz):
                            break      # Exits the loop if the file has no more lines

                        striped_lines = start_quiz[count_line].strip()      # Separates each line

                        # Ignores blank lines and lines with the answer key
                        if striped_lines == striped_lines.startswith("The correct answer is:"):
                            count_line += 1
                            continue
                        
                        # Prints the questions and options on the txt file
                        print(striped_lines)
                        count_line += 1

                        # Checks if the line is the answer key
                        if count_line < len(start_quiz) and start_quiz[count_line].startswith("The correct answer is:"):
                            answer = start_quiz[count_line].replace("The correct answer is: ", "").strip()   # Separates the answer
                            count_line += 1

                            # Asks user for the answer to the question
                            user_answer = input('What do you think is the answer?: ').lower().strip()
                            question_counter += 1      # Counts how many questions have been displayed

                            if  user_answer == answer:
                                    print("Correct!")     # Prints correct if the answer is correct
                                    correct_answers += 1  # Adds to the number of correct answers
                            if user_answer != answer:
                                print("Wrong!")          # Prints wrong is the answer is wrong
                            if user_answer == "quit":     # Returns to the menu 
                                    break
                        
                percentage = correct_answers / question_counter * 100    # Calculates the percentage of the score 
                print(f"Congrats {self.usernames}! You have scored {correct_answers} out of {question_counter}!\n Which means you have answered {percentage}% of the questions correctly!")
            
            finally:
                quiz.close()

    def score_viewer(self, usernames):
        # Create a list of [username, score] pairs
        top_scorers = [[name, score] for name, score in zip(usernames)]    
        
        # Sort the list by score in descending order
        top_scorers.sort(key=lambda x: x[1], reverse=True)
        
        # Display the sorted scores
        print("Top Scorers:")
        for i, (name, score) in enumerate(top_scorers, 1):
            print(f"{i}. {name} {score} points")

usernames = input("What is your name?: ")
file_reader = FileReader(usernames)
file_reader.quiz_file_reader()
            