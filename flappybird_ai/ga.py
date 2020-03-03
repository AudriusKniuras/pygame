import bird
import random

def calculateFitness(saved_birds):
    sum = 0
    for bird in saved_birds:
        sum += bird.score

    for bird in saved_birds:
        # noramlize fitness values
        bird.fitness = bird.score / sum
    return saved_birds


def pickOne(screen, saved_birds):
    index = 0
    r = random.random()

    while r > 0:
        r = r - saved_birds[index].fitness
        index += 1
    index -= 1

    bird_parent = saved_birds[index]
    child = bird.Bird(screen, bird_parent.brain)
    child.mutate()
    return child

# def pickOne(screen, saved_birds):
#     bird_parent = random.choice(saved_birds)
#     child = bird.Bird(screen, bird_parent.brain)
#     child.mutate()
#     return child


def nextGeneration(screen, birds_arr, pop, saved_birds):
    saved_birds = calculateFitness(saved_birds)
    new_gen_birds = []

    for i in range(pop):
        new_gen_birds.append(pickOne(screen, saved_birds))
    
    # saved_birds = []
    return new_gen_birds