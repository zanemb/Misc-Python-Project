# Zane Mazor-Brown
# Professor King
# BUS 392-01
# 10 November 2021

# College of Business Exam Scoring Application

# The department’s Scantron machine has broken. Due to budget pressures, the
# Dean’s office has asked you to create an application that grades the Scantron
# portion of student exams. The exam has 25 multiple-choice questions. The
# correct answers are on Canvas in the supplied answers.txt file under Week 7.

# Your program should read from the answers.txt file and store these correct
# answers in a list. You must create your own text file to test the application
# with one student answer per line – no question numbers. You must name the
# file “student_answers.txt”. The program should read the student’s answers for
# each of the 25 questions from a text file and store the answers in another
# list. After the student’s answers have been read from the file, the program
# should display a message indicating whether the student passed or failed the
# exam. (A student must correctly answer 18 of the 25 questions to pass the
# exam.) It should then display the total number of correctly answered 
# questions, the total number of incorrectly answered questions, and a list
# showing the question numbers of the incorrectly answered questions. The 
# deliverable is a source code file with the .py extension submitted through 
# Canvas.

# NOTES:
#   - Your program must use functions and a main().
#   - Use of exception handling is encouraged!
#   - Your program must have comments for each line or section in code 
#     (including in main()).

# define main function
def main():
    # open answers.txt file and add answers to a list
    answer_key = create_answer_list("answers.txt")
    # open student_answers.txt file and add answers to a list
    stud_answers = create_answer_list("student_answers.txt")
    # compare student answers with the key and return list of wrong answers
    wrong_answers = evaluate_answers(answer_key, stud_answers)
    # use quantity of incorrect answers to display a pass or fail message
    display_pass_fail(wrong_answers)
    # use quantity of incorrect answers to display total right/wrong and
    # which questions were answered incorrectly
    display_right_wrong(wrong_answers)

# define function to open a file and return contents (answers) as a list
def create_answer_list(file):
    # create empty list to append answers to
    list = []
    # open file with argument provided in read mode
    opened_file = open(file, "r")
    # iterate through file, get rid of end whitespaces, and add values to list
    for answer in opened_file:
        list.append(answer.rstrip())
    # return the answer list to variable when function is called
    return list

# define function to compare 2 answer lists + append wrong answers to a list
def evaluate_answers(answer_key, stud_answers):
    # define empty list to accept wrong answer index positions
    wrong_answers = []
    # iterate through 24 (25) items in each list
    for i in range(24):
        # condition for one of the 25 answers being correct
        if answer_key[i] == stud_answers[i]:
            continue
        # condition for one of the 25 answers being incorrect
        else:
            wrong_answers.append(i)
    # return list of wrong answers for use in later functions
    return wrong_answers

# define function to display pass/fail given number of wrong answers
def display_pass_fail(wrong_answers):
    # find number of total incorrect answers and store in variable num
    num = len(wrong_answers)
    # calculate score out of 25 using number of incorrect answers
    score = 25 - num
    # condition for getting more than 7 questions wrong (fail)
    if num > 7:
        # display fail message
        print("Student Failed")
    # condition for passing if student got 7 or fewer questions incorrect
    else:
        # display pass message
        print("Student Passed")

# define function to display # of correct/incorrect
# questions and which questions were incorrect
def display_right_wrong(wrong_answers):
    # find quantity of incorrect answers
    wrong = len(wrong_answers)
    # calculate quantity of correct answers given quantity of incorrect
    score = 25 - len(wrong_answers)
    # display quantity of correct/incorrect answers
    print(f"Student got {score} questions correct and {wrong} questions incorrect")
    # display question numbers of incorrect answers
    for i in wrong_answers:
        # add 1 because indexing starts at 0
        i += 1
        print(f"Question #{i} was incorrect")

# call main function
main()