# Your task is to create a Python script that analyzes 
# the records to calculate each of the following:

# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the 
# entire period
# 3. Calculate the changes in "Profit/Losses" over the
# entire period
# 4. The greatest increase in profits (date and amount)
# over the entire period
# 5. The greatest decrease in profits (date and amount)
# over the entire period

# Import Dependencies
import numpy as np
import matplotlib.pyplot as plt

# DATA SET 1
gyms = ["Crunch", "Planet Fitness", "NY Sports Club", "Rickie's Gym"]
members = [49, 92, 84, 53]

members = [49, 92, 84, 53]
x_axis = np.arange(len(gyms))

# DATA SET 2
x_lim = 2 * np.pi
x_axis = np.arange(0, x_lim, 0.1)
sin = np.sin(x_axis)

# DATA SET 3
gyms = ["Crunch", "Planet Fitness", "NY Sports Club", "Rickie's Gym"]
members = [49, 92, 84, 53]
x_axis = np.arange(0, len(gyms))
colors = ["yellowgreen", "red", "lightcoral", "lightskyblue"]
explode = (0, 0.05, 0, 0)

# DATA SET 4
x_axis = np.arange(0, 10, 0.1)
times = []
for x in x_axis:
    times.append(x * x + np.random.randint(0, np.ceil(max(x_axis))))

    