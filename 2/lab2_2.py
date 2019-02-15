# print sound text. Insert 3 numbers as a parametr

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# My solution
string = "Everybody sing a song: "

if z == 1:
    end = "!"
else:
    end = "."

if y == 0:
    string = string[:-1]

la = "la-" * x
la = la[:-1]

kypl = (la+" ") * y
kypl = kypl[:-1]

print string + kypl + end

# Teacher solution
print 'Everybody sing a song:' + (' ' + 'la-'*(x-1) + 'la')*y + '!'*z + '.'*(1-z)
