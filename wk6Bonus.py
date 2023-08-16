import random
import math
count = 0
for i in range(10000):
    x = random.random()
    y = random.random()
    if (x**2) + (y**2) < 1:
        count += 1
pi = 4 * (count/10000)
print("Calculated value of π:", pi)
print("Value of π from math library:", str(math.pi))
print("Difference:", pi - math.pi)
