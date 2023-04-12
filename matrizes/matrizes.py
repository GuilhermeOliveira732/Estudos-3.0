import random
import re
import time
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from envs.pythonProject21.Lib.warnings import filterwarnings
from matplotlib import cm
import warnings

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid")

numero = 99
while numero != 0:
    numero = random.randint(0, 100)
    numero2 = np.random.rand(1, 100)
    numero3 = np.random.random_integers(0, 100, size=(3,3))
    numero4 = np.random.random(100)
    numero5 = np.random.randint(0, 100)
    numero6 = 1
    numero7 = 2
    print(numero, '\n', numero3, '\n', numero5)









