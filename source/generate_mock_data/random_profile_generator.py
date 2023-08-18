import toml
import random

def generate_person():
    names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Green"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    states = ["NY", "CA", "IL", "TX", "AZ"]
    countries = ["USA", "Canada", "UK", "Australia", "Germany"]
    hobbies = ["Reading", "Cycling", "Gaming", "Swimming", "Cooking"]
    languages = ["English", "Spanish", "French", "German", "Mandarin"]
    books = ["To Kill a Mockingbird", "1984", "The Catcher in the Rye", "Pride and Prejudice", "Moby Dick"]

    person = {
        "name": random.choice(names),
        "age": {
            "years": random.randint(18, 60)
        },
        "location": {
            "city": random.choice(cities),
            "state": random.choice(states),
            "country": random.choice(countries)
        },
        "interests": {
            "hobbies": random.sample(hobbies, k=3), # Pick 3 random hobbies
            "languages": random.sample(languages, k=2), # Pick 2 random languages
            "favorite_books": random.sample(books, k=3) # Pick 3 random books
        }
    }

    return person

def save_to_toml(person_data, filename):
    with open(filename, 'w') as file:
        toml.dump(person_data, file)

if __name__ == "__main__":
    for i in range(100):
        random_person = generate_person()
        profile_path = "data/profiles/"
        save_to_toml(random_person, profile_path + f"person_{i}.toml")
