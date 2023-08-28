import toml
import random
from norwegian_lists import movies, books, intresser, norwegianCounties, norwegianLivingConditions, Influencers, boy_names, girl_names, last_names

def get_random_number(min, max):
    return random.randint(min, max)

def generate_person():
    gender = random.choice(["male", "female"])
    if gender == "male":
        first_name = random.choice(boy_names)
    else:
        first_name = random.choice(girl_names)
    
    full_name = first_name + " " + random.choice(last_names)
    
    person = {
        "name": full_name,
        "gender": gender,
        "age": {
            "years": random.randint(7, 18)
        },
        "location": {
            "fylke": random.choice(norwegianCounties),
            "living_condition": random.choice(norwegianLivingConditions)
        },
        "interests": {
            "hobbies": random.sample(intresser, k=get_random_number(0,5)), # Velg 3 tilfeldige interesser
            "languages": ["Norsk"], # Antatt at alle snakker norsk
            "favorite_books": random.sample(books, k=get_random_number(0,5)), # Velg 3 tilfeldige bøker
            "favorite_movies": random.sample(movies, k=get_random_number(0,5)), # Velg 3 tilfeldige filmer
            "favorite_influencers": random.sample(Influencers, k=get_random_number(0,5)) # Velg 2 tilfeldige influencere
        },
        "personality": {
            "openness": random.randint(0, 100), # Score fra 0 til 100
            "conscientiousness": random.randint(0, 100),
            "extraversion": random.randint(0, 100),
            "agreeableness": random.randint(0, 100),
            "neuroticism": random.randint(0, 100)
        }
    }

    return person

def save_to_toml(person_data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        toml.dump(person_data, file)


if __name__ == "__main__":
    for i in range(100):
        random_person = generate_person()
        profile_path = "data/profiles/"
        save_to_toml(random_person, profile_path + f"person_{i}.toml")
