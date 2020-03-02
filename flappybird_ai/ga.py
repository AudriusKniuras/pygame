import bird
import random

def calculateFitness(birds_arr):
    sum = 0
    for bird in birds:
        sum += bird.score

    for bird in birds:
        # noramlize fitness values
        bird.fitness = bird.score / sum

def pickOne():
    child = random.choice(saved_bird)
    return child


def nextGeneration(screen, birds_arr, pop, saved_birds):

    calculateFitness()
    for i in range(pop):
        birds_arr.append(pickOne(saved_birds))
    return birds_arr