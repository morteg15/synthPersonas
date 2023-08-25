import os
import json

# Paths to your folders
PROFILE_FOLDER = 'data\profiles'
SESSION_FOLDER = 'source\\api\session\\session_2'
RESPONSE_FILENAME = "users_response.jsonl"

def get_all_profiles():
    profiles = {}
    for profile_file in os.listdir(PROFILE_FOLDER):
        with open(os.path.join(PROFILE_FOLDER, profile_file), 'r') as f:
            profiles[profile_file] = f.read()
    return profiles

def id_the_responses(responses, profiles):
    profile_dict = {}
    for response in responses:
        for message in response[0]['messages']:
            if message['role'] == "system":
                for filename, profile_content in profiles.items():
                    if profile_content in message['content']:
                        profile_dict[filename] = response
                        break
    return profile_dict

def extract_question_and_answer(response):
    question = response[0]['messages'][-1]['content']
    answer = response[1]['choices'][0]['message']['content']
    return question, answer

def main():
    with open(os.path.join(SESSION_FOLDER, RESPONSE_FILENAME), 'r') as f:
        profiles = get_all_profiles()
        responses = [json.loads(line) for line in f]
        profiles_dict = id_the_responses(responses, profiles)

        for filename, response in profiles_dict.items():
            question, answer = extract_question_and_answer(response)
            updated_profile = profiles[filename] + f"\n\n[question_and_answer]\nquestion = \"{question}\"\nanswer = \"{answer}\""
            
            # Save the updated profile
            with open(os.path.join("test_folder", filename), 'w') as f:
                f.write(updated_profile)

if __name__ == "__main__":
    main()
