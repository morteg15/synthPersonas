# import requests
# from functools import lru_cache

# @lru_cache(maxsize=None)  # Unbounded cache. Adjust `maxsize` if needed.
# def _cached_request(name, age, location, interest):
#     response = requests.post('http://127.0.0.1:5000/survey', json={
#         "name": name,
#         "age": age,
#         "location": location,
#         "interest": interest
#     })
#     return response.json().get('answer')

# def evaluate(individual):
#     name, age, location, interest = individual

#     # Use the cached request function
#     answer = _cached_request(name, age, location, interest)
    
#     if answer == "Yes":
#         fitness = 1
#     else:
#         fitness = 0

#     return fitness,



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
