# import necessary libraries
import json
import random
import os

# add function to load question from JSON file
def load_questions(quiz_output):
    if not os.path.exists(quiz_output):
        print(f"Error: File '{quiz_output}' does not exist.")
        return []
    
    try:
        with open(quiz_output, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('questions', [])
    except json.JSONDecodeError:
        print(f"Error: File '{quiz_output}' is not a valid JSON file.")
    return []

# add function to ask a question and check the answer
def ask_question(question_data):
    print("Question:")
    print(question_data['question'])
    user_answer = input("Your answer: ").strip()
    correct_answer = question_data['answer'].strip()
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")

# main function to load the questions and pick a random one
def main():
    print("Welcome to the Quiz!")
    print("Current Working Directory:", os.getcwd())  # Check current directory
    questions = load_questions(r'C:\Users\Chloie Nicole Rivera\OneDrive - Polytechnic University of the Philippines\Desktop\BSCPE 1-6\2ND SEM\[CMPE 103] OOP\rivera_python_quiz_creator_oop\python_quiz.json')
    if not questions:
        print("No questions found in the quiz file.")
        return
    
    # loop to allow multiple questions
    while questions:
        selected_questions = random.choice(questions)
        ask_question(selected_questions)
        questions.remove(selected_questions)
        continue_quiz = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_quiz != 'yes':
            print("Thank you for playing!")
            break

    print("Thank you for playing!")

# entry point check for running the program
if __name__ == "__main__":
    main()