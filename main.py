# Copyright (C) 2011 Joe Jacob <joe_jacob04@yahoo.com>

# This Source Code Form is subject to the terms of
# the Mozilla Public License, v. 2.0. If a copy of
# the MPL was not distributed with this file, You
# can obtain one at http://mozilla.org/MPL/2.0/.

import evolve

if __name__ == '__main__':
    data = range(0,800)
    population = evolve.Evolve(mutation=0.1,individuals=10,bits=7)
    target = [1,67,34,22,25]
    generation = 0
    result=[]
    
    for target_no in target:
        population.generate_population(data)
        fitness = population.assign_fitness(target_no)
        while fitness > 0:
            count = 0
            temp = []
            temp_fitness = []
            
            while count < (population.individuals/2):
                individual1 = population.select_individual(fitness)
                individual2 = population.select_individual(fitness)
                (child1, child2)=population.crossover(individual1, individual2)
                mutant1 = int(population.mutate(child1), 2)
                mutant2 = int(population.mutate(child2), 2)
                temp.append(mutant1)
                temp.append(mutant2)
                temp_fitness.append(0.0)
                temp_fitness.append(0.0)
                count += 1
            population.data = temp[:]
            population.fitness = temp_fitness[:]
            fitness = population.assign_fitness(target_no)
            generation += 1
            
        if target_no in population.data:
            result.append(str(target_no))
    print 'Total Generations:', generation
    print ' '.join(result)
