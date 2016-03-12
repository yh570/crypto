class Trie:
  root = {}
  end = "/"
  def build(self, word):
    node = self.root
    for c in word:
      node = node.setdefault(c,{})
    node[self.end] = None

  def find(self, word):
    node = self.root
    for c in word:
      if c not in node:
        return False
      node = node[c]
    return self.end in node

  def find_prefix(self, prefix):
    node = self.root
    for c in prefix:
      if c not in node:
        return False
      node = node[c]
    return True


