import numpy as np
from agents import *

# Defining the values a square of the room can have:
strings = ["Clean", "Dirty", "Obstacle"]


def room(x, y):
    # Creating matrix with random values chosen between the three above:
    matrix = np.random.choice(strings, size=(x, y))

    # We do not want Non-Obstacle squares to be isolated:
    # Loop through the matrix and replace "Clean" or "Dirty" elements that do not have an adjacent square of the same type with a random value chosen between "Clean" and "Dirty"
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == "Clean":
                if (
                    i > 0
                    and matrix[i - 1][j] != "Clean"
                    and matrix[i - 1][j] != "Dirty"
                ):
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])
                elif (
                    i < 3
                    and matrix[i + 1][j] != "Clean"
                    and matrix[i + 1][j] != "Dirty"
                ):
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])
                elif (
                    j > 0
                    and matrix[i][j - 1] != "Clean"
                    and matrix[i][j - 1] != "Dirty"
                ):
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])
                elif (
                    j < 3
                    and matrix[i][j + 1] != "Clean"
                    and matrix[i][j + 1] != "Dirty"
                ):
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])
            elif matrix[i][j] == "Dirty":
                if (
                    i > 0
                    and matrix[i - 1][j] != "Dirty"
                    and matrix[i - 1][j] != "Clean"
                ):
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])
                elif (
                    i < 3
                    and matrix[i + 1][j] != "Dirty"
                    and matrix[i + 1][j] != "Clean"
                ):
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])
                elif (
                    j > 0
                    and matrix[i][j - 1] != "Dirty"
                    and matrix[i][j - 1] != "Clean"
                ):
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])
                elif (
                    j < 3
                    and matrix[i][j + 1] != "Dirty"
                    and matrix[i][j + 1] != "Clean"
                ):
                    matrix[i][j] = np.random.choice(["Clean", "Dirty"])

    print(matrix)


room(4, 4)
