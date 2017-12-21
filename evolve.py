# Copyright (C) 2011 Joe Jacob <joe_jacob04@yahoo.com>

# This Source Code Form is subject to the terms of
# the Mozilla Public License, v. 2.0. If a copy of
# the MPL was not distributed with this file, You
# can obtain one at http://mozilla.org/MPL/2.0/.

import random
import math
import logging

class Evolve:
    '''
    Defines the class for genetic operations.
    '''
    
    def __init__(self, crossover=0.7, mutation=0.01, bits=8,
    individuals=10, log=True):
        self.crossover_rate = crossover
        self.mutation_rate = mutation
        self.bit_length = bits
        self.individuals = individuals
        self.data = []
        self.fitness = []
        self.log = log
        if self.log:
            LOG_FILENAME = "evolve.log"
            logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO, filemode='w')


    def generate_population(self, data_list):
        '''
        Generates a set of random individuals from list of data
        '''
        for i in range(0, self.individuals):
            self.data.append(random.choice(data_list))
            self.fitness.append(0.0)
        return i
        
    def assign_fitness(self, target):
        '''
        Assigns fitness to each individual in the population.
        '''
        total_fitness = 0
        for individual in range(0, self.individuals):
            try:
                difference = float(target-self.data[individual])
                self.fitness[individual] = 1.0 / math.fabs(difference)
            except ZeroDivisionError:
                self.fitness[individual] = -777
            total_fitness += self.fitness[individual]
        return total_fitness

    def to_binary(self, individual):
        '''
        Converts a decimal to binary string
        '''
        return "".join([str((individual >> y) & 1) \
        for y in range(self.bit_length-1, -1, -1)])

    def select_individual(self, total_fitness):
        '''
        Selects an individual from the population for next generation
        '''
       
        slice_point = random.uniform(0, total_fitness)
        fitness_now = 0
        for fitness_value in self.fitness:
            fitness_now += fitness_value
            if fitness_now >= slice_point:
                position = self.fitness.index(fitness_value)
                individual = self.to_binary(self.data[position])
                return individual

    def crossover(self, individual1, individual2):
        '''
        Performs crossover between two individuals
        '''
        if random.random() < self.crossover_rate:
            pivot = random.randint(1, self.bit_length/2)
            child1 = individual1[:pivot] + \
            individual2[pivot:]
            child2 = individual2[:pivot] + \
            individual1[pivot:]
            if self.log:
                logging.info('Crossover on: %s %s at %d', individual1, individual2, pivot)
            return (child1, child2)
        return (individual1, individual2)

    def mutate(self, individual):
        '''
        Performs mutation on the individual
        '''
        mutant = ''
        for bit in individual:
            if random.random() < self.mutation_rate:
                if bit == '0':
                    mutant += '1'
                else:
                    mutant += '0'
            else:
                mutant += bit
        if self.log:
                    logging.info('Mutation: %s', individual)
        return mutant
        
