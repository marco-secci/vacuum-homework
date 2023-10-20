from agents import *
import pandas as pd


class TrivialVacuumEnvironment(Environment):
    """This environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""

    def __init__(self):
        super().__init__()
        self.status = {loc_A: "Clean", loc_B: "Clean"}

    def thing_classes(self):
        return [
            Wall,
            Dirt,
            Obstacle,
            ReflexVacuumAgent,
        ]

    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        return agent.location, self.status[agent.location]

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

    def performance_score(self, i, j, agent, action):
        self.status = [loc_A[i], loc_B[j]]

        self.execute_action(agent, action)
        print(agent.performance)


# Initialize the two-state environment
trivial_vacuum_env = TrivialVacuumEnvironment()


"""We change the simpleReflexAgentProgram so that it doesn't make use of the Rule class"""


def SimpleReflexAgentProgram():
    """This agent takes action based solely on the percept. [Figure 2.10]"""

    def program(percept):
        loc, status = percept
        return "Suck" if status == "Dirty" else "Right" if loc == loc_A else "Left"

    return program
