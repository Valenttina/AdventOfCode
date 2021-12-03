import numpy as np
import pandas as pd

opensteps = pd.read_csv("C:/Users/ValCa/Documents/Courses/AdventOfCode/Day2/input.csv")

#PUZZLE 1
depth = 0
forward = 0

for index, row in opensteps.iterrows():
    if row[0] == "forward":
        forward = forward + row[1]
    elif row[0] == "up":
        depth = depth + row[1]
    else:
        depth =depth - row[1]

print(depth*forward)





