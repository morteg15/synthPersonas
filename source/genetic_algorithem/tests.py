
from genetic_algorithem import toolbox, evaluate
import json
import random
from deap import base, creator, tools
from model.persona_attributes import random_persona, NAMES, AGES, LOCATIONS, INTERESTS
from utils.genetic_operations import custom_crossover, custom_mutation
from utils.fittnes_function import evaluate

from deap import base, creator, tools

from genetic_algorithem import compute_interest_distribution

def test_evaluate():
    assert evaluate(["John", 25, "USA", "Birds"]) == (1,)
    assert evaluate(["John", 25, "USA", "Fishing"]) == (0,)
    
def test_selection():
    pop = [
        creator.Individual(["John", 25, "USA", "Birds"]),
        creator.Individual(["Jane", 30, "UK", "Fishing"]),
        creator.Individual(["Doe", 28, "CAN", "Birds"]),
        creator.Individual(["Smith", 35, "AUS", "Traveling"])
    ]
    fitnesses = list(map(evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    selected = toolbox.select(pop, 2)
    for ind in selected:
        assert ind[3] == "Birds"

def test_random_persona():
    persona = random_persona()
    assert persona[0] in NAMES
    assert persona[1] in AGES
    assert persona[2] in LOCATIONS
    assert persona[3] in INTERESTS

def test_custom_crossover():
    ind1 = creator.Individual(["John", 25, "USA", "Birds"])
    ind2 = creator.Individual(["Jane", 30, "UK", "Fishing"])
    child1, child2 = custom_crossover(ind1, ind2)
    
    assert child1[0] in [ind1[0], ind2[0]]
    assert child2[0] in [ind1[0], ind2[0]]
    # ... do similar assertions for other attributes if necessary ...
def test_custom_mutation():
    individual = creator.Individual(["John", 25, "USA", "Fishing"])
    toolbox.mutate(individual)
    
    assert individual[0] in NAMES
    assert individual[1] in AGES
    assert individual[2] in LOCATIONS
    assert individual[3] in INTERESTS
def test_compute_interest_distribution():
    pop = [
        creator.Individual(["John", 25, "USA", "Birds"]),
        creator.Individual(["Jane", 30, "UK", "Birds"]),
        creator.Individual(["Doe", 28, "CAN", "Gaming"]),
        creator.Individual(["Smith", 35, "AUS", "Traveling"])
    ]
    
    distribution = compute_interest_distribution(pop)
    assert distribution == 0.5  # 2 out of 4 individuals have "Birds" interest
def test_elite_selection():
    pop = [
        creator.Individual(["John", 25, "USA", "Birds"]),
        creator.Individual(["Jane", 30, "UK", "Fishing"]),
        creator.Individual(["Doe", 28, "CAN", "Birds"]),
        creator.Individual(["Smith", 35, "AUS", "Traveling"])
    ]
    fitnesses = [1, 0, 1, 0]
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = (fit,)
    
    elites = tools.selBest(pop, 2)
    for ind in elites:
        assert ind[3] == "Birds"

#run tests 
test_evaluate()
test_selection()