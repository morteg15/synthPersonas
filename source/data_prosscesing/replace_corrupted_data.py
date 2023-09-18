import difflib
import toml
import json
import os

def replace_corrupted_with_original(corrupted_qa_list, original_questions):
    replaced_qa_list = []
    for qa in corrupted_qa_list:
        corrupted_question = qa['question']
        closest_match = difflib.get_close_matches(corrupted_question, original_questions.keys(), n=1)
        if closest_match:
            qa['question'] = closest_match[0]
        replaced_qa_list.append(qa)
    
    return replaced_qa_list

def load_original_questions(file_path):
    """Load the original questions from a JSON file."""
    with open(file_path, "r", encoding='utf8') as file:
        return json.load(file)

def load_and_fix_toml(file_path, original_questions):
    """Load TOML data, fix corrupted sections, and return the corrected data."""
    with open(file_path, "r", encoding="latin1") as file:
        data = toml.load(file)
    data["question_and_answer"] = replace_corrupted_with_original(data["question_and_answer"], original_questions)
    return data

def save_fixed_toml(data, directory, filename):
    """Save the corrected TOML data to the specified directory with the given filename."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w', encoding="utf8") as file:
        file.write(toml.dumps(data))

def process_toml_file(input_path, output_dir, original_questions_path):
    """Process and fix a single TOML file."""
    original_questions = load_original_questions(original_questions_path)
    # find all the toml files in the directory
    files = os.listdir(input_path)
    for file in files:
        if file.endswith(".toml"):
            fixed_data = load_and_fix_toml(f"{input_path}\\{file}", original_questions)
            save_fixed_toml(fixed_data, output_dir, file)
            print(f"Processed and saved corrected data to: {os.path.join(output_dir, file)}")

input_path = "session_test\profiles"
output_dir = "fixed_toml_files"
original_questions_path = "data/gss/survey_asked.json"

process_toml_file(input_path, output_dir, original_questions_path)
