# ================================================================= #
import pandas as pd  #
import matplotlib.pyplot as plt  #
import random  #
import numpy as np  #

#                                                                   #
import vacuum_environment as env  #
from agents import *  #
from vacuum_world import program  #

# ================================================================= #


def BidimensionalModelBasedVacuumAgent(x: int, y: int, strings: list[str]):
    matrix = env.rooms(x, y, strings)
    model = env.rooms_keychain()

    def program(percept):
        pass

    return program
