# def calculate_combined_counts(group, real_distributions):

#     combined_counts = {q: {'ja': 0, 'nei': 0} for q in real_distributions.keys()}
#     for individual in group:
#         answers = individual['question_and_answer']
#         for item in answers:
#             question_key = item['question']
#             if question_key not in real_distributions:
#                 continue
#             if 'Ja'.lower() in item['answer'].lower():
#                 combined_counts[question_key]['ja'] += 1
#             elif 'Nei'.lower() in item['answer'].lower():
#                 combined_counts[question_key]['nei'] += 1
#     return combined_counts


# def group_evaluate(group, real_distributions):
#     combined_counts = calculate_combined_counts(group, real_distributions)
#     total_error = 0

#     for question, counts in combined_counts.items():
#         total_responses = counts['ja'] + counts['nei']
#         ja_percentage = (counts['ja'] / total_responses) * 100
#         nei_percentage = (counts['nei'] / total_responses) * 100
#         total_error += abs(real_distributions[question]['ja'] - ja_percentage) + abs(real_distributions[question]['nei'] - nei_percentage)

#     average_error = total_error / len(real_distributions)
#     return 100 - average_error,


def calculate_combined_counts(group, real_distributions):
    # Initialize combined_counts with zeros for all alternatives
    combined_counts = {q: {alt: 0 for alt in real_distributions[q]} for q in real_distributions.keys()}

    for individual in group:
        answers = individual['question_and_answer']
        for item in answers:
            question_key = item['question']
            if question_key not in real_distributions:
                continue
            # Increment the count for the given answer if it's in our alternatives
            answer_given = item['answer'].lower()
            for alternative in real_distributions[question_key]:
                if alternative.lower() in answer_given:
                    combined_counts[question_key][alternative] += 1
                    break
    return combined_counts

def group_evaluate(group, real_distributions):
    combined_counts = calculate_combined_counts(group, real_distributions)
    total_error = 0

    for question, counts in combined_counts.items():
        total_responses = sum(counts.values())
        
        if total_responses == 0: # To prevent division by zero
            continue

        for alternative in counts:
            alternative_percentage = (counts[alternative] / total_responses) * 100
            total_error += abs(real_distributions[question][alternative] - alternative_percentage)

    average_error = total_error / len(real_distributions)
    return 100 - average_error,



def evaluate(individual):
    name = individual[0]
    age = individual[1]
    interest = individual[3]  # Assuming interests are still at the 4th position
    return_value = 0
    if name == "Dave":
        return_value += 0.33
    if interest == "Birds":
        return_value += 0.34
    if age == 30:
        return_value += 0.33
    return return_value,
