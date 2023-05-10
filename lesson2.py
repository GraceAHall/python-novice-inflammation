

"""
Goals
- learn numpy basics
- Explain what a library is and what libraries are used for.
- Import a Python library and use the functions it contains.
- Read tabular data from a file into a program.
- Select individual values and subsections from data.
- Perform operations on arrays of data.
"""

### loading with numpy ###
# import numpy 
# load data
# set const vars, reload data
# attributes vs methods

import numpy

INFLAMMATION1_PATH = 'data/inflammation-01.csv'
DELIMITER = ','

# data = numpy.loadtxt(fname=INFLAMMATION1_PATH, delimiter=DELIMITER)
# print(data) 
# print(type(data))
# print(data.dtype)
# print(data.shape)
# print('first value in data:', data[0, 0])

### what is code? 
# - computer doesn't care about the text. doesn't read any of it. 
# - eg a binary .exe executable - its just 1s and 0s. 
# - so what are coding languages? 
# - just a way for us to wrap our little human brains around what we are doing. 
# - humans like to model things as objects
# - eg a car: 4 wheels, 4 doors, headlights, can honk, can drive
# - python thinks of everything as an object
# we could imagine a car CLASS which would have the following

"""
class Car:
    # traits (attributes)
    wheels: int
    doors: int
    num_headlights: int
    
    # functionality (methods)
    def drive():
        # moves the car forward
    
    def honk():
        # makes the car honk

"""
# print(data.dtype)  # attribute
# print(data.shape)  # attribute


# class Snail:
#     def __init__(self, name: str, age: int, color: str):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.x: int = 0
#         self.y: int = 0

#     def move(self, vec: list[int]) -> None:
#         self.x += vec[0]
#         self.y += vec[1]
#         print(f'I, the great snail {self.name} am moving.')
#         print(f'I, the great snail {self.name} am at [{self.x}, {self.y}]')
    
# fred = Snail('fred', 11, 'brown')
# print(fred.name)
# print(fred.age)
# print(fred.x)
# fred.move([5, 1])
# fred.move([1, 2])
# print(fred.x)

## back to our dataframe 
# print(data[0][1])
# print(data[0, 1])

#           day1 day2 day3 
# patient      0    2    2 

# print('top left corner')
# print(data[0:5, 0:5])
# print()
# print('first row (patient 1)')
# print(data[0, 0:40])    # first row (patient 1)
# print()
# print('still first row (patient 1)')
# print(data[0, :])       # still first row (patient 1)
# print()
# print('second row (patient 2)')
# print(data[1, :])       # second row (patient 2)
# print()
# print('inflammation for patient 1 on day 5')
# print(data[0, 4])       # inflammation for patient 1 on day 5

# data = numpy.loadtxt(fname=INFLAMMATION1_PATH, delimiter=DELIMITER)

# maxval, minval, stdval = numpy.amax(data), numpy.amin(data), numpy.std(data)
# maxval = numpy.amax(data)
# minval = numpy.amin(data)
# stdval = numpy.std(data)

# print('maximum inflammation:', maxval)
# print('minimum inflammation:', minval)
# print('standard deviation:', stdval)

# print('maximum inflammation:', numpy.amax(data))
# print('minimum inflammation:', numpy.amin(data))
# print('standard deviation:', numpy.std(data))

# patient_max_inflammations = numpy.amax(data, axis=1)
# daily_max_inflammations = numpy.amax(data, axis=0)

# print('\npatient_max_inflammations: \n',  patient_max_inflammations)
# print('\ndaily_max_inflammations: \n',  daily_max_inflammations)

# patient_mean_inflammations = numpy.mean(data, axis=1)
# daily_mean_inflammations = numpy.mean(data, axis=0)

# print('\npatient_mean_inflammations: \n',  patient_mean_inflammations)
# print('\ndaily_mean_inflammations: \n',  daily_mean_inflammations)

# patient4_week1 = data[3, :7]
# print(patient4_week1)
# print(numpy.diff(patient4_week1))

# patient4 = data[3, :]
# print(patient4_week1)
# print(numpy.diff(patient4))




