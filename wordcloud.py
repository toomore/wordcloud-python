import operator

class wordcloud(object):
  def __init__(self, w, l = [2,3,4]):
    self.word = w.decode('utf-8')
    self.l = l
    self.makelist()
    self.calfres = self.calfre()

  def getlens(self):
    return len(self.word)

  def getwords(self):
    return self.calwords.keys()

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

  def calfre(self):
    re = {}
    for i in self.ml:
      try:
        re[i] += 1
      except KeyError:
        re[i] = 1
    self.calwords = re
    x = sorted(re.iteritems(), key=operator.itemgetter(1),reverse=True)
    return x

  def maketimesdict(self):
    re = {}
    for i in self.calwords:
      try:
        re[self.calwords[i]].append(i)
      except KeyError:
        re[self.calwords[i]] = []
        re[self.calwords[i]].append(i)
    return re
