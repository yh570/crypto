# <Program Name>
#  enc.py
# <Purpose>
#  This script implements the encryptor for Test 1 and Test 2.
#  It's used to create samples for test1 and test 2 to verify the correctness of Test 1 and Test 2

import random

# DEBUG FLAG
DEBUG = 1

L = 500
WORDS_NUM = 25
KEY_LENGTH = {'a': 8, 'b': 1, 'c': 3, 'd': 4, 'e': 13, 'f': 2,'g': 2,
              'h': 6, 'i': 7,'j': 1, 'k': 1, 'l': 4,'m': 2, 'n': 7,
              'o': 8,'p': 2, 'q': 1, 'r': 6,'s': 6, 't': 9,
              'u': 3,'v': 1, 'w': 2, 'x': 1, 'y': 2, 'z': 1}


# The computation of which key is returned by the algorithm is
# based on a scheduling algorithm which is intentionally left
# unknown and is a deterministic algorithm.
# This function is a supposed algorithm.
# It may depend on j, L and the length of the list on that row.
def unknown_deterministic_algorithm(j, L, length_current_key):
  return j % length_current_key
  # return j * L % length_current_key


# Generate the plaintext-to-ciphertext table
def enc_cipher_maps_gen():
  cipher_maps = {}
  for key in KEY_LENGTH:
    cipher_maps[key] = []
  cipher_randoms_gen = random.sample(xrange(0,103), 103)
  count = 0
  for key in KEY_LENGTH:
    for length_ch in range(KEY_LENGTH[key]):
      cipher_maps[key].append(cipher_randoms_gen[count])
      count += 1
  return cipher_maps

# Generate the plaintext for Test 2
# Each word is randomly chosen from english dictionary words
# 'english_words.txt' should be placed in the same path
def test_2_plaintext_gen():
  plaintext = ""
  f = open('english_words.txt')
  english_words = f.readlines()
  print english_words
  random_index = random.sample(xrange(len(english_words)), WORDS_NUM)

  for i in range(WORDS_NUM):
    plaintext += english_words[random_index[i]][:-2] + " "

  # delete last space-separate
  return plaintext[:-1]

# Generate ciphertext for Test 1
# Input is string type
def enc_test_1(plaintext):
  ciphertext = ""
  cipher_maps = enc_cipher_maps_gen()

  if DEBUG:
    print cipher_maps

  for j in range(L):
    if plaintext[j] == " ":
      ciphertext += " "
      continue
    ciphertext += str(cipher_maps[plaintext[j]][unknown_deterministic_algorithm(j, L, len(cipher_maps[plaintext[j]]))])
    if j < L - 1:
      if plaintext[j + 1] != " ":
        ciphertext += ","

  return ciphertext

# Generate ciphertext for Test 2
# Input is string type
def enc_test_2(plaintext):
  ciphertext = ""
  cipher_maps = enc_cipher_maps_gen()

  for j in range(len(plaintext)):
    if plaintext[j] == " ":
      ciphertext += " "
      continue
    ciphertext += str(cipher_maps[plaintext[j]][unknown_deterministic_algorithm(j, len(plaintext), len(cipher_maps[plaintext[j]]))])
    if j < len(plaintext) - 1:
      if plaintext[j + 1] != " ":
        ciphertext += ","
  return ciphertext

# For Unit Test
if __name__ == "__main__":
  #plaintext_test = "revelation revering rightest impersonalize juliennes scientists reemphasizing propose crony bald pampering discharged lincoln authoresses interacted laked bedmaker intolerably beltlines warningly worldliness serologic bottom guessed hangup vitiates snaky polypous manifolding sweatshirt divisiveness decapitation musketry versers pizzas aperies reorganizes fender presentations thereuntil fly entrapped causewayed shaped freemasonry nudging efflorescence hydrated zazen exegeses fracas unprogressivel"
  #print enc_test_1(plaintext_test)
  #print test_2_plaintext_gen()
  # print enc_test_2(plaintext = test_2_plaintext_gen())[0]
  # print enc_test_2(plaintext = test_2_plaintext_gen())[1]
  plaintext =  test_2_plaintext_gen()
  print plaintext
  cipher =  enc_test_2(plaintext)
  print cipher
  print len(cipher)
