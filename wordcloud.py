import operator

class wordcloud(object):
  def __init__(self, w, l = [2,3,4]):
    self.word = w.decode('utf-8')
    self.l = l
    self.wordslist = self.makelist(self.word)[:]
    self.calfres = self.calfre()

  def makelist(self, word):
    ml = []
    for i in self.l:
      if len(word) >= i:
        add = i
        while add <= len(word):
          ml.append(word[0+add-i:add])
          add += 1
    return ml

  def calfre(self):
    re = {}
    for i in self.wordslist:
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

  def popsamewords(self):
    x = self.maketimesdict()
    xkeys = x.keys()
    xkeys.reverse()
    for i in xkeys:
      print i

      if i == 1:
        x.pop(i)
      else:
        if len(x[i]) > 1:
          for s in x[i]:
            mkl = self.makelist(s)
            for d in mkl[:-1]:
              try:
                x[i].remove(d)
              except ValueError:
                pass
    try:
      return x
    except KeyError:
      pass
