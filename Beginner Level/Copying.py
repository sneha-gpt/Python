
# Task 1 -> Use the 'is' operator to check if the copies are truly independent 

import copy
matrix = [[1, 3],
          [2, 4]]

# Assignment 
new_matrix = matrix;
print("Assigment -> Is independent? ", new_matrix is not matrix)

# Shallow copy
new_matrix = copy.copy(matrix)
print("Shallow -> Is top level independent? ", new_matrix is not matrix)
print("Shallow copy -> Is deeper level independent? ", new_matrix[0] is not matrix[0])

# Deep copy
new_matrix = copy.deepcopy(matrix)
print("Deep -> Is top level independent? ", new_matrix is not matrix)
print("Deep copy -> Is deeper level independent? ", new_matrix[0] is not matrix[0])