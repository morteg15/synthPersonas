import json

# Configuration
CONFIG = {
    "question": "What is your opinion on topic X?",  # Specify the question here
    "mode": "opinion",  # Change to "answer" for the other mode
    "output_file": "output.jsonl"
}

def generate_jsonl_structure(question, user_messages, outputfile, mode="opinion"):
    """
    Generate a JSONL structure based on a question, user messages, and a mode.

    Parameters:
    - question (str): The question that user messages are responding to.
    - user_messages (list): A list of messages from the user.
    - mode (str): Either "opinion" or "answer".

    Returns:
    - dict: The generated JSONL structure.
    """
    
    # Validate mode
    if mode not in ["opinion", "answer"]:
        raise ValueError("Mode should be either 'opinion' or 'answer'.")

    # Base structure
    jsonl_structure = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": question},  # Question as the first system message
            {"role": "system", "content": "I am a resonator. I read through many messages and find the general opinion or the correct result."}
        ]
    }

    # Add user messages
    for message in user_messages:
        jsonl_structure["messages"].append({"role": "user", "content": message})

    # Add system response based on mode
    if mode == "opinion":
        jsonl_structure["messages"].append({"role": "user", "content": "Based on the messages, the general opinion is [summary/opinion]."})
    else:
        jsonl_structure["messages"].append({"role": "user", "content": "Based on the messages, the most likely correct result is [result]."})



    # Save to file
    with open(outputfile, 'w') as f:
        f.write(json.dumps(jsonl_structure, indent=2))

    print(f"Resonator saved to " + outputfile)

    # return jsonl_structure

# user_messages = []
# responses = read_responses("source\\api\\session\\session_1.jsonl")
# for response in responses:
#     user_messages.append(response[-1])
    

# # # Example usage
# # user_messages = ["This is the first message.", "Here's another message.", "And one more for good measure."]
# jsonl_structure = generate_jsonl_structure(CONFIG["question"], user_messages, CONFIG["mode"])

# # Save to file
# with open(CONFIG["output_file"], 'w') as f:
#     f.write(json.dumps(jsonl_structure, indent=2))

# print(f"Resonator saved to {CONFIG['output_file']}")
