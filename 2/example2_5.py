# count formula

import math

n = 10
t = 0.99

# My solution
W = math.pi * t * 2 ** (3.0 * (n - 1) / 2)
print W

# Teacher solution
W = math.pi * t * math.pow(2, (3.0 * (n - 1) / 2))
print W
