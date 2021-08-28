import os
import pandas as pd

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


df = pd.read_csv(os.path.join(HOME, "python", "options.csv"))


# options
reps = 15-5 + 1

cardio = 2

rest = 4

sets = 3

exercises = len(df)

reps * cardio * rest * sets * exercises