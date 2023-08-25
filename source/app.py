from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
import os
import toml
from api.create_session import session
from api.utils.read_responses import get_all_profiles, id_the_updated_responses

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(BASE_DIR)

# Default session path
SESSION_PATH = os.path.join(BASE_DIR, 'source\\api\\session')

PICTURE_DIR = os.path.join(BASE_DIR, "data", "profilepictures")


def load_jsonl(file_path):
    with open(file_path, 'r') as file:
        return [json.loads(line) for line in file]


def extract_question(data):
    for entry in data:
        for message in entry[0]['messages']:
            if message['role'] == 'user':
                return message['content']


def extract_general_opinion(resonor_data):
    return resonor_data[0]['choices'][0]['message']['content']


@app.route('/')
def landing():
    sessions = [s for s in os.listdir(SESSION_PATH) if os.path.isdir(os.path.join(SESSION_PATH, s))]
    if not sessions:
        return render_template('landing.html', sessions=None)
    else:
        return render_template('landing.html', sessions=sessions)

@app.route('/select_session', methods=['POST'])
def select_session():
    selected_session = request.form.get('selected_session')
    return redirect(url_for('index', session_name=selected_session))


@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form.get('question')
    current_session_name = request.form.get('session_name', None)  # Get the current session name from the form
    
    # If there's no current session name, generate a new one
    if not current_session_name:
        sessions = [s for s in os.listdir(SESSION_PATH) if os.path.isdir(os.path.join(SESSION_PATH, s))]
        session_numbers = [int(s.split('_')[-1]) for s in sessions if s.startswith('session_')]
        highest_number = max(session_numbers, default=1)
        current_session_name = f"session_{highest_number}"
        session(question)
    else:
        session(question, current_session_name)
    
    # Redirect to the session page with the current session name
    return redirect(url_for('index', session_name=current_session_name))



@app.route('/index/<session_name>')
def index(session_name):
    current_session_path = os.path.join(SESSION_PATH, session_name)
    user_response = load_jsonl(os.path.join(current_session_path, 'users_response.jsonl'))
    resonor_response = load_jsonl(os.path.join(current_session_path, 'resonator_response.jsonl'))
    question = extract_question(user_response)
    general_opinion = extract_general_opinion(resonor_response)
    profiles = get_all_profiles(current_session_path, new_session = False)
    profiles_dict = id_the_updated_responses(user_response, profiles)
    
    # Pass session_name to the template
    return render_template('index.html', user_data=user_response, question=question, general_opinion=general_opinion, session_name=session_name, profiles_dict=profiles_dict)


# @app.route('/index/<session_name>/profile/<int:profile_id>')
# def display_profile(session_name, profile_id):
#     # Use session_name to locate the correct directory if needed
#     profile_path = os.path.join(SESSION_PATH, session_name, 'profiles')
#     profile_file = os.path.join(profile_path, f"person_{profile_id}.toml")
#     picture_file = f"profilepicture_{profile_id}.jpg"
#     person = toml.load(profile_file)
#     return render_template('profile.html', person=person, picture_file=picture_file, profile_id=profile_id)

@app.route('/index/<session_name>/profile/<int:profile_id>')
def display_profile(session_name, profile_id):
    # Use session_name to locate the correct directory
    profile_path = os.path.join(SESSION_PATH, session_name, 'profiles')
    profile_file = os.path.join(profile_path, f"person_{profile_id}.toml")
    picture_file = f"profilepicture_{profile_id}.jpg"
    person = toml.load(profile_file)
    return render_template('profile.html', person=person, picture_file=picture_file, profile_id=profile_id,  session_name=session_name)


@app.route('/profile_picture/<filename>')
def serve_picture(filename):
    return send_from_directory(PICTURE_DIR, filename)


if __name__ == '__main__':
    app.run(debug=True)
