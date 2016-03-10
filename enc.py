import random

DEBUG = 1

KEY_LENGTH = {'a': 8, 'b': 1, 'c': 3, 'd': 4, 'e': 13, 'f': 2,'g': 2,
              'h': 6, 'i': 7,'j': 1, 'k': 1, 'l': 4,'m': 2, 'n': 7,
              'o': 8,'p': 2, 'q': 1, 'r': 6,'s': 6, 't': 9,
              'u': 3,'v': 1, 'w': 2, 'x': 1, 'y': 2, 'z': 1}

def unknown_deterministic_algorithm(j, L, length_current_key):
  return j * L % length_current_key

def enc_test_1(plaintext):
  ciphertext = ""
  cipher_maps = {}
  L = 500
  for key in KEY_LENGTH:
    cipher_maps[key] = []
  cipher_randoms_gen = random.sample(xrange(0,103), 103)
  count = 0
  for key in KEY_LENGTH:
    for length_ch in range(KEY_LENGTH[key]):
      # print length_ch
      cipher_maps[key].append(cipher_randoms_gen[count])
      count += 1

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

  if ciphertext[-1] == ",":
    ciphertext = ciphertext[:-1]
  return ciphertext

if __name__ == "__main__":
  plaintext_test = "revelation revering rightest impersonalize juliennes scientists reemphasizing propose crony bald pampering discharged lincoln authoresses interacted laked bedmaker intolerably beltlines warningly worldliness serologic bottom guessed hangup vitiates snaky polypous manifolding sweatshirt divisiveness decapitation musketry versers pizzas aperies reorganizes fender presentations thereuntil fly entrapped causewayed shaped freemasonry nudging efflorescence hydrated zazen exegeses fracas unprogressivel"
  print enc_test_1(plaintext_test)
