import numpy as np


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


class BidimensionalVacuumAgent:
    def __init__(self, env: np.ndarray):
        self.performance = 0
        self.x = env.shape[0]
        self.y = env.shape[1]
        self.env = env

    def vacuum_agent(self):
        # Create a 2D array with the specified dimensions and strings:
        print(f"The room is {self.env}")
        # Choose a random starting position for the agent:
        # Create a list of valid positions that are not obstacles
        valid_positions = []

        for i in range(self.x):
            for j in range(self.y):
                if self.env[i, j] != "Obstacle":
                    valid_positions.append((i, j))

        if not valid_positions:
            print(
                f"""No valid starting positions (without obstacles) available. You hit the one in {(1 / (1/3)^(x * y))} chance to get a {x} by {y} self.env composed
                at random choosing among three values composed of only one of these three elements, I'd go play some scratch cards if I were you.
                Now, let's re-run the script: """
            )
            return self.vacuum_agent(
                self.x, self.y
            )  # Abort if there are no valid positions.

        # Choose a random starting position for the agent from valid positions:
        self.agent_pos = random.choice(valid_positions)
        # Loop until all cells are either Clean or Obstacle:

    def movement(self):
        while True:
            # Get the value of the current cell:
            current_cell = self.env[self.agent_pos]
            print(
                f"Vacuum is in position {self.agent_pos}; the status of the cell is {current_cell}. "
            )

            # If the cell is Dirty, clean it:
            if current_cell == "Dirty":
                self.env[self.agent_pos] = "Clean"
                print(f"Cleaned cell {self.agent_pos}")
                self.performance += 10

            # If the cell is Clean, check adjacent cells for Dirty cells:
            elif current_cell == "Clean":
                possible_moves = []
                dirty_adjacent = False

                # Checking if there are dirty cells nearby:
                if (
                    self.agent_pos[0] > 0
                    and self.env[self.agent_pos[0] - 1, self.agent_pos[1]] == "Dirty"
                ):
                    dirty_adjacent = True
                    print(
                        f"There's a Dirty square near here! It's located in {[self.agent_pos[0] - 1, self.agent_pos[1]]}! "
                    )
                    possible_moves.append([self.agent_pos[0] - 1, self.agent_pos[1]])
                if (
                    self.agent_pos[0] < self.x - 1
                    and self.env[self.agent_pos[0] + 1, self.agent_pos[1]] == "Dirty"
                ):
                    dirty_adjacent = True
                    print(
                        f"There's a Dirty square near here! It's located in {[self.agent_pos[0] + 1, self.agent_pos[1]]}! "
                    )
                    possible_moves.append([self.agent_pos[0] + 1, self.agent_pos[1]])

                if (
                    self.agent_pos[1] > 0
                    and self.env[self.agent_pos[0], self.agent_pos[1] - 1] == "Dirty"
                ):
                    dirty_adjacent = True
                    print(
                        f"There's a Dirty square near here! It's located in {[self.agent_pos[0], self.agent_pos[1] - 1]}! "
                    )
                    possible_moves.append([self.agent_pos[0], self.agent_pos[1] - 1])
                if (
                    self.agent_pos[1] < self.y - 1
                    and self.env[self.agent_pos[0], self.agent_pos[1] + 1] == "Dirty"
                ):
                    dirty_adjacent = True
                    print(
                        f"There's a Dirty square near here! It's located in {[self.agent_pos[0], self.agent_pos[1] + 1]}! "
                    )
                    possible_moves.append([self.agent_pos[0], self.agent_pos[1] + 1])

                # If there is a Dirty cell adjacent, move to it. If there's more than one, choose one at random:
                if dirty_adjacent:
                    dirty_pos = tuple(
                        possible_moves[random.randint(0, len(possible_moves) - 1)]
                    )
                    self.env[self.agent_pos] = "Clean"
                    self.agent_pos = dirty_pos
                    print(f"Moved to cell {self.agent_pos}")
                    self.performance -= 1

                else:
                    # Find a random cell that is not an Obstacle and move to it:
                    possible_moves = []
                    if (
                        self.agent_pos[0] > 0
                        and self.env[self.agent_pos[0] - 1, self.agent_pos[1]]
                        != "Obstacle"
                    ):
                        possible_moves.append("North")
                    if (
                        self.agent_pos[0] < self.x - 1
                        and self.env[self.agent_pos[0] + 1, self.agent_pos[1]]
                        != "Obstacle"
                    ):
                        possible_moves.append("South")
                    if (
                        self.agent_pos[1] > 0
                        and self.env[self.agent_pos[0], self.agent_pos[1] - 1]
                        != "Obstacle"
                    ):
                        possible_moves.append("West")
                    if (
                        self.agent_pos[1] < self.y - 1
                        and self.env[self.agent_pos[0], self.agent_pos[1] + 1]
                        != "Obstacle"
                    ):
                        possible_moves.append("East")

                    if len(possible_moves) > 0:
                        action = possible_moves[
                            random.randint(0, len(possible_moves) - 1)
                        ]
                        if action == "North":
                            self.agent_pos = (self.agent_pos[0] - 1, self.agent_pos[1])
                        elif action == "South":
                            self.agent_pos = (self.agent_pos[0] + 1, self.agent_pos[1])
                        elif action == "West":
                            self.agent_pos = (self.agent_pos[0], self.agent_pos[1] - 1)
                        elif action == "East":
                            self.agent_pos = (self.agent_pos[0], self.agent_pos[1] + 1)
                        print(f"Executing action {action}...")
                        self.performance -= 1

            # If all cells are Clean or Obstacle, break out of the loop:
            if np.all(np.isin(self.env, ["Clean", "Obstacle"])):
                break

        print("All cells are Clean or Obstacle")
        return


if __name__ == "__main__":
    strings = ["Clean", "Dirty", "Obstacle"]
    random_matrix = rooms(4, 4, strings)

    vacuum = BidimensionalVacuumAgent(random_matrix)
    vacuum.vacuum_agent()
    vacuum.movement()
    print(
        f"The vacuum has finished its job. Its performance score is {vacuum.performance}. "
    )
