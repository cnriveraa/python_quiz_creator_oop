# python_quiz_creator_main_code.py

# output file name
file_name = "quiz_questions.txt"

while True: # start an infinite loop to keep asking for questions
    question = input("Enter the question: ")     # prompt for the user to enter the questions
    
    asnwers = {} # a dictionary to store the answers
    
    for option in ['a', 'b', 'c', 'd']:
        answer = input(f"Enter answer for option {option}: ")    # prompt for the user to enter the answers
        answer[option] = answer       # store the answers in the dictionary

    correct_answer = input("Enter the correct answer (a, b, c, or d): ").lower()    # prompt for the correct answer

    # validate the correct answer
    if correct_answer not in answer:
        print("Invalid answer. Please enter a, b, c, or d.")  # error message if the answer is not valid
        continue  # restart the loop to ask questions again


# add the questions and answers to the text file
# ask if the user wants another question