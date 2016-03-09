import fileread

KEY_TABLE = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [],'g': [], 
              'h': [], 'i': [],'j': [], 'k': [], 'l': [],'m': [], 'n': [], 
              'o': [],'p': [], 'q': [], 'r': [],'s': [], 't': [], 
              'u': [],'v': [], 'w': [], 'x': [], 'y': [], 'z': []}

KEY_LENGTH = {'a': 8, 'b': 1, 'c': 3, 'd': 4, 'e': 13, 'f': 2,'g': 2, 
              'h': 6, 'i': 7,'j': 1, 'k': 1, 'l': 4,'m': 2, 'n': 7, 
              'o': 8,'p': 2, 'q': 1, 'r': 6,'s': 6, 't': 9, 
              'u': 3,'v': 1, 'w': 2, 'x': 1, 'y': 2, 'z': 1}


def text_to_num_list(text):
  num = []
  for words in text.split(' '):
    temp = []
    for i in words.split(','):
      temp.append(int(i))
    num.append(temp)
  return num


def length_compare(text, numlist):
  for i in range(0, len(text)):
    if len(text[i]) != len(numlist[i]):
      print text[i], len(text[i]), numlist[i], len(numlist[i])
      return False
  return True


def find_fit_length_plaintext(dictionary,cipher_num):
  itr = []
  for i in range(0,len(dictionary)):
    print dictionary[i]
    if length_compare(dictionary[i], cipher_num):
      itr.append(i)
  return itr


def assign_key(text, numlist):
  key_t = KEY_TABLE
  for i in range(0,len(text)):
    for j in range(0,len(text[i])):
      key_t[text[i][j]].append(numlist[i][j])
  print key_t





# main
plaintext = fileread.PLAINTEXT()
print plaintext.english_words
cipher_text = raw_input("--->")
cipher_num = text_to_num_list(cipher_text)

print cipher_num

itr = find_fit_length_plaintext(plaintext.dictionary, cipher_num)

if len(itr) == 0:
  print("The cipher text is NOT encrypted from the plaintext of dictionary\n")

else:
  assign_key(plaintext.dictionary[itr[0]], cipher_num)




