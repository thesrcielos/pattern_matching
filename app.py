import sys
from pattern_matching import algorithms
from pattern_matching import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 10000
    maximum_size = 50000
    step = 5000
    samples_by_size = 7
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Brute Force | Morris Pratt | Search with Automaton")
    for row in table:
        print(row)
