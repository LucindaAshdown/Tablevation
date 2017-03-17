from html.parser import HTMLParser
import re
def bfs10166(bfs10164):
  s = bfs10165()
  s.feed(bfs10164)
  return s.get_data()

class bfs10165(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.reset()
    self.bfs10170 = []

  def handle_data(self, d):
    self.bfs10170.append(d)

  def get_data(self):
    return ''.join(self.bfs10170)


def bfs10200(bfs10167):
  bfs10167 = bfs10171(bfs10167)
  try:
    bfs10172 = (bfs10167.index('>') + 1)
    bfs10174 = bfs10167.rindex('<', bfs10172)
  except ValueError:
    return bfs10167

  bfs10173 = bfs10167[:bfs10172]
  bfs10175 = bfs10167[bfs10174:]
  bfs10176 = bfs10167[bfs10172:bfs10174]
  if (('<' in bfs10176) or (len(bfs10176) > 60)):
    return ('%s...%s' % (bfs10173, bfs10175))
  else:
    return bfs10167


def bfs10171(bfs10177):
  bfs10201 = bfs10177.strip()
  bfs10201 = re.sub('\\s+', ' ', bfs10201)
  bfs10201 = bfs10201.replace('> ', '>').replace(' <', '<')
  return bfs10201

