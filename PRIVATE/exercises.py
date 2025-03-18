import numpy as np
import math as ma

# generating data for height and weight

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

# pasting together as two columns
np_city = np.column_stack((height, weight))

# Create np_height_in from np_city
np_height_in = np.array(np_city[:, 0])

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))


avg = np.mean(np_city[:, 0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_city[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_city[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
heights = np_city[:, 0]
weights = np_city[:, 1]
corr = np.corrcoef(heights, weights)
print("Correlation: " + str(corr))
