from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/survey', methods=['POST'])
def survey():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    location = data.get('location')
    interest = data.get('interest')
    
    # For simplicity, let's assume our survey asks if they like the new exhibit based on their interest
    if interest == "Birds":
        answer = "Yes"
    else:
        answer = "No"
    
    # You can make it more complex by taking into account other attributes
    
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
