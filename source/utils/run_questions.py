# import os
# from api.create_session import session

# def create_sessions_from_questions(questions: list):
#     for question in questions:
#         # For hvert spørsmål, opprett en ny sesjon og navngi mappen med en unik identifikator.
#         for session_name in questions[question]:
#             session(question, session_name)




# if __name__ == "__main__":

#     create_sessions_from_questions(questions_set)



"""
"Bruker du plattformen Discord? svar ja eller nei "
"""
# Discord, J 9-11
# Discord, G 9-11

"""
"Bruker du Facebook? svar ja eller nei"
"""
#Facebook, J 9-11
#Facebook, G 9-11
#Facebook, J 12-14
#Facebook, G 12-14
"""
Ser du på videoer på internett som handler om gaming? svar ja eller nei"
"""
# Innhold, gaming, J 8-12*
# Innhold, gaming, G 8-12*

# Det samme men med inhold mote

# Innhold, mote, J 8-12
# Innhold, mote, J 8-12



import os
import json
from api.create_session import session, ask_without_resonator

def fetch_content_from_file(session_name):
    file_path = f"source/api/session/{session_name}/resonator_response.jsonl"

    with open(file_path, 'r') as file:
        data = json.load(file)
        content = data["choices"][0]["message"]["content"]
    return content

def save_single_answer_to_file(question, session_name):
    content = fetch_content_from_file(session_name)

    with open("answers.txt", 'a', encoding='utf-8') as file:  # 'a' flag means append
        file.write(f"Question: {question}\n")
        file.write(f"{session_name}: {content}\n\n")

def create_sessions_from_questions(questions: dict):
    for question, session_names in questions.items():
        for session_name in session_names:
            session(question, session_name)
            save_single_answer_to_file(question, session_name)

if __name__ == "__main__":
    # questions_set = {
    # "Bruker du plattformen Discord? Begrun svaret (hold begrunnelsen kort) og svar endelig svar er [ja] eller [nei]." :
    # [
    #     "session_j9-11",
    #     "session_g9-11",
    # ],

    # "Bruker du Facebook? Begrun svaret (hold begrunnelsen kort) og svar ja eller nei." :
    # [
    #     "session_j9-11",
    #     "session_g9-11",
    #     "session_j12-14",
    #     "session_g12-14",
    # ],

    # "Ser du på videoer på internett som handler om gaming? Begrun svaret (hold begrunnelsen kort) og svar endelig svar er [ja] eller [nei]." :
    # [
    #     "session_j8-12",
    #     "session_g8-12",
    # ],

    # "Ser du på innhold som handler om mote? Begrun svaret (hold begrunnelsen kort) og svar endelig svar er [ja] eller [nei]." :
    # [
    #     "session_j8-12",
    #     "session_g8-12",
    # ]
    # }
    # create_sessions_from_questions(questions_set)
    questions = [
    "Bruker du plattformen Discord? Begrun svaret (hold begrunnelsen kort) og svar endelig svar er [ja] eller [nei]." ,
    "Bruker du Facebook? Begrun svaret (hold begrunnelsen kort) og svar ja eller nei." ,
    "Ser du på videoer på internett som handler om gaming? Begrun svaret (hold begrunnelsen kort) og svar endelig svar er [ja] eller [nei]."
    ]
    question = "Ser du på innhold som handler om mote? Begrun svaret (hold begrunnelsen kort) og svar endelig svar er [ja] eller [nei]."

    session_name = "session_test_fittest_group"
    

    # for question in questions:
    answers = ask_without_resonator(question, session_name)
