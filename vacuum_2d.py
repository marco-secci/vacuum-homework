import pandas as pd
import numpy as np

import vacuum_agent
from agents import *
from vacuum_world import SimpleReflexAgentProgram, program
from vacuum_environment import room


# ====================================== #
# BIDIMENSIONAL VACUUM ENVIRONMENT CLASS #
# ====================================== #
class BidimensionalVacuumEnvironment(Environment):
    """This environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""

    # =========== #
    # INIT METHOD #
    # =========== #
    def __init__(self, x, y):
        super().__init__()
        # Set environment dimensions:
        self.x = x
        self.y = y
        # Create rooms:
        self.matrix = room(self.x, self.y)
        # rooms statuses list:

        # Create dictionary with rooms' statuses:
        self.status = {}

    # ==================== #
    # THING CLASSES METHOD #
    # ==================== #
    def thing_classes(self):
        return [
            Wall,
            Dirt,
            Obstacle,
            ReflexVacuumAgent,
        ]

    # ============== #
    # PERCEPT METHOD #
    # ============== #
    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        return agent.location, self.status[agent.location]

    # ===================== #
    # EXECUTE ACTION METHOD #
    # ===================== #
    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""

        if action == "Right":
            agent.location = loc_B
            agent.performance -= 1
        elif action == "Left":
            agent.location = loc_A
            agent.performance -= 1
        elif action == "Suck":
            if self.status[agent.location] == "Dirty":
                agent.performance += 10
            self.status[agent.location] = "Clean"

    """We change the SimpleReflexAgentProgram so that it doesn't make use of the Rule class"""


# ================================== #
# SIMPLE REFLEX AGENT PROGRAM METHOD #
# ================================== #
def SimpleReflexAgentProgram():
    """This agent takes action based solely on the percept. [Figure 2.10]"""

    # ============== #
    # PROGRAM METHOD #
    # ============== #
    def program(percept):
        loc, status = percept
        if status == "Dirty":
            return "Suck"
        elif status == "Clean":
            pass  # TODO

    return program


if __name__ == "__main__":
    # Initialize the two-state environment
    env = BidimensionalVacuumEnvironment()
    vacuum = Agent(program)

    print(room(4, 4))
