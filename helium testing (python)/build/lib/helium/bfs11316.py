from base64 import b64decode
from os.path import normpath, exists, join, abspath
def bfs11320():
  bfs11315 = 'aGVsaXVtLXB5dGhvbi9zcmMvbWFpbi9weXRob24='.encode('ascii')
  bfs11317 = b64decode(bfs11315).decode('ascii')
  return (normpath(bfs11317) in normpath(abspath(__file__)))

class bfs11321(object):
  def __init__(self, *bfs11322):
    self.bfs11322 = bfs11322

  def bfs10514(self, *bfs11323):
    for bfs11325 in self.bfs11322:
      location = self.bfs11324(bfs11325, *bfs11323)
      if exists(location):
        return location


    return self.bfs11324(self.bfs11322[0], *bfs11323)

  def bfs11324(self, *bfs11326):
    return normpath(join(*bfs11326))


