# First prog. Count formula. Insert 2 numbers as a parametr

import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

# My solution
x = math.sqrt(a * b) / (math.e ** a * b) + a * math.e ** (2 * a / b)
print x

# Teacher solution
y = math.sqrt(a * b) / (math.exp(a) * b) + a * math.exp(2 * a / b)
print y
