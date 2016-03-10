class PLAINTEXT:
  def __init__(self):
    self.english_words = []
    self.dictionary = []
    self._import_plaintext()


  def _import_plaintext(self):
    with open('english_words.txt','r') as f:
      for line in f:
        for word in line.split():      
          self.english_words.append(word)

    temp = []
    flag = 0

    with open('plaintext_dictionary.txt','r') as f:
      for line in f:
        for word in line.split():
          if word == '1':
            flag = 1
          elif word == '2':
            self.dictionary.append(temp)
            temp = []
            flag = 2
          elif word == '3':
            self.dictionary.append(temp)
            temp = []
            flag = 3
          elif word == '4':
            self.dictionary.append(temp)
            temp = []
            flag = 4
          elif word == '5':
            self.dictionary.append(temp)
            flag = 5
            temp = []
          elif flag > 0:
            temp.append(word)
      self.dictionary.append(temp)

    self.dictionary.append(["who", "are", "you", "bbb"])

