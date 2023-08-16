import random
import statistics as s

def gaussian_distribution():
    values = []
    for _ in range(1000):
        values.append(random.gauss(100, 10))
    return values
print("Mean: ", s.mean(gaussian_distribution()))
print("Standard Deviation: ", s.stdev(gaussian_distribution()))