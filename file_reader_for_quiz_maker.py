# Quiz maker with application of oop

class FileReader:
    def quiz_file_reader():
        while True:
            subjects = input("What subject would you like to do?(math, science, history, english)(Enter quit to exit): ")
            if subjects == "quit":
                break
            try:
                quiz = open(f"{subjects}.txt", "r")
                start_quiz = quiz.readlines
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