import os
import toml

def classify_answer_based_on_score(answer):
    score = 0
    if "ikke medlem" in answer.lower():
        score += 1
    if "bare ikke" in answer.lower():
        score += 1
    if " ja " in answer.lower():
        score -= 1
    if "medlem" in answer.lower() and "ikke medlem" not in answer.lower():
        score -= 1

    if score > 0:
        return answer + " Alternativ: Ikke nevnt"
    else:
        return answer + " Alternativ: Nevnt"

def process_toml_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = toml.load(f)

    if "question_and_answer" in data:
        for qa in data["question_and_answer"]:
            if 'nevnt' in qa["question"].lower() or 'ikke nevnt' in qa["question"].lower():
                qa["answer"] = classify_answer_based_on_score(qa["answer"])

    return data

def save_to_new_file(data, filepath, output_directory):
    new_filepath = os.path.join(output_directory, os.path.basename(filepath))
    with open(new_filepath, 'w', encoding='utf-8') as f:
        toml.dump(data, f)

def main(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".toml"):
            filepath = os.path.join(input_directory, filename)
            processed_data = process_toml_file(filepath)
            save_to_new_file(processed_data, filepath, output_directory)

    print(f"Processed all TOML files from {input_directory} and saved the modified files in {output_directory}.")

if __name__ == "__main__":
    INPUT_DIRECTORY = "session_data\profiles"
    OUTPUT_DIRECTORY = "session_data_processed\profiles"
    main(INPUT_DIRECTORY, OUTPUT_DIRECTORY)
