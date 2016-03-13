"""
<Program Name>
  Hu-Lin-Vadakkalpradeepkumar-decrypt2.py
<Purpose>
  This script implements the decryptor for course CS6903 project1, test#2.
  The decryptor works for decrypting the cipher text which is
  randomly select 500 characters from known plaintext with 100k words,
  and encrypted by permutatino ciphers.
"""



import fileread
import time
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




# Build the words dictionary from english_word with a same length
def setup_list(length):
  temp_list = []
  plaintext = fileread.PLAINTEXT()
  for words in plaintext.english_words:
    if len(words) == length:
      temp_list.append(words)
  return temp_list




# Comvert input cipher string to num list
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





# reset text-cipher table
def reset_dictionary(num_to_key):
  temp_dic = deepcopy(KEY_TABLE)
  for key, value in num_to_key.iteritems():
    temp_dic[value].append(key)
  return temp_dic




# Main algorithm function
# Input ciper list which is sorted by length, longest to shortest
# Create words list for different length of cipher
# Depth First Searching algorithm
# From cipher words[i], search first no-conflict plaintext from dictionary with same words length
# If success get a plintext, i++
# Else, i--, pop previous cipher's plaintext
# Conflict checking by both cipher_to_text and text_to_cipher table
def assign_key(temp_cipher):
  reset_num_list = {}
  key_table_temp = deepcopy(KEY_TABLE)
  plain_list = []
  back_up_list = {}
  reset_temp_num_list = []
  flag = True
  num_to_key = {}

  i = 0
  j = 0
  k = 0
  flag_list = []
  flag = True
  flagk = True

  for k in range(0, len(temp_cipher)):
    if len(temp_cipher[k]) not in back_up_list:
      back_up_list[len(temp_cipher[k])] = setup_list(len(temp_cipher[k]))
  k = 0

  while i < len(temp_cipher):
    if i not in flag_list:
      if len(plain_list) > i:
        del plain_list[i:]
      templist = deepcopy(back_up_list[len(temp_cipher[i])])
      plain_list.append(templist)
      flag_list.append(i)
      flag_list.sort()

    while len(plain_list[i]) > 0:

      flag = True

      while j < len(temp_cipher[i]):


        if temp_cipher[i][j] not in num_to_key:
          # conflict
          if len(key_table_temp[plain_list[i][0][j]]) == KEY_LENGTH[plain_list[i][0][j]]:
            flag = False
            for key in reset_temp_num_list:
              del num_to_key[key]
            key_table_temp = reset_dictionary(num_to_key)
            reset_temp_num_list = []
            break
          # no conflict
          key_table_temp[plain_list[i][0][j]].append(temp_cipher[i][j])
          num_to_key[temp_cipher[i][j]] = plain_list[i][0][j]
          reset_temp_num_list.append(temp_cipher[i][j])
          j = j+1
        else:
          # conflict
          if num_to_key[temp_cipher[i][j]] != plain_list[i][0][j]:
            flag = False
            for key in reset_temp_num_list:
              del num_to_key[key]
            key_table_temp = {}
            key_table_temp = deepcopy(reset_dictionary(num_to_key))
            reset_temp_num_list = []
            break
          j = j+1



      # plain[i][k] is fit for cipher[i]
      if flag:
        reset_num_list[i] = reset_temp_num_list
        reset_temp_num_list = []
        flagk = True
        j = 0
        break
      # plain[i][k] is not fit for cipher[i], k++
      else:
        j=0
        del plain_list[i][0]
        flagk = False

    # cipher[i] can't fit in plain[i]
    # roll back to i-1
    if not flagk:
      if i == 0:
        num_to_key = []
        return num_to_key
      flag_list.remove(i)
      for key in reset_temp_num_list:
        del num_to_key[key]
      reset_temp_num_list = []
      i = i-1
      for key in reset_num_list[i]:
        del num_to_key[key]
      key_table_temp = {}
      key_table_temp = deepcopy(reset_dictionary(num_to_key))
      del reset_num_list[i]
      del plain_list[i][0]
      flagk = True
    else:
      i = i+1
  return num_to_key








if __name__ == "__main__":
  print "\n\n************************************************************************"
  print "* Title  : Project 1 (Cryptanalysis: decryption of permutation ciphers)"
  print "* Decryptor for test#2"
  print "* Author : Yu Hu, Heng Lin and Aravind Vadakkalpradeepkumar"
  print "* Date   : 03/12/2016 "
  print "************************************************************************\n\n";

  while True:
    print "Please input your cipher text:"
    cipher_text = raw_input("--->")
    #cipher_text = enc.enc_test_1(temp_str)
    temp_cipher = text_to_num_list(cipher_text)
    if len(temp_cipher) == 0:
      print "Invalid cipher text input\n please reinput your cipher\n"
    else:
      break

  num_to_key = {}

  sorted_cipher = deepcopy(temp_cipher)
  sorted_cipher.sort(key = len, reverse = True)

  start_time = time.time()
  num_text = assign_key(sorted_cipher)

  if len(num_text) == 0:
    print "The cipher text is not encrpted from the word in the english_words"
  else:
    key_table_temp = {}
    key_table_temp = deepcopy(reset_dictionary(num_text))

    print "The key table is shown below:"
    print key_table_temp

    string = ""

    for num in temp_cipher:
      for i in num:
        string += num_text[i]
      string += ' '

    print "The plaintext for cipher is shown below:"
    print string
    print("--- %s seconds ---" % (time.time() - start_time))

    print "Thank you for your using."

  raw_input("Press any key to exit...")
