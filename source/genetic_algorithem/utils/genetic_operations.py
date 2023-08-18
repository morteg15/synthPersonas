import random
import copy
from model.persona_attributes import ATTRIBUTES


def custom_crossover(ind1, ind2):
    length = len(ind1)
    cx_point = random.randint(0, length - 1)
    ind1[cx_point:], ind2[cx_point:] = ind2[cx_point:], ind1[cx_point:]
    return ind1, ind2


def custom_mutation(ATTRIBUTES, ind):
    mutation_point = random.randint(0, len(ATTRIBUTES) - 1)
    ind[mutation_point] = random.choice(ATTRIBUTES[mutation_point])
    return ind

def custom_selection(population, k):
    population = copy.deepcopy(population)
    # find the best k individuals with the highest fitness
    return sorted(population, key=lambda x: x.fitness.values[0], reverse=True)[:k]

def update_fitness(pop, toolbox):
    evaluated_pop = copy.deepcopy(pop)
    fitnesses = list(map(toolbox.evaluate, evaluated_pop))
    for ind, fit in zip(evaluated_pop, fitnesses):
        ind.fitness.values = fit
    return evaluated_pop


def get_avrage_fitness(pop):
    # Calculate average fitness for the current generation and store it
    fitnesses = [ind.fitness.values[0] for ind in pop]
    return sum(fitnesses) / len(pop)


def get_offspring(pop, size, crossover_probability, toolbox):
    # double the size of the parents
        
    parents = list(copy.deepcopy(pop))
    offspring = []

    for _ in range(size // 2):  # size//2 pairs will give 'size' offspring
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        
        # # Ensure different parents are selected for crossover
        # while parent1 == parent2:
        #     parent2 = random.choice(parents)
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        if random.random() < crossover_probability:
            child1, child2 = toolbox.mate(child1, child2)
            offspring.extend([child1, child2])
        else:
            offspring.extend([child1, child2])

    return offspring
    # return parents


def mutation(offspring, mutation_probability, toolbox):
    #make a copy of the offspring
    mutated_offspring = copy.deepcopy(offspring)
    counter = 0
    # Mutation
    for mutant in mutated_offspring:
        if random.random() < mutation_probability:
            # mutant = toolbox.mutate(mutant)
            mutation_point = random.randint(0, len(ATTRIBUTES) - 1)
            mutant[mutation_point] = random.choice(ATTRIBUTES[mutation_point])
            del mutant.fitness.values
            counter += 1
    print("Number of mutations:", counter)
    return mutated_offspring
