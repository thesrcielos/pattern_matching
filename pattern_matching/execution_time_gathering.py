import time
import tracemalloc
from pattern_matching import algorithms
from pattern_matching import constants
from pattern_matching import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size, two=False):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size, two)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size, two):
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.generate_patterns_data(size))
    if two:
        return [
            take_time_for_algorithm(samples, algorithms.morris_pratt_algorithm),
            take_time_for_algorithm(samples, algorithms.search_with_automaton),
        ]

    return [
        take_time_for_algorithm(samples, algorithms.search_brute_force),
        take_time_for_algorithm(samples, algorithms.morris_pratt_algorithm),
        take_time_for_algorithm(samples, algorithms.search_with_automaton),
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, pattern_matching_approach):
    times = []
    memory_usage = []

    for sample, pattern in samples_array:
        tracemalloc.start()
        start_time = time.time()
        pattern_matching_approach(sample, pattern)
        end_time = time.time()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(int(constants.TIME_MULTIPLIER * (end_time - start_time)))
        memory_usage.append(peak)
    times.sort()
    memory_usage.sort()
    return times[len(times) // 2], memory_usage[len(memory_usage) // 2]
