import unittest
from pattern_matching import data_generator
from pattern_matching import constants


class DataGeneratorTest(unittest.TestCase):
    def test_data_generator_with_empty_list(self):
        N = 0
        random_list = data_generator.generate_patterns_data(N, 0.1)[0]
        self.assertTrue(N == len(random_list))
        pass

    def test_data_generator_with_1(self):
        N = 1
        random_list = data_generator.generate_patterns_data(N, 0.1)[0]
        self.assertTrue(N == len(random_list))
        pass

    def test_data_generator_with_2(self):
        N = 2
        random_list = data_generator.generate_patterns_data(N, 0.1)[0]
        self.assertTrue(N == len(random_list))
        pass

if __name__ == "__main__":
    unittest.main()
