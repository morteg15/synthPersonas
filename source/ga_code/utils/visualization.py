
import matplotlib.pyplot as plt
from deap import tools

import matplotlib.pyplot as plt

def plot_avg_fitness(fitnesses_over_generations, dev_fitnesses_over_generations):
    plt.plot(fitnesses_over_generations, label='Fitness')
    plt.plot(dev_fitnesses_over_generations, label='Dev Fitness', linestyle='--')  # Added this line
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness Over Generations')
    plt.legend()  # Added this line to show a legend
    plt.show()


def plot_interest_distribution(interest_distributions):
    generations = list(range(len(interest_distributions)))

    # Get all unique interests across generations
    all_interests = set()
    for dist in interest_distributions:
        all_interests.update(dist.keys())

    # Now plot for each interest
    for interest in all_interests:
        plt.plot(generations, [gen_dist.get(interest, 0) for gen_dist in interest_distributions], label=interest)
    
    plt.xlabel('Generation')
    plt.ylabel('Count')
    plt.title('Distribution of Interests Over Generations')
    plt.legend()
    plt.show()


known_interests = ['Reptiles', 'Mammals', 'Fish', 'Birds']

def plot_interest_distribution_groupwise(interest_distributions):
    generations = list(range(len(interest_distributions)))

    # Get all unique interests/attributes across generations
    all_interests = set()
    for dist in interest_distributions:
        all_interests.update(dist.keys())

    print(f"All interests/attributes found: {all_interests}")

    # Filter out non-interest keys (like names or numbers which don't seem to be interests)
    valid_interests = [interest for interest in all_interests if interest in known_interests]

    print(f"Valid interests to be plotted: {valid_interests}")

    # Now plot for each interest
    for interest in valid_interests:
        plt.plot(generations, [gen_dist.get(interest, 0) for gen_dist in interest_distributions], label=interest)

    plt.xlabel('Generation')
    plt.ylabel('Count')
    plt.title('Distribution of Interests Over Generations')
    plt.legend()
    plt.show()


def get_interest_distribution(population):
    interests_count = {}
    for individual in population:
        individual_interests = individual[3]  # Assuming interests are stored at index 3 in each individual
        if isinstance(individual_interests, str):  # In case the interests are stored as a single string
            individual_interests = [individual_interests]

        for interest in individual_interests:
            interests_count[interest] = interests_count.get(interest, 0) + 1
    return interests_count

def get_interest_distribution_group(population):
    interests_count = {}

    # Loop through each group in the population
    for group in population:
        # Loop through each individual/persona in the group
        for individual in group:
            individual_interests = individual["interests"]["hobbies"]  # Assuming interests are stored at index 3 in each individual
            
            # In case the interests are stored as a single string
            if isinstance(individual_interests, str):
                individual_interests = [individual_interests]

            # Update the interests count
            for interest in individual_interests:
                interests_count[interest] = interests_count.get(interest, 0) + 1

    return interests_count



def compute_interest_distribution(population):
    """Compute the distribution of the 'Birds' interest among the population."""
    total_count = len(population)
    birds_count = sum(1 for individual in population if individual[3] == "Birds")
    return birds_count / total_count


def print_top_personas(pop, elite_size):
    top_personas = tools.selBest(pop, elite_size)
    # Print the top personas
    for persona in top_personas:
        print(persona)
    print("-------------------------------------")
