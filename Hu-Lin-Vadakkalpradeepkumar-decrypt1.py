"""
<Program Name>
  Hu-Lin-Vadakkalpradeepkumar-decrypt1.py
<Purpose>
  This script implements the decryptor for course CS6903 project1, test#1.
  The decryptor works for decrypting the cipher text which is
  randomly select from plaintext_dictionary.txt with five 500 hundres characters plaintext,
  and encrypted by permutatino ciphers.
"""

import fileread
from copy import deepcopy


# Initial KEY_TABLE
KEY_TABLE = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [],'g': [],
              'h': [], 'i': [],'j': [], 'k': [], 'l': [],'m': [], 'n': [],
              'o': [],'p': [], 'q': [], 'r': [],'s': [], 't': [],
              'u': [],'v': [], 'w': [], 'x': [], 'y': [], 'z': []}



# Settup the encryption rule for each characters
KEY_LENGTH = {'a': 8, 'b': 1, 'c': 3, 'd': 4, 'e': 13, 'f': 2,'g': 2,
              'h': 6, 'i': 7,'j': 1, 'k': 1, 'l': 4,'m': 2, 'n': 7,
              'o': 8,'p': 2, 'q': 1, 'r': 6,'s': 6, 't': 9,
              'u': 3,'v': 1, 'w': 2, 'x': 1, 'y': 2, 'z': 1}



# Convert input ciper text to numbers
# Valid input checking
def text_to_num_list(text):
  num = []
  for words in text.split(' '):
    temp = []
    for i in words.split(','):
      if i.isdigit():
        if 0 <= int(i) <= 102:
          temp.append(int(i))
        else:
          num = []
          return num
      else:
        num = []
        return num
    num.append(temp)
  return num


# Comparing each words length between ciphertext and plaintext
def _length_compare(text, numlist):
  if len(text) != len(numlist):
    return False
  for i in range(0, len(text)):
    if len(text[i]) != len(numlist[i]):
      return False
  return True



# Comparing all plaintext sentences' words length with cipertext
def find_fit_length_plaintext(dictionary,cipher_num):
  itr = []
  for i in range(0,len(dictionary)):
    if _length_compare(dictionary[i], cipher_num):
      itr.append(i)
  return itr



# Assign the cipher text as key to each characters
# Using encription rule to check the key paring
# if assigned key's number is larger than preset size
# or same number assigned more than one character
# return false
def assign_key(text, numlist):
  for i in range(0,len(text)):
    key_t = deepcopy(KEY_TABLE)
    num_key_table = {}
    for j in range(0,len(text[i])):
      if numlist[i][j] not in num_key_table:
        num_key_table[numlist[i][j]] = text[i][j]
        key_t[text[i][j]].append(numlist[i][j])
        if len(key_t[text[i][j]]) > KEY_LENGTH[text[i][j]]:
          return False
      else:
        if num_key_table[numlist[i][j]] != text[i][j]:
          return False
  return True



# main
# may add a function later
if __name__ == "__main__":
  print "\n\n************************************************************************"
  print "* Title  : Project 1 (Cryptanalysis: decryption of permutation ciphers)"
  print "* Decryptor for test#1"
  print "* Author : Yu Hu, Heng Lin and Aravind Vadakkalpradeepkumar"
  print "* Date   : 03/12/2016 "
  print "************************************************************************\n\n";
  plaintext = fileread.PLAINTEXT()
  temp_str = ' '.join(plaintext.dictionary[4])
  while True:
    print "Please enter your cipher text"
    cipher_text = raw_input("--->")
    #cipher_text = enc.enc_test_1(temp_str)
    cipher_num = text_to_num_list(cipher_text)
    if len(cipher_num) == 0:
      print "Invalid cipher text input\n please reinput your cipher\n"
    else:
      break


  itr = find_fit_length_plaintext(plaintext.dictionary, cipher_num)

  if len(itr) == 0:
    print("The cipher text is NOT encrypted from the plaintext of dictionary\n")

  else:
    dict_key = []
    found_flag = 0
    for i in itr:
      if(assign_key(plaintext.dictionary[i], cipher_num)):
        print "\nFound a fit plaintext! The plaintext is shown as below:\n"
        temp_str = ' '.join(plaintext.dictionary[i])
        found_flag += 1
        print temp_str
    if found_flag > 0:
      print "Totally found ", found_flag, " plaintext fit for this cipher_text\n"
    else:
      print "The input cipher text was not encrypted from known plaintext\n"

  raw_input("Press any key to exit...")




