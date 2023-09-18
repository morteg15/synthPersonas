import json
from deap import base, creator, tools
from model.persona_attributes import random_persona, ATTRIBUTES
from utils.genetic_operations import custom_crossover, custom_mutation, custom_selection
from utils.fittnes_function import evaluate
from utils.visualization import (
    plot_avg_fitness,
    plot_interest_distribution,
    compute_interest_distribution,
)
from services.genetic_algorithem import ga

creator.create("Fitness", base.Fitness, weights=(1.0,))  # Maximize fitness
creator.create("Individual", list, fitness=creator.Fitness)

toolbox = base.Toolbox()
toolbox.register("persona_attributes", random_persona)
toolbox.register(
    "individual", tools.initIterate, creator.Individual, toolbox.persona_attributes
)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("select", custom_selection)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", custom_crossover)
toolbox.register(
    "mutate",
    custom_mutation,
    ATTRIBUTES
)
   


def main(config, toolbox):
    result_pop, interest_distributions, avg_fitnesses = ga(config, toolbox)
    plot_interest_distribution(interest_distributions)
    plot_avg_fitness(avg_fitnesses)

    top_personas = tools.selBest(result_pop, config["elite_size"])
    for persona in top_personas:
        print(persona)

    final_distribution = compute_interest_distribution(result_pop)
    print(f"Final distribution of 'Birds' interest: {final_distribution * 100:.2f}%")
    print(f"fittest individual: {tools.selBest(result_pop, 1)}")
    print(f"population size: {config['population_size']}")
    print(f"number of generations: {config['generations']}")
    print(f"final population: {len(result_pop)}")

if __name__ == "__main__":
    # Load the configuration
    with open("source\\genetic_algorithem\\config.cfg", "r") as file:
        config = json.load(file)
    main(config, toolbox)

