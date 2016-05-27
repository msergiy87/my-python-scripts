import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = sys.argv[1].lower()
shift = int(sys.argv[2])
coded_text = ''
new_letter = ''
letter_position = None

coder = {}
for i in range(len(alphabet)):
    coder[alphabet[i]] = alphabet[(i + shift) % len(alphabet)]

for letter in text:
    if letter in coder:
        coded_text = coded_text + coder[letter]
    else:
        coded_text = coded_text + letter
print coded_text
