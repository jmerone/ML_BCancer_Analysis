# Python code for Breast Cancer Data

#Step 1: import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
                      header = None)