from ga_code.utils.genetic_operations import get_offspring, mutation_group, update_fitness, get_avrage_fitness, update_fitness_group
from ga_code.utils.visualization import get_interest_distribution_group
from deap import tools
import copy

def ga(config, toolbox):
    best_avg_fitness_so_far = float('-inf')
    generations_without_improvement = 0
    MAX_GENERATIONS_WITHOUT_IMPROVEMENT = 4 # You can adjust this value
    pop = toolbox.population(n=config["population_size"])
    ngen, crossover_probability, mutation_probability = config["generations"], config["crossover_probability"], config["mutation_probability"]
    elite_size = config["elite_size"]
    parents_size = int((len(pop)- elite_size)/2)
    # toolbox.register("select", tools.selTournament, tournsize=config["tournament_size"])

    # Lists to store data for visualization
    interest_distributions = []
    avg_fitnesses = []

    # pop = update_fitness(pop, toolbox)
    pop = update_fitness_group(pop, toolbox)
    for gen in range(ngen):
        if gen in [0, ngen//2, ngen-1]:  # initial, middle, and last generation
            print(f"Interest distribution at generation {gen}:")
            for interest, count in get_interest_distribution_group(pop).items():
                print(f"{interest}: {count}")
            print("-" * 50)  # to separate the distributions for clarity
    
        # Visualizations
        interest_distributions.append(get_interest_distribution_group(pop))
        avg_fitness = get_avrage_fitness(pop)
        avg_fitnesses.append(avg_fitness)
        birds_interest_count = get_interest_distribution_group(pop).get('Birds', 0)
        print(f"Generation {gen}: Average fitness: {avg_fitness}, Birds interest count: {birds_interest_count}")
        
        # elites = copy.deepcopy(tools.selBest(pop, elite_size))
        elites = copy.deepcopy(toolbox.select(pop, elite_size))
        parents = copy.deepcopy(toolbox.select(pop, parents_size))
        print(f"Generation {gen}: Number of elites: {len(elites)}, Number of parents: {len(parents)}")
        # Ensure that the total number of children and elites equals the original population size
        number_of_children = len(pop) - elite_size
        offspring = get_offspring(parents, number_of_children, crossover_probability, toolbox)
        mutated_offspring =  mutation_group(offspring, mutation_probability, toolbox)
        # mutated_offspring = offspring

        # Merge the elites and offspring    
        pop = mutated_offspring + elites

        # Re-evaluate changed individuals
        pop = update_fitness(pop, toolbox)
        # pop = update_fitness(invalids, toolbox) + valids
        if avg_fitness > best_avg_fitness_so_far:
            # 4. Update the best average fitness and reset the counter
            best_avg_fitness_so_far = avg_fitness
            generations_without_improvement = 0
        else:
            # 5. Increment the counter
            generations_without_improvement += 1
        if generations_without_improvement >= MAX_GENERATIONS_WITHOUT_IMPROVEMENT:
            print("Stopping early due to lack of improvement.")
            break
    return pop, interest_distributions, avg_fitnesses
