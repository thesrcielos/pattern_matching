# About this repo

Simple python project to show a way to take experiental execution time to compare a set of algorithms (three in this case) in fair way.

## Pattern Matching


### Problem statement
​
The problem is to find a pattern in a text

| Algorithm            | Best Case        | Average Case     | Worst Case       | Space Complexity |
|----------------------|-----------------|------------------|------------------|------------------|
| **Brute Force**      | \( O(mn) \)       | \( O(mn) \)      | \( O(mn) \)      | \( O(1) \)        |
| **Morris-Pratt**     | \( O(n + m) \)       | \( O(n + m) \)   | \( O(n + m) \)   | \( O(m) \)        |
| **Automaton Search** | \( O(n) \)       | \( O(n) \)       | \( O(n) \)       | \( O(mσ) \)  |




# Python version
Python 3.11.0
​
# Running locally and testing

* Note: This instructions are for mac. Windows or linux may require some changes. 
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.sh`
* To try a default example, run: `: ./run.sh`. In the file ./run.sh is just an example, you can modify it. Theck the `app.py` file to get to understand how it works.

# Current coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
pattern_matching\__init__.py             0      0   100%
pattern_matching\algorithms.py          72      0   100%
pattern_matching\constants.py            2      0   100%
pattern_matching\data_generator.py      21      4    81%
test\__init__.py                         0      0   100%
test\test_algorithms.py                 24      1    96%
test\test_data_generator.py             21      1    95%
--------------------------------------------------------
TOTAL                                  140      6    96%
```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.
