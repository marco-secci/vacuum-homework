import numpy as np
import random


def vacuum_agent(x: int, y: int, strings: list[str]):
    # Create a 2D array with the specified dimensions and strings:
    matrix = np.random.choice(strings, size=(x, y))
    print(f"The room is {matrix}")
    # Choose a random starting position for the agent:
    agent_pos = (random.randint(0, x - 1), random.randint(0, y - 1))
    # Loop until all cells are either Clean or Obstacle:
    while True:
        # Get the value of the current cell:
        current_cell = matrix[agent_pos]
        print(
            f"Vacuum is in position {agent_pos}; the status of the cell is {current_cell}. "
        )

        # If the cell is Dirty, clean it:
        if current_cell == "Dirty":
            matrix[agent_pos] = "Clean"
            print(f"Cleaned cell {agent_pos}")

        # If the cell is Clean, check adjacent cells for Dirty cells:
        elif current_cell == "Clean":
            possible_moves = []
            dirty_adjacent = False

            # Checking if there are dirty cells nearby:
            if agent_pos[0] > 0 and matrix[agent_pos[0] - 1, agent_pos[1]] == "Dirty":
                dirty_adjacent = True
                print(
                    f"There's a Dirty square near here! It's located in {[agent_pos[0] - 1, agent_pos[1]]}! "
                )
                possible_moves.append([agent_pos[0] - 1, agent_pos[1]])
            if (
                agent_pos[0] < x - 1
                and matrix[agent_pos[0] + 1, agent_pos[1]] == "Dirty"
            ):
                dirty_adjacent = True
                print(
                    f"There's a Dirty square near here! It's located in {[agent_pos[0] + 1, agent_pos[1]]}! "
                )
                possible_moves.append([agent_pos[0] + 1, agent_pos[1]])

            if agent_pos[1] > 0 and matrix[agent_pos[0], agent_pos[1] - 1] == "Dirty":
                dirty_adjacent = True
                print(
                    f"There's a Dirty square near here! It's located in {[agent_pos[0], agent_pos[1] - 1]}! "
                )
                possible_moves.append([agent_pos[0], agent_pos[1] - 1])
            if (
                agent_pos[1] < y - 1
                and matrix[agent_pos[0], agent_pos[1] + 1] == "Dirty"
            ):
                dirty_adjacent = True
                print(
                    f"There's a Dirty square near here! It's located in {[agent_pos[0], agent_pos[1] + 1]}! "
                )
                possible_moves.append([agent_pos[0], agent_pos[1] + 1])

            # If there is a Dirty cell adjacent, move to it. If there's more than one, choose one at random:
            if dirty_adjacent:
                dirty_pos = tuple(
                    possible_moves[random.randint(0, len(possible_moves) - 1)]
                )
                matrix[agent_pos] = "Clean"
                agent_pos = dirty_pos
                print(f"Moved to cell {agent_pos}")

            else:
                # Find a random cell that is not an Obstacle and move to it:
                possible_moves = []
                if (
                    agent_pos[0] > 0
                    and matrix[agent_pos[0] - 1, agent_pos[1]] != "Obstacle"
                ):
                    possible_moves.append("North")
                if (
                    agent_pos[0] < x - 1
                    and matrix[agent_pos[0] + 1, agent_pos[1]] != "Obstacle"
                ):
                    possible_moves.append("South")
                if (
                    agent_pos[1] > 0
                    and matrix[agent_pos[0], agent_pos[1] - 1] != "Obstacle"
                ):
                    possible_moves.append("West")
                if (
                    agent_pos[1] < y - 1
                    and matrix[agent_pos[0], agent_pos[1] + 1] != "Obstacle"
                ):
                    possible_moves.append("East")

                if len(possible_moves) > 0:
                    action = possible_moves[random.randint(0, len(possible_moves) - 1)]
                    if action == "North":
                        agent_pos = (agent_pos[0] - 1, agent_pos[1])
                    elif action == "South":
                        agent_pos = (agent_pos[0] + 1, agent_pos[1])
                    elif action == "West":
                        agent_pos = (agent_pos[0], agent_pos[1] - 1)
                    elif action == "East":
                        agent_pos = (agent_pos[0], agent_pos[1] + 1)
                    print(f"Executing action {action}...")

        # If all cells are Clean or Obstacle, break out of the loop:
        if np.all(np.isin(matrix, ["Clean", "Obstacle"])):
            break

    print("All cells are Clean or Obstacle")


# Example usage
vacuum_agent(4, 4, ["Clean", "Dirty", "Obstacle"])
