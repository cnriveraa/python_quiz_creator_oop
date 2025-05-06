# import necessary libraries
import json
import random
import os

# add function to load question from JSON file
def load_question(quiz_output):
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
def main(quiz_output):
    print("Welcome to the Quiz!")
    question = load_question(quiz_output)
    if not question:
        print("No questions found in the quiz file.")
        return
    question = random.choice(question)
    ask_question(question)

# entry point check for running the program
if __name__ == "__main__":
    quiz_output = 'python_quiz.json'  # specify the path to your JSON file
    main(quiz_output)