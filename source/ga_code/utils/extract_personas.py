import toml
import os

def extract_personas_from_files(directory_path):
    personas = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".toml"):
            file_path = os.path.join(directory_path, filename)
            remove_newlines_from_answers(file_path)
            with open(file_path, 'r' ,encoding="utf8") as file:
                data = toml.load(file)
                personas.append(data)
    return personas

def remove_newlines_from_answers(filename):
    with open(filename, 'r' ,encoding="utf8") as file:
        lines = file.readlines()

    # Process the lines to remove newlines from answers
    in_answer = False
    new_lines = []
    current_answer = ""

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("answer ="):
            in_answer = True
            current_answer += stripped_line
            if current_answer.endswith("\""):
                in_answer = False
                new_lines.append(current_answer +"\n")
                current_answer = ""
        elif in_answer and not stripped_line.endswith("\""):
            current_answer += " " + stripped_line
        elif in_answer and stripped_line.endswith("\""):
            current_answer += " " + stripped_line
            new_lines.append(current_answer +"\n")  # Add an extra newline after each answer
            current_answer = ""
            in_answer = False
        else:
            new_lines.append(line)

    # If we're still inside an answer at the end of the file, append the current answer
    if in_answer:
        new_lines.append(f'answer = {current_answer}\n')

    # Remove any trailing empty lines
    new_lines[-1] = new_lines[-1].replace("\n", "")

    # Write the processed lines back to the file
    with open(filename, 'w', encoding='utf8') as file:
        file.writelines(new_lines)



if __name__ == "__main__":
    filename = "source\\api\\session\\session_ga_g8-12\\profiles\\person_11.toml"
    # remove_newlines_from_answers(filename)
    with open(filename, 'r'  ,encoding="utf8") as file:
        data = toml.load(file)
    print(data)
