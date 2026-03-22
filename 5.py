import random

# população inicial
population = [random.sample(range(1,6), 5) for _ in range(10)]

def fitness(individual):
    return sum(individual)  # simulação de custo

def select(population):
    return sorted(population, key=fitness)[:5]

def crossover(p1, p2):
    point = random.randint(1,3)
    return p1[:point] + p2[point:]

def mutate(individual):
    i, j = random.sample(range(len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

# evolução
for generation in range(10):
    selected = select(population)
    new_population = []

    for _ in range(10):
        p1, p2 = random.sample(selected, 2)
        child = crossover(p1, p2)

        if random.random() < 0.3:
            child = mutate(child)

        new_population.append(child)

    population = new_population

best = min(population, key=fitness)
print("Best solution:", best, "Cost:", fitness(best))
