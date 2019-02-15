# count formula. Insert 3 numbers as a parametr

import sys
import math

x = float(sys.argv[1])
u = float(sys.argv[2])
q = float(sys.argv[3])

# My solution
y = 1 / (q * math.sqrt(2 * math.pi)) *  math.pow(math.e, (-1 * (math.pow((x-u), 2) / (2 * math.pow(q, 2)))))
print y

# Teacher solution
z = (1 / (q * math.sqrt(2 * math.pi))) * math.exp(-(x-u) ** 2 / (2 * q ** 2))
print z
