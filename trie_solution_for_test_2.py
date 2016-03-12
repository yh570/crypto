import trie
import copy

KEY_TABLE = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [],'g': [],
              'h': [], 'i': [],'j': [], 'k': [], 'l': [],'m': [], 'n': [],
              'o': [],'p': [], 'q': [], 'r': [],'s': [], 't': [],
              'u': [],'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
KEY_LENGTH = {'a': 8, 'b': 1, 'c': 3, 'd': 4, 'e': 13, 'f': 2,'g': 2,
              'h': 6, 'i': 7,'j': 1, 'k': 1, 'l': 4,'m': 2, 'n': 7,
              'o': 8,'p': 2, 'q': 1, 'r': 6,'s': 6, 't': 9,
              'u': 3,'v': 1, 'w': 2, 'x': 1, 'y': 2, 'z': 1}
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def build_alphabet_trie():
  trie_alphabet = trie.Trie()
  f = open("english_words.txt")
  words = f.readlines()
  for word in words:
    trie_alphabet.build(word[:-2])
  return trie_alphabet

def check_assign_number_to_charactor(table):
  check_table = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [],'g': [],
                 'h': [], 'i': [],'j': [], 'k': [], 'l': [],'m': [], 'n': [],
                 'o': [],'p': [], 'q': [], 'r': [],'s': [], 't': [],
                 'u': [],'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
  for i in table:
    if table[i] != "":
      if table[i] not in check_table[table[i]]:
        check_table[table[i]].append(i)
  for i in check_table:
    if len(check_table[i]) > KEY_LENGTH[i]:
      return False
  return True

def check_legal_word(word, trie_alphabet):
  return trie_alphabet.find(word)

def check_legal_prefix(prefix, trie_alphabet):
  return trie_alphabet.find_prefix(prefix)

def add_to_table(i, ch, table):
  table[i] = ch;
  return table

def delete_from_table(i, ch, table):
  table[i] = ""
  return table

def table_to_plaintext(table, cipher_text_list):
  # print table
  plaintext = ""
  for word in cipher_text_list:
    for ch in word:
      if table[int(ch)] == '':
        plaintext += "*"
      else:
        plaintext += table[int(ch)]
    plaintext += " "
  return plaintext

def check_previous(prev_words):
  for word in prev_words:
    if check_legal_word(word, trie_alphabet) == False:
      return False
  return True

def search(trie_alphabet, table, i, current, prev_words):
  print current
  if i == len(wordchain) and check_assign_number_to_charactor(table) == True and check_legal_word(current, trie_alphabet) == True and check_previous(prev_words) == True:
    print table_to_plaintext(table, ll)
    print table #DEBUG
    print prev_words
    exit()
  if i in word_index:
    if check_legal_word(current, trie_alphabet) == True and check_assign_number_to_charactor(table) == True and check_previous(prev_words) == True:
      # print current, i
      prev_words.append(current)
      current = ""
    else:
      i = i - len(current)
      # prev_words.pop(-1)
      return
  if check_assign_number_to_charactor(table) == False:
    return
  if table[int(wordchain[i])] == "":
    for ch in alphabet:
      current += ch
      table = add_to_table(int(wordchain[i]), ch, table);
      if check_legal_prefix(current, trie_alphabet) == True and check_assign_number_to_charactor(table) == True and check_previous(prev_words) == True:
        # print i, 2 #DEBUG
        search(trie_alphabet, table, i + 1, current, prev_words)
      current = current[:-1]
      table = delete_from_table(int(wordchain[i]), ch, table)
  else:
    ch = table[int(wordchain[i])]
    current += ch
    table = add_to_table(int(wordchain[i]), ch, table);
    if check_legal_prefix(current, trie_alphabet) == True and check_assign_number_to_charactor(table) == True and check_previous(prev_words) == True:
      # print i, 1 #DEBUG
      search(trie_alphabet, table, i + 1, current, prev_words)
    current = current[:-1]
    table = delete_from_table(int(wordchain[i]), ch, table)





