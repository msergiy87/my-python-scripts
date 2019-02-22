# count formula. Insert 3 numbers as a parametr

import sys

x = int(sys.argv[1])	# kilkist la
y = int(sys.argv[2])	# kilkist kypletiv
z = int(sys.argv[3])	# end symbol

song_string = "Everybody sing a song:"

if x <= 0:
  print "x shouldnt be 0 and positive"
  quit()

if z == 1:
  song_end = "!"
elif z == 0:
  song_end = "."
else:
  print "z should be 0 or 1"
  quit()

if y < 0:
  print "y should be positive"
  quit()

kyplet = (' ' + 'la-'*(x-1) + 'la')*y

print song_string + kyplet + song_end

# Teacher solution
print 'Everybody sing a song:' + (' ' + 'la-'*(x-1) + 'la')*y + '!'*z + '.'*(1-z)
 
