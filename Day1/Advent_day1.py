import numpy as np

opentxt = open("C:/Users/ValCa/Documents/Courses/AdventOfCode/Day1/input.txt", "r") #opens the file in read mode
measurement = np.array(opentxt.read().splitlines()) #puts the file into an array
measurement = [int(i) for i in measurement]

index1 = 0
increased1 = 0

#PUZZLE 1
for i in range(len(measurement)-1):
    index1 += 1
    if measurement[index1] > measurement[index1-1]:
        increased1 += 1
print(increased1)

#PUZZLE 2
index2 = 0
increased2 = 0
sumas = []

for i in range(len(measurement)-2):
    suma = sum(measurement[i:i+3])
    sumas.append(suma)
    index2 += 1
    if sumas[index2-1] > sumas[index2-2]:
        increased2 += 1
print(increased2)