if __name__ == "__main__":
  #plaintext = "plunderable jawbreaker laundresses broncos dot siberia pastilles braced supernumerary risking creosotes sanatory befuddle fumes cesiums straitly redelivering buffeting appestat panelled hairlocks autogenesis biddies bazar neurology marital anodization dung logways feyest dismortgaged treats responses curia inexpensive hyperventilation gridlock menstruant bier locoed boogyman overprecisely muzzle bestowing amassed cosigns greeting repulsing shellacked mixture pommeled skiers fudging unlighted fetid simper tulip washroom singular studios reproachfully spectra wizard coopts synthesizing repackage waxings bellmen foreboded blowtubes parols unjustification rationalizations loran entrenchment smog latinize tactually swaps oversensitively orrery photosynthesizes rouging frizzly strapper saintdom ultramicrotome older vaginitis pyruvic bureaucratized topic equipments sillies sewage ventage blind creping stood barbarians"
  #ciphertext = "20,55,98,83,35,32,4,42,84,55,86 30,39,70,84,50,19,101,34,21,18 48,8,54,38,63,50,15,56,59,71,74 84,4,75,83,14,82,62 63,73,53 62,7,84,93,18,27,39 96,8,74,47,27,57,55,86,74 84,4,85,5,19,52 56,54,20,86,50,17,25,12,23,18,101,22,60 36,27,66,34,7,17,11 46,22,32,28,91,81,24,86,56 91,16,78,85,53,75,36,6 84,86,29,98,100,52,48,15 51,25,65,9,56 5,94,66,49,25,12,91 66,41,4,85,97,88,95,6 68,15,63,32,55,27,44,80,18,97,78,11 84,25,51,29,71,24,27,77,11 8,96,20,23,66,41,89,47 96,101,77,93,55,95,2,35 99,85,7,18,95,13,14,34,91 0,98,53,13,11,71,90,9,56,87,91 84,7,52,63,87,32,66 84,16,69,85,50 38,23,98,18,61,48,73,45,60 65,16,4,76,41,39,95 8,83,61,63,7,69,89,47,27,28,38 35,54,1,45 55,61,45,70,39,60,62 29,71,6,9,62,53 35,97,66,12,73,68,79,45,8,45,80,63 88,50,2,8,24,91 50,21,56,96,82,83,66,40,56 5,25,50,76,101 97,78,93,58,20,2,90,74,3,44,71 43,6,20,93,4,44,2,38,47,97,95,85,79,76,102,90 45,36,27,35,55,102,46,34 65,80,38,59,79,18,54,16,77,47 84,3,9,4 95,81,46,75,23,63 84,61,81,11,6,65,42,38 61,44,15,18,20,22,21,46,3,74,93,55,60 65,25,69,69,57,21 84,86,62,88,81,70,7,17,45 16,65,85,66,62,93,63 14,61,62,97,45,1,74 45,4,93,94,88,27,77,11 36,71,20,98,95,59,7,17,11 56,10,19,48,57,16,14,34,86,100 12,3,58,79,25,50,71 96,82,12,65,94,57,2,52 66,34,49,21,36,74 29,25,100,11,97,78,45 54,38,55,97,45,99,64,40,63 29,19,47,27,100 62,97,12,20,40,50 88,54,57,87,20 70,39,91,72,50,28,61,12 74,3,1,11,54,95,85,50 56,47,98,100,7,81,56 36,86,20,22,61,85,5,72,51,98,57,55,60 66,96,94,46,41,18,101 70,49,69,42,50,100 46,73,75,20,79,56 91,6,90,92,99,93,91,76,69,7,17,45 18,21,96,101,46,34,39,11,2 31,101,58,87,83,11,59 84,94,48,57,12,15,90 29,61,68,80,84,102,63,40,100 84,57,75,70,24,98,84,86,62 96,89,18,82,55,56 98,78,30,98,56,24,7,29,3,5,89,64,49,28,17 4,39,92,49,82,17,101,48,27,69,89,92,97,28,1,74 55,102,68,8,1 21,38,24,36,93,1,5,99,12,15,17,24 56,12,61,45 55,89,24,76,38,7,69,71 79,42,46,41,25,85,57,55,60 56,31,101,96,66 102,44,40,18,66,15,77,59,7,88,3,44,86,48,60 102,22,4,19,36,6 96,99,13,92,28,66,6,17,24,43,32,66,49,69,80,91 50,13,25,45,97,78,11 51,68,7,69,69,48,60 91,53,50,16,20,96,9,18 62,8,87,83,26,35,75,65 98,55,24,22,0,12,3,14,50,28,53,81,65,21 13,57,100,94,18 44,89,45,49,90,97,79,87,59 96,60,22,25,44,27,14 84,25,68,86,85,54,5,4,42,41,87,69,71,35 79,13,20,27,14 23,33,54,87,20,12,9,90,47,62 59,76,55,95,97,32,59 74,80,31,101,45,40 44,15,90,64,101,45,9 84,48,97,78,52 14,68,32,96,3,1,11 91,53,102,13,35 84,85,50,84,89,68,27,16,38,62"
  plaintext = "repel chrism selection choking castigated epicures knackeries canalize ripest subprincipals journalese document biffies scuppered reverters avowed maundies yeasted range politest tything zebra bwana killer survived"
  ciphertext = "88,7,78,72,22 27,86,6,35,69,66 11,7,23,72,28,67,45,48,102 28,40,89,71,4,102,31 21,90,5,17,42,18,73,20,29,92 72,24,35,27,68,83,9,11 71,70,73,27,71,96,56,35,101,54 28,32,59,94,84,34,41,96 83,35,24,9,5,36 54,68,47,24,82,4,102,21,35,24,90,74,54 81,8,68,83,63,94,84,39,69,33 57,0,27,68,66,96,62,20 47,60,100,19,34,29,69 54,21,75,24,78,39,88,33,92 82,7,58,72,6,67,25,83,54 26,58,64,77,7,61 66,26,75,70,57,45,33,69 12,7,30,5,17,15,43 6,73,63,31,65 78,38,22,45,52,25,44,37 55,12,3,2,60,53,31 41,25,47,82,32 47,97,46,102,73 71,34,74,84,39,88 44,91,82,58,42,58,96,61"
  cipher_text_list = ciphertext.split(" ")
  ll = []
  for word in cipher_text_list:
    ll.append(word.split(","))
  wordchain = []
  count = 0
  word_index = []
  for i in ll:
    wordchain += i
    count += len(i)
    word_index += [count]
  # print wordchain
  # print word_index
  table = {}
  for i in range(103):
    table[i] = ""
  trie_alphabet = build_alphabet_trie()
  # print trie_alphabet.find_prefix("")
  # print ll
  # print len(ciphertext)
  search(trie_alphabet = trie_alphabet, table = table, i = 0, current = "", prev_words = [])


