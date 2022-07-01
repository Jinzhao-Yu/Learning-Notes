#!/usr/bin/env python
# coding: utf-8

# # 1 Binary Search
# > **QUESTION:** Alice has some cards with numbers written on them. She arranges the cards in **decreasing** order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over **as few cards as possible**. Write a function to help Bob locate the card.

# ## 0.1 Example inputs & outputs for test
# To solve a data structure problem, the first step is to come up with some examples inputs&outputs, covered all edge cases, in order to test our algorithm.

# In[2]:


# test inputs & outputs
tests = []

# query occurs in the middle 
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# cards does not contain query, return -1
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty, return -1
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times, return the first location
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})


# In[3]:


tests


# ## 0.2 Time Complexity & Space Complexity
# Complexity: always refers to the worst-case complexity (i.e. the highest possible time/space taken by the program/algorithm to process an input)\
# Time complexity: also called the running time of the algorithm\
# Space complexity: numbers of variables we need to iterate through the array

# ## 1.1 linear search
# linear search: 按顺序比较每一个位置的元素和query是否相同，相同则返回position

# In[8]:


# linear search
def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


# In[9]:


from jovian.pythondsa import evaluate_test_cases
evaluate_test_cases(locate_card_linear, tests)


# Time complexity of linear search is O(N), because the worst case of the run time could be $cN$, where $N$ is the numbers of cards and $c$ is the runtime of one iteration.\
# Space complexity of linear serach is O(1), because we only need 1 variable `position` in the iteration.

# ## 1.2 Binary Search
# Binary Search 原理上与二分法相同，由于本身是按照顺序排列，因此每次循环只需要比较query和middle的数字进行比较，而后不断进行二分法式的比较，最终获得output\
# <img src="https://miro.medium.com/max/494/1*3eOrsoF9idyOp-0Ll9I9PA.png">

# In[ ]:




