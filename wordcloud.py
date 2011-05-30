class wordcloud(object):
  def __init__(self, w, l = [2,3,4]):
    self.word = w.decode('utf-8')
    self.l = l

  def getlens(self):
    return len(self.word)

  def cklens(self, l):
    return len(self.word) >= l

  def makelist(self):
    self.ml = []
    for i in self.l:
      if self.cklens(i):
        add = i
        while add <= self.getlens():
          self.ml.append(self.word[0+add-i:add])
          add += 1
    return self.ml
