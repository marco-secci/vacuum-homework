import numpy as np
import matplotlib.pyplot as plt
import random
import string

from vacuum_world import SimpleReflexAgentProgram, program
from agents import *

# Defining the values a square of the room can have:


# ============ #
# ROOMS METHOD #
# ============ #
def rooms(x: int, y: int, strings: list[str]):
    """
    ## `rooms` method

    ==================================

    #### Description

    Takes as input the two dimensions of the room and creates one accordingly with random status for every cell, chosen between "Clean", "Dirty" and "Obstacle". Every cell touching other two squares that are either Clean or Dirty at directions North, West, South, or East.

    ==================================

    #### Parameters

    #### - `x`: `int`
    Room's dimension on the `x` axis.

    #### - `y`: `int`
    Room's dimension on the `y` axis.

    #### - `strings`: `list[str]`
    The list of strings that will be used to randomly assign a value to every cell of the room.
    """
    # Creating matrix with random values chosen between the three above:
    matrix = np.random.choice(strings, size=(x, y))

    # Loop through the matrix and replace "Clean" or "Dirty" elements that do not have two adjacent squares of the same type with a random value chosen between "Clean" and "Dirty"
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == "Clean":
                adjacent_one = False
                adjacent_two = False
                if i > 0 and matrix[i - 1][j] == "Clean":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif i < x - 1 and matrix[i + 1][j] == "Clean":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif j > 0 and matrix[i][j - 1] == "Clean":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif j < y - 1 and matrix[i][j + 1] == "Clean":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                if i > 0 and matrix[i - 1][j] == "Dirty":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif i < x - 1 and matrix[i + 1][j] == "Dirty":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif j > 0 and matrix[i][j - 1] == "Dirty":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif j < y - 1 and matrix[i][j + 1] == "Dirty":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                if not adjacent_one or not adjacent_two:
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])
            elif matrix[i][j] == "Dirty":
                adjacent_one = False
                adjacent_two = False
                if i > 0 and matrix[i - 1][j] == "Clean":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif i < x - 1 and matrix[i + 1][j] == "Clean":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif j > 0 and matrix[i][j - 1] == "Clean":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif j < y - 1 and matrix[i][j + 1] == "Clean":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                if i > 0 and matrix[i - 1][j] == "Dirty":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif i < x - 1 and matrix[i + 1][j] == "Dirty":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif j > 0 and matrix[i][j - 1] == "Dirty":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                elif j < y - 1 and matrix[i][j + 1] == "Dirty":
                    if adjacent_one == False:
                        adjacent_one = True
                    elif adjacent_two == False:
                        adjacent_two = True
                if not adjacent_one or not adjacent_two:
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])

    return matrix
    # Creating cool visualization of the room
    # plt.imshow(matrix, "Paired")
    # plt.colorbar()
    # plt.xlabel("")
    # plt.ylabel("")
    # plt.show()
    # print(matrix)


# ===================== #
# ROOMS KEYCHAIN METHOD #
# ===================== #
def rooms_keychain(matrix: np.ndarray):
    """
    ## `rooms_keychain` method

    ==================================

    #### Description
    Returns a dictionary with a different key for every cell. If two cells have the same status, they're key
    will still be different.

    ==================================

    #### Parameters

    #### - `matrix` : `ndarray`
    The matrix for which the keychain will be created.
    """
    # Create an empty dictionary to to store the matrix with unique keys:
    matrix_dict = {}

    # Iterating through the matrix and assign unique keys:
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            value = matrix[i, j]
            key = "".join(random.choices(string.ascii_uppercase, k=5))
            matrix_dict.__setitem__(key, value)

    return matrix_dict


# ====================== #
# KEYCHAIN MATRIX METHOD #
# ====================== #
def keychain_matrix(keychain: dict, matrix: np.ndarray):
    """
    ## `keychain_matrix` method

    ==================================

    #### Description
    Uses a matrix created with the `rooms` method, a keychain created with the `rooms_keychain` method,
    and creates a matrix of the same dimension of the room, with in each cell the key corresponding to the room's
    cell.

    #### Parameters

    #### - `keychain`: `dict`
    The dictionary of all keys assigned to cells in the room.

    #### - `matrix` `np.ndarray`
    The room matrix created for which the keychain has been made.
    """
    key_matrix = matrix  # Placeholder because np.empty_like does not work properly
    list_keys = list(keychain.keys())
    # Counter for the cell we are in:
    counter = 0
    # Iterating through every cell:
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Creating the new matrix:
            key_matrix[i, j] = list_keys[counter]
            counter += 1
    return key_matrix


if __name__ == "__main__":
    strings = ["Clean", "Dirty", "Obstacle"]
    random_matrix = rooms(4, 4, strings)

    resulting_dict = rooms_keychain(random_matrix)
    key_matrix = keychain_matrix(resulting_dict, random_matrix)
    print(resulting_dict)
    print(key_matrix)
