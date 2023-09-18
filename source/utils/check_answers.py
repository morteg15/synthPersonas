import toml
import os


def count_answers_in_toml(directory_path, question_dict):
    """
    Count the answers for specific questions in TOML files within a directory.

    :param directory_path: Path to the directory containing the TOML files.
    :param question_dict: Dictionary containing the question and its alternatives.
    :return: Dictionary with the count of each alternative.
    """
    # Create a new dictionary for the counts
    count_dict = {question: {alternative: 0 for alternative in alternatives} for question, alternatives in question_dict.items()}
    print("there are this many toml files in the directory:", len(os.listdir(directory_path)))
    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".toml"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding="utf8") as file:
                data = toml.load(file)
            
            # Check if 'question_and_answer' key exists in the TOML file
            if 'question_and_answer' in data:
                for qna in data['question_and_answer']:
                    # Check if the question matches any in our question_dict
                    if qna['question'] in question_dict:
                        matched = False
                        for alternative in question_dict[qna['question']]:
                            if alternative.lower() in qna['answer'].lower():
                                count_dict[qna['question']][alternative] += 1
                                matched = True
                        # If no match was found, log the unexpected answer
                        if not matched:
                            print(f"Unexpected answer '{qna['answer']}' for question '{qna['question']}' in file {filename}")

    return count_dict


def calculate_error_margin(true_distribution, output_counts):
    """
    Calculate the error margin between the true distribution and the output counts.

    :param true_distribution: Dictionary containing the true distribution percentages for each question.
    :param output_counts: Dictionary containing the counts of each alternative for each question from the TOML files.
    :return: Dictionary containing the error margin for each question and alternative.
    """
    error_margin = {}
    avrage_error = 0
    count = 0
    for question, true_dist in true_distribution.items():
        # Check if the question exists in both dictionaries
        if question in output_counts:
            total_responses = sum(output_counts[question].values())
            error_margin[question] = {}

            for alternative, true_percentage in true_dist.items():
                # Calculate the percentage from the output counts
                output_percentage = (output_counts[question].get(alternative, 0) / total_responses) * 100
                # Calculate the error margin for this alternative
                error_margin[question][alternative] = abs(true_percentage - output_percentage)
                avrage_error += error_margin[question][alternative]
                count += 1
    avrage_error = avrage_error / count
    return error_margin, avrage_error


# # Example usage
# directory_path = "source\\api\\session_ga\\session_test_fittest_group\profiles"  # Replace with the path to your TOML files
# question_dict = {
#     "Bruker du plattformen Discord? Begrun svaret (hold begrunnelsen kort) og svar endelig svar er [ja] eller [nei]." : {"Ja": 80, "Nei": 20}
# }
# key = "Bruker du plattformen Discord? Begrun svaret (hold begrunnelsen kort) og svar endelig svar er [ja] eller [nei]."

# result = count_answers_in_toml(directory_path, question_dict)
# error = calculate_error_margin(question_dict[key], result[key])
# print(result)
# print("true distribution:", question_dict[key])
# print("errors on", error)