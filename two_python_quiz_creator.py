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
# main function to load the questions and pick a random one
# entry point check for running the program