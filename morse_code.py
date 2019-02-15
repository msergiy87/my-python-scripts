morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--.."
}

def encode_morze(text):

   text_upper = text.upper()

   morse = ''
   lst_morse = []
   insert = ''
   lst_code = []
   coded_morse = {}

   lst_word = []
   cod_liter = ''
   lst_cod_liter = []
   lst_cod_word = []

   rezalt = ''

   for letter in morse_code:
      lst_code = []
      morse = morse_code.get(letter)
      lst_morse = list(morse)
      for symbol in lst_morse:
         if symbol == ".":
            insert = "^"
         if symbol == "-":
            insert = "^^^"
         lst_code.append(insert)
      coded_morse[letter] = "_".join(lst_code)

   lst_word = text_upper.split(' ')
   for word in lst_word:
      for liter in word:
         cod_liter = coded_morse.get(liter)
         if cod_liter == None:
            cod_liter = ""
         lst_cod_liter.append(cod_liter)
      lst_cod_word.append(lst_cod_liter)
      lst_cod_liter = []

   for a in range(len(lst_cod_word)):

      times = lst_cod_word[a].count('')
      for i in range(times):
         lst_cod_word[a].remove('')

      lst_cod_word[a] = '___'.join(lst_cod_word[a])
   for b in range(len(lst_cod_word)):

      rezalt = '_______'.join(lst_cod_word)
   return rezalt
      
print encode_morze('Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.') 
