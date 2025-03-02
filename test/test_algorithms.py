import unittest
from pattern_matching import algorithms
from pattern_matching import data_generator
from pattern_matching import constants

test_cases = [
    ["ABABABABABAB", "ABAB"],  
    ["XYZXYZXYZXYZ", "XYZX"],  
    ["ABCDEFGHIJKL", "DEFG"],  
    ["AABCAAADAAAB", "AA"],    
    ["MISSISSIPPI", "ISS"],   
    ["HELLO WORLD", "WORLD"], 
    ["1234567890", "678"],  
    ["abcdeabcdeabcde", "cde"], 
    ["abcdefgh", "xyz"],       
    ["aaaaaa", "aaa"]    
]

expected_results = [
    [0, 2, 4, 6, 8],  
    [0, 3, 6],   
    [3],             
    [0, 4, 5, 8, 9],  
    [1, 4],           
    [6],             
    [5],              
    [2, 7, 12],       
    [],              
    [0, 1, 2, 3]
]
class AlgorithmsTests(unittest.TestCase):
    def test_search_brute_force(self):
        for i in range(len(test_cases)):
            text, pattern = test_cases[i]
            result = algorithms.search_brute_force(text, pattern)
            self.assertEqual(result, expected_results[i])

    def test_search_morris_pratt(self):
        for i in range(len(test_cases)):
            text, pattern = test_cases[i]
            result = algorithms.morris_pratt_algorithm(text, pattern)
            self.assertEqual(result, expected_results[i])

    def test_search_with_automaton(self):
        for i in range(len(test_cases)):
            text, pattern = test_cases[i]
            result = algorithms.search_with_automaton(text, pattern)
            self.assertEqual(result, expected_results[i])

if __name__ == "__main__":
    unittest.main()
