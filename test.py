import numpy as np
import random
import string

from vacuum_environment import room


def create_unique_keys_matrix_dict(matrix):
    # Create an empty dictionary to to store the matrix with unique keys:
    matrix_dict = {}

    # Iterating through the matrix and assign unique keys:
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            value = matrix[i, j]  # Questo è uno tra 'Clean' 'Dirty' e 'Obstacle'
            key = "".join(random.choices(string.ascii_uppercase, k=5))
            matrix_dict.__setitem__(key, value)

    return matrix_dict


random_matrix = room(4, 4)

resulting_dict = create_unique_keys_matrix_dict(random_matrix)
print(resulting_dict)
