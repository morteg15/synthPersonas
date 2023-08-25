import os
import json
from api.utils.read_responses import get_all_profiles, id_the_responses, get_question_and_answer


def update_profiles(session_name, new_session: bool = False):
    session_path = os.path.join('source\\api\session', session_name)
    response_filename = os.path.join(session_path, "users_response.jsonl")
    with open(response_filename, 'r') as f:
        profiles = get_all_profiles(session_path, new_session)
        responses = [json.loads(line) for line in f]
        profiles_dict = id_the_responses(responses, profiles)

        for filename, response in profiles_dict.items():
            question, answer = get_question_and_answer(response)
        
            updated_profile = profiles[filename] + f"\n\n[[question_and_answer]]\nquestion = \"{question}\"\nanswer = \"{answer}\""
            
            # if folder do not exist create it
            if not os.path.exists(os.path.join(session_path + "\\profiles")):
                os.mkdir(os.path.join(session_path + "\\profiles"))
            # Save the updated profile
            with open(os.path.join(session_path + "\\profiles", filename), 'w') as f:
                f.write(updated_profile)

