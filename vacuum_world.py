from agents import *

class TrivialVacuumEnvironment(Environment):
    """This environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""

    def __init__(self):
        super().__init__()

    def thing_classes(self):
        return [
            Wall,
            Dirt,
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
        loc, status = percept()
        return ('Suck' if status == 'Dirty' 
                else'Right' if loc == loc_A 
                            else'Left')
    return program

        
# Create a simple reflex agent the two-state environment
program = SimpleReflexAgentProgram()
simple_reflex_agent = Agent(program)



for p in range(2):
    trivial_vacuum_env.add_thing(simple_reflex_agent)
    simple_reflex_agent.location = p
    if p == 0:
        action = 'Right'
    else:
        action = 'Left'
    print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))
    for i in range(2):
        for j in range(2):
            # Run the environment
            trivial_vacuum_env.performance_score(i, j, simple_reflex_agent, action='Right')
            
            # Check the current state of the environment
            print("State of the Environment: {}.".format(trivial_vacuum_env.status))

            print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))

            # Delete the previously added simple reflex agent
            trivial_vacuum_env.delete_thing(simple_reflex_agent)












# # TODO: Implement this function for the two-dimensional environment
# def update_state(state, action, percept, model):
#     pass

# # Create a model-based reflex agent
# model_based_reflex_agent = ModelBasedVacuumAgent()

# # Add the agent to the environment
# trivial_vacuum_env.add_thing(model_based_reflex_agent)

# print("ModelBasedVacuumAgent is located at {}.".format(model_based_reflex_agent.location))

# # Run the environment
# trivial_vacuum_env.step()

# # Check the current state of the environment
# print("State of the Environment: {}.".format(trivial_vacuum_env.status))

# print("ModelBasedVacuumAgent is located at {}.".format(model_based_reflex_agent.location))
