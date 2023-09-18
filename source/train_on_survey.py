import os
import random
import shutil
import json

from api.create_session import ask_without_resonator, create_session
from api.update_session_profiles import update_profiles
# from utils.create_profiles import create_random_personas
from utils.create_profiles_adults import create_random_personas
from ga_code.run_group_ga import run_ga_group
from utils.check_answers import count_answers_in_toml, calculate_error_margin

# Load the configuration from the JSON file
with open("source/config.cfg", "r", encoding="utf8") as file:
    config = json.load(file)


# Load the Survey data
survey_path =  "data\gss\survey_asked.json"
with open(survey_path, "r", encoding="utf8") as file:
    survey = json.load(file)


session_name = config["session"]["session_name"]
session_path = os.path.join("source", "api", "session_ga", session_name)
profile_path = os.path.join(session_path, "profiles")
save_path = os.path.join(session_path, "fittest_group")


def hide_question(survey, num_to_hide=5):
    hidden_question = {}
    
    # Randomly select keys to hide
    keys_to_hide = random.sample(list(survey.keys()), num_to_hide)
    
    for key in keys_to_hide:
        hidden_question[key] = survey[key]
        del survey[key]
    
    return hidden_question


def hide_last_questions(survey, num_to_hide=1):
    hidden_questions = {}
    
    # Get the last 'num_to_hide' keys from the survey
    keys_to_hide = list(survey.keys())[-num_to_hide:]
    
    for key in keys_to_hide:
        hidden_questions[key] = survey[key]
        del survey[key]
    
    return hidden_questions
if __name__ == "__main__":
    # print("Starting with creating a session")
    # create_session(session_path)
    # create_random_personas(
    #     session_path,
    #     pop_number=200,
    #     gender=config["session"]["gender"],
    #     age_range=config["session"]["age_range"],
    # )
  
    # print("Finished creating a session")
    # print("Starting with asking the questions")

    # for question in survey:
    #     answers = ask_without_resonator(question, session_path) 

    # update_profiles(session_path)

    # Hide a question
    # key = "Ser du på videoer på internett som handler om gaming? Begrun svaret først slik som personas ville svart (hold begrunnelsen kort) og derreter svar endelig svar er [ja] eller [nei]."
    hidden_questions = hide_question(survey, num_to_hide=5)

    print("Starting with running the genetic algorithm")
    run_ga_group(survey, hidden_questions, config["genetic_algorithm"], profile_path, save_path)
    print("Finished running the genetic algorithm")

    random_profiles = random.sample(os.listdir(profile_path), config["genetic_algorithm"]["group_size"])
    random_profiles_path = os.path.join(session_path, "random_profiles")

    # Delete the folder if it already exists
    if os.path.exists(random_profiles_path):
        shutil.rmtree(random_profiles_path)
    os.mkdir(random_profiles_path)

    for profile in random_profiles:
        shutil.copyfile(
            os.path.join(profile_path, profile),
            os.path.join(random_profiles_path, profile)
        )

    random_profiles_count = count_answers_in_toml(random_profiles_path, hidden_questions)
    random_profiles_error, random_avg_error = calculate_error_margin(hidden_questions, random_profiles_count)

    answer_count = count_answers_in_toml(save_path, hidden_questions)
    _, avg_error = calculate_error_margin(hidden_questions, answer_count)

    print("Answers:", answer_count)
    print("The real distribution:", hidden_questions)
    print("Errors:", avg_error)
    print("Improvement over random profiles:", random_avg_error - avg_error)
