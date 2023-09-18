from ga_code.utils.genetic_operations import (
    get_offspring, mutation_group, update_fitness, 
    get_avrage_fitness, update_fitness_group
)
from ga_code.utils.visualization import get_interest_distribution_group
from deap.tools import selBest
import copy

MAX_GENERATIONS_WITHOUT_IMPROVEMENT = 4  # Constant defined outside the function

def ga(config, toolbox):
    pop = initialize_population(config, toolbox)
    ngen = config["generations"]
    
    interest_distributions = []  # List to store interest distributions
    avg_fitnesses = []  # List to store average fitnesses
    dev_fitnesses = []  # List to store average fitnesses
    
    for gen in range(ngen):
        pop, avg_fitness, dev_avrage = process_generation(gen, ngen, pop, config, toolbox)
        # dev_avrage = toolbox.dev_evaluate(pop)  # Evaluate the population using the dev_evaluate function in the toolbox.
        # toolbox.
        
        interest_distributions.append(get_interest_distribution_group(pop))  # Assuming you have this function available
        avg_fitnesses.append(avg_fitness)
        dev_fitnesses.append(dev_avrage)
        if should_stop_early(avg_fitness, config):
            print("Stopping early due to lack of improvement.")
            break

    return pop, interest_distributions, avg_fitnesses, dev_fitnesses


def initialize_population(config, toolbox):
    """Initialize the population and update its fitness."""
    pop = toolbox.population(n=config["population_size"])
    return update_fitness_group(pop, toolbox)

def process_generation(gen, ngen, pop, config, toolbox):
    """Process one generation and return the updated population and average fitness."""
    print_interest_distribution(gen, ngen, pop)
    best_ind = toolbox.select(pop, 1)[0]
    avg_fitness = get_avrage_fitness(pop)
    dev_avrage = toolbox.evaluate_dev(best_ind)
    print_generation_stats(gen, avg_fitness,dev_avrage, pop)
    
    elites, parents = select_individuals(pop, config, toolbox)
    offspring = create_offspring(parents, config, toolbox)
    
    pop = offspring + elites
    return update_fitness_group(pop, toolbox), avg_fitness, dev_avrage

def print_interest_distribution(gen, ngen, pop):
    """Print the interest distribution for specific generations."""
    if gen in [0, ngen//2, ngen-1]:
        print(f"Interest distribution at generation {gen}:")
        for interest, count in get_interest_distribution_group(pop).items():
            print(f"{interest}: {count}")
        print("-" * 50)

def print_generation_stats(gen, avg_fitness,dev_avrage, pop):
    """Print stats for the current generation."""
   
    birds_interest_count = get_interest_distribution_group(pop)
    print(f"Generation {gen}: Average fitness: {avg_fitness} Dev fitness {dev_avrage},  len(pop): {len(pop)}")

def select_individuals(pop, config, toolbox):
    """Select elites and parents from the population."""
    elite_size = config["elite_size"]
    parents_size = (config["population_size"] - elite_size) // 2
    
    elites = copy.deepcopy(selBest(pop, elite_size))
    parents = copy.deepcopy(toolbox.select(pop, parents_size))
    
    print(f"Number of elites: {len(elites)}, Number of parents: {len(parents)}")
    return elites, parents

def create_offspring(parents, config, toolbox):
    """Create offspring from parents."""
    crossover_probability = config["crossover_probability"]
    mutation_probability = config["mutation_probability"]
    
    offspring = get_offspring(parents, config["population_size"] - config["elite_size"], crossover_probability, toolbox)
    return mutation_group(offspring, mutation_probability, toolbox)

def should_stop_early(avg_fitness, config):
    """Determine if the algorithm should stop early."""
    if avg_fitness > config.get('best_avg_fitness_so_far', float('-inf')):
        config['best_avg_fitness_so_far'] = avg_fitness
        config['generations_without_improvement'] = 0
    else:
        config['generations_without_improvement'] += 1

    return config['generations_without_improvement'] >= MAX_GENERATIONS_WITHOUT_IMPROVEMENT
