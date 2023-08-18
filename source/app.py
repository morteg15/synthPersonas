from flask import Flask, render_template, send_from_directory
import toml
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# remove source from path
BASE_DIR = os.path.dirname(BASE_DIR)
PROFILE_PATH = os.path.join(BASE_DIR,  "data", "profiles")
PICTURE_DIR = os.path.join(BASE_DIR,  "data", "profilepictures")

@app.route('/profile/<int:profile_id>')
def display_profile(profile_id):
    profile_file = os.path.join(PROFILE_PATH, f"person_{profile_id}.toml")
    picture_file = f"profilepicture_{profile_id}.jpg"  # Assuming .jpg format, change if different

    # # Ensure valid profile id
    # if not os.path.exists(profile_file):
    #     return "Profile not found! im here" + str(profile_file) + str(picture_file), 404

    person = toml.load(profile_file)
    return render_template('profile.html', person=person, picture_file=picture_file, profile_id=profile_id)

@app.route('/profile_picture/<filename>')
def serve_picture(filename):
    return send_from_directory(PICTURE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
