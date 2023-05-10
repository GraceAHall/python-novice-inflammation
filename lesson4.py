

"""
Goals
- mutable vs immutable
- lists
- list slicing
"""

# python lists 


# # lists vs arrays vs tuples

# # lists: a linear collection of objects. objects can be any type.
# mylist = [2, 28, 'hello', 20.11]
# print(mylist)

# # tuples: immutable lists. 
# mytuple = (1, 5, "hello", 3)
# mytuple[0] = 2 # throws error
# print(mytuple)

# # arrays: all objects must be same type (no native python support), but numpy has this concept
# import numpy
# print(numpy.array([1, 2, 3, 4, 5]))

# mild_salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
# hot_salsa = mild_salsa        # <-- mild_salsa and hot_salsa point to the *same* list data in memory
# hot_salsa[0] = 'hot peppers'
# print('Ingredients in mild salsa:', mild_salsa)
# print('Ingredients in hot salsa:', hot_salsa)

# from copy import deepcopy
# mild_salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
# hot_salsa = deepcopy(mild_salsa) # <-- takes all the data in mild_salsa, copies it to different memory address, assigns copied data to hot_salsa
# hot_salsa[0] = 'hot peppers'
# print('Ingredients in mild salsa:', mild_salsa)
# print('Ingredients in hot salsa:', hot_salsa)

# beatles = "In an octopus's garden in the shade"
# myslice = beatles[0] + beatles[2] + beatles[4::2]
# myslice = beatles[0:35:2]  # start:stop:step
# myslice = beatles[::2]
# print(myslice)

# I notpssgre ntesae