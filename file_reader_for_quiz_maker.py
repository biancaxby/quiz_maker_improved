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