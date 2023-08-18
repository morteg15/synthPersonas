def create_survey():
    questions = [
        {
            "question": "What is the primary color used to depict water in most maps?",
            "options": ["Red", "Green", "Blue", "Yellow"],
            "answer": "Blue"
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere for photosynthesis?",
            "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"],
            "answer": "Carbon dioxide"
        }
    ]
    return questions

def answer_survey_with_LLM(questions, llm):
    # Using a mock function for llm.predict. Replace with actual function call.
    llm_answers = []
    for q in questions:
        llm_response = llm.predict(q["question"], q["options"]) # assuming llm.predict returns one of the options
        llm_answers.append(llm_response)
    return llm_answers

def grade_survey(llm_answers, correct_answers):
    score = 0
    for i in range(len(llm_answers)):
        if llm_answers[i] == correct_answers[i]:
            score += 1
    return score / len(llm_answers)

def main():
    survey = create_survey()
    correct_answers = [q["answer"] for q in survey]

    # Mock LLM interface for demonstration. Replace with your LLM's API/interface.
    class MockLLM:
        def predict(self, question, options):
            # For demonstration purposes, return a random choice. In practice, replace with actual LLM call.
            import random
            return random.choice(options)

    llm = MockLLM()
    llm_responses = answer_survey_with_LLM(survey, llm)

    fitness_score = grade_survey(llm_responses, correct_answers)
    print(f"Fitness Score: {fitness_score*100:.2f}%")

if __name__ == "__main__":
    main()
