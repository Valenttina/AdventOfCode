import numpy as np
import pandas as pd

opensteps = pd.read_csv("C:/Users/ValCa/Documents/Courses/AdventOfCode/Day2/input.csv")

#PUZZLE 1
depth = 0
forward = 0
aim = 0

for index, row in opensteps.iterrows():
    if row[0] == "forward":
        forward = forward + row[1]
        depth = depth + (row[1]*aim)
    elif row[0] == "up":
        aim = aim - row[1]
    else:
        aim = aim + row[1]

print(depth*forward)





