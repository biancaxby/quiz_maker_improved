# Quiz maker with application of oop 

class QuizMaker:
    def add__questions(self):
        while True:    
            subjects = input('What subject would you like?(math, science, history, english)(enter quit to return)')
            if subjects == "quit":
                break
            try: 
                questions = open(f"{subjects}.txt", "a")
                questions.write(input('Enter a question: \n'))
                questions.write(f"a) {input('Enter option a: ')}\n")
                questions.write(f"a) {input('Enter option b: ')}\n")
                questions.write(f"a) {input('Enter option c: ')}\n")
                questions.write(f"a) {input('Enter option d: ')}\n")
                questions.write(f"The correct answer is: {input('Enter the correct answer: ')}\n")
            finally:
                questions.close

quizmaker = QuizMaker()
quizmaker.add__questions()


#ask user what sub
#open file
#add question
#add options
#close file