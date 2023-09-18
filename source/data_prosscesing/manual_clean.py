

import toml
import os

def save_fixed_toml(data, directory, filename):
    """Save the corrected TOML data to the specified directory with the given filename."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w', encoding="utf8") as file:
        file.write(toml.dumps(data))

def update_profile_answers(profile_path):
    with open(profile_path, 'r', encoding='utf8') as f:
        profile = toml.load(f)

    for q_and_a in profile["question_and_answer"]:
        question = q_and_a["question"]
        answer = q_and_a["answer"]

        options_start = question.find('[')
        options_end = question.find(']')
        options = question[options_start+1:options_end].split(', ')
        options = [option.replace("'","") for option in options]
        
        for option in options:
            if option.lower() in answer.lower():
                break
        else:
            # If none of the options were found in the answer, let the user pick one
            print(question)
            print(answer)
            for idx, option in enumerate(options):
                print(f"{idx+1}. {option}")
            
            choice = int(input("Velg et alternativ: ")) - 1
            updated_answer = answer + f" [{options[choice]}]"
            q_and_a["answer"] = updated_answer

    # Save changes to a new folder
    save_fixed_toml(profile, "manual_fixed_profiles", os.path.basename(profile_path))

def process_folder(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".toml"):
                print(f"Processing {file}...")
                file_path = os.path.join(root, file)
                update_profile_answers(file_path)
                input("Press Enter to continue to the next profile...")


profile_path = "session_fixed\profiles"
process_folder(profile_path)
