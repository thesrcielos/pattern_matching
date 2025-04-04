import math
from pattern_matching import constants

def search_brute_force(word, pattern):
    size_sub = len(pattern) 
    matches = []

    for i in range(len(word) - size_sub + 1):
        isValid = True
        for j in range(size_sub):
            if word[i+j] != pattern[j]:
                isValid = False
                break
        if isValid:
            matches.append(i)
    return matches

def prepM(pattern):
    i = 0
    n = len(pattern)
    mpNext = [0] * (n + 1)
    j = mpNext[0] = -1

    while i < n:
        while j > -1 and pattern[j] != pattern[i]:
            j = mpNext[j]                               # If it fails in certain part of the pattern, jump to the part of the largest prefix that is also a sufix
        i+=1                                            
        j+=1
        mpNext[i] = j

    return mpNext

def morris_pratt_algorithm(word, pattern):
    mpNext = prepM(pattern)
    i = j = 0
    n = len(word)
    m = len(pattern)
    matches = []
    
    while j < n:
        while i > -1 and pattern[i] != word[j]:
            i = mpNext[i]
        i+=1
        j+=1
        if i >= m:
            matches.append(j - i)
            i = mpNext[i]

    return matches

def next_state(pattern, M, state, char):
    if state < M and pattern[state] == char:
        return state + 1 
    
    for i in range(state - 1, -1, -1):  
        n = 0
        if pattern[i] == char:          
            while n < i:
                if pattern[n] != pattern[state - i + n]:
                    break
                n+=1
            if n == i:
                return n + 1
    return 0


def build_automaton(pattern, alphabet):
    m = len(pattern)
    dfa = [{c: 0 for c in alphabet} for _ in range(m + 1)]
    
    for q in range(m + 1):
        for c in alphabet:
            dfa[q][c] = next_state(pattern, m, q, c)
    return dfa

def search_with_automaton(text, pattern):
    alphabet = set(text) | set(pattern)  
    dfa = build_automaton(pattern, alphabet)
    m = len(pattern)
    matches = []
    state = 0
    
    for i, c in enumerate(text):
        state = dfa[state][c] 
        if state == m:  
            matches.append(i - m + 1)
    
    return matches