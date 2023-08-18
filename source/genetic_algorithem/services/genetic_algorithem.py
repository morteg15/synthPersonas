from utils.genetic_operations import get_offspring, mutation, update_fitness, get_avrage_fitness
from utils.visualization import get_interest_distribution, print_top_personas
from deap import tools
import copy

def ga(config, toolbox):
    pop = toolbox.population(n=config["population_size"])
    ngen, crossover_probability, mutation_probability = config["generations"], config["crossover_probability"], config["mutation_probability"]
    elite_size = config["elite_size"]
    parents_size = int((len(pop)- elite_size)/2)
    # toolbox.register("select", tools.selTournament, tournsize=config["tournament_size"])

    # Lists to store data for visualization
    interest_distributions = []
    avg_fitnesses = []

    pop = update_fitness(pop, toolbox)
    for gen in range(ngen):
        # print_top_personas(pop, elite_size)
        # Visualizations
        old_pop = copy.deepcopy(pop)
        interest_distributions.append(get_interest_distribution(pop))
        avg_fitnesses.append(get_avrage_fitness(pop))
        
        # elites = copy.deepcopy(tools.selBest(pop, elite_size))
        elites = copy.deepcopy(toolbox.select(pop, elite_size))
        parents = copy.deepcopy(toolbox.select(pop, parents_size))
        offspring = get_offspring(parents, len(pop), crossover_probability, toolbox)
        mutated_offspring =  mutation(offspring, mutation_probability, toolbox)
        # mutated_offspring = offspring

        # Merge the elites and offspring    
        pop = mutated_offspring + elites

        # Re-evaluate changed individuals
        invalids = [ind for ind in pop if not ind.fitness.valid]
        valids = [ind for ind in pop if ind.fitness.valid]
        pop = update_fitness(invalids, toolbox) + valids
       

    return pop, interest_distributions, avg_fitnesses
