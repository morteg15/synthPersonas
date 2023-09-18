import os
from deap import base, creator, tools
import toml

from ga_code.model.persona_attributes import get_random_persona
from ga_code.utils.genetic_operations import custom_crossover, custom_mutation, custom_selection
from ga_code.utils.visualization import plot_interest_distribution_groupwise, plot_avg_fitness
from ga_code.services.genetic_algorithem_clean import ga
from ga_code.utils.extract_personas import extract_personas_from_files
from ga_code.utils.fittnes_function import group_evaluate



def save_fittest_group_to_file(fittest_group, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, persona in enumerate(fittest_group):
        file_content = toml.dumps(persona)
        with open(os.path.join(output_folder, f"fittest_persona_{index}.toml"), 'w', encoding="utf8") as file:
            file.write(file_content)


def initialize_toolbox(real_distribution, hidden_distrubution, config, path_to_profiles):
    creator.create("Fitness", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.Fitness)
    toolbox = base.Toolbox()
    toolbox.register("select", custom_selection)
    toolbox.register("evaluate", group_evaluate, real_distributions=real_distribution)
    toolbox.register("evaluate_dev", group_evaluate, real_distributions=hidden_distrubution)
    toolbox.register("mate", custom_crossover)
    toolbox.register("mutate", custom_mutation)

    personas = extract_personas_from_files(path_to_profiles)
    toolbox.register("persona_attributes", get_random_persona, personas)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.persona_attributes, n=config["group_size"])
    toolbox.register("population", tools.initRepeat, list, toolbox.individual, n=config["population_size"])

    return toolbox


def run_ga_group(real_distribution,hidden_distrubution, config, path_to_profiles, save_path):
    toolbox = initialize_toolbox(real_distribution, hidden_distrubution, config, path_to_profiles)
    super_population, interest_distributions, avg_fitnesses, dev_fitnesses = ga(config, toolbox)

    plot_interest_distribution_groupwise(interest_distributions)
    plot_avg_fitness(avg_fitnesses, dev_fitnesses)

    print(f"number of generations: {config['generations']}")
    print(f"total groups in final super population: {len(super_population)}")
    fittest_group = tools.selBest(super_population, 1)[0]
    print(f"fittest group: {fittest_group}")
    save_fittest_group_to_file(fittest_group, save_path)
