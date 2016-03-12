import enc
import fileread
import time
from copy import deepcopy

KEY_TABLE = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [],'g': [], 
              'h': [], 'i': [],'j': [], 'k': [], 'l': [],'m': [], 'n': [], 
              'o': [],'p': [], 'q': [], 'r': [],'s': [], 't': [], 
              'u': [],'v': [], 'w': [], 'x': [], 'y': [], 'z': []}

KEY_LENGTH = {'a': 8, 'b': 1, 'c': 3, 'd': 4, 'e': 13, 'f': 2,'g': 2, 
              'h': 6, 'i': 7,'j': 1, 'k': 1, 'l': 4,'m': 2, 'n': 7, 
              'o': 8,'p': 2, 'q': 1, 'r': 6,'s': 6, 't': 9, 
              'u': 3,'v': 1, 'w': 2, 'x': 1, 'y': 2, 'z': 1}


def find_repeat_numbers(ciphertext):
  repeat_numbers_table = {}
  for i in range(103):
    repeat_numbers_table[i] = []
  cipher_text_list = ciphertext.split(" ")
  print "#1"
  print cipher_text_list
  ll = []
  for word in cipher_text_list:
    ll.append(word.split(","))
  print "#2"
  print ll
  for number in range(103):
    for word in ll:
      if str(number) in word:
          repeat_numbers_table[number].append(word)
  return repeat_numbers_table

def get_length_table(ciphertext):
  length_table = {}
  cipher_text_list = ciphertext.split(" ")
  ll = []
  for word in cipher_text_list:
    ll.append(word.split(","))
  for charactor_len in range(1,20):
    length_table[charactor_len] = []
  for word in ll:
    length_table[len(word)].append(word)
  return length_table

def len_distribution_english_words():
  f = open("english_words.txt")
  words = f.readlines()
  length_table = {}
  for charactor_len in range(1,50):
    length_table[charactor_len] = 0
  for word in words:
    length_table[len(word) - 2] += 1
  return length_table

def setup_list(length):
  temp_list = []
  plaintext = fileread.PLAINTEXT()
  for words in plaintext.english_words:
    if len(words) == length:
      temp_list.append(words)
  return temp_list


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

def reset_dictionary(num_to_key):
  temp_dic = deepcopy(KEY_TABLE)
  for key, value in num_to_key.iteritems():
    temp_dic[value].append(key)
  return temp_dic



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
  plaintext = "plunderable jawbreaker laundresses broncos dot siberia pastilles braced supernumerary risking creosotes sanatory befuddle fumes cesiums straitly redelivering buffeting appestat panelled hairlocks autogenesis biddies bazar neurology marital anodization dung logways feyest dismortgaged treats responses curia inexpensive hyperventilation gridlock menstruant bier locoed boogyman overprecisely muzzle bestowing amassed cosigns greeting repulsing shellacked mixture pommeled skiers fudging unlighted fetid simper tulip washroom singular studios reproachfully spectra wizard coopts synthesizing repackage waxings bellmen foreboded blowtubes parols unjustification rationalizations loran entrenchment smog latinize tactually swaps oversensitively orrery photosynthesizes rouging frizzly strapper saintdom ultramicrotome older vaginitis pyruvic bureaucratized topic equipments sillies sewage ventage blind creping stood barbarians"
  ciphertext = "62,20,6,26 4,90,61,42,79,67,14,7,63,90,71,84,20,17,7,73,19 16,51,61,72,71,12,31,21,35,34,50,83,56 40,90,57,7,4,83,86,88,56 13,54,12,5,71,99,4,7,81,24 11,50,57,25,90,71,81,72,22,64,52,13 42,46,81,54,71,78,15,33,27,89,4 19,93,18,84,94,77,102,39,55,73 23,17,36,25,88,49,67,47 2,53,3,75,0,96,47 48,12,13,93,94,76,7,63,13 41,98,86,52,102,54,14 93,17,80,48,13,97,59,62 7,55,88,42,61,16,17,1,48,96,78 82,16,6,32,83,56 32,90,34,77,12,38 62,54,18,5,57,61,3,71 52,8,55,101,87,85,86,22,47,83,56 15,33,7,15,58,90,80,77,74,73 44,45,46,16,62 63,86,43,31,30,79,51,56 1,84,43,64,29,24,65,97,13 64,52,29,77,79,67,86,21,9,82 1,68,72,14,98,57,90,101,84,68,17 78,5,83,72,15,43,83,56"
  length_table = get_length_table(ciphertext)
  num_to_key = {}

  length = max(length_table.keys())
  table = len_distribution_english_words()
  list_dic = {}
  list_dic[length] = setup_list(length)

  temp_cipher = text_to_num_list(ciphertext)
  sorted_cipher = deepcopy(temp_cipher)
  sorted_cipher.sort(key = len, reverse = True)

  start_time = time.time()
  num_text = assign_key(sorted_cipher)

  print num_text
  string = ""

  for num in temp_cipher:
    for i in num:
      string += num_text[i]
    string += ' '

  print string
  print("--- %s seconds ---" % (time.time() - start_time))
