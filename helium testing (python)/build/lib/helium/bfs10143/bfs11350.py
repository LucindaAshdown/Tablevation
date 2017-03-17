from datetime import date
from os import listdir
from os.path import join, getmtime
from tempfile import gettempdir
class bfs11375(object):
  bfs11376 = 1000
  def bfs11365(self):
    bfs11377 = date.today()
    bfs11401 = gettempdir()
    bfs11400 = 0
    for bfs11402 in listdir(bfs11401):
      file_path = join(bfs11401, bfs11402)
      try:
        bfs11403 = date.fromtimestamp(getmtime(file_path))
      except (OSError, ValueError):
        pass
      else:
        if (bfs11403 > bfs11377):
          bfs11377 = bfs11403

        bfs11400 += 1
        if (bfs11400 >= self.bfs11376):
          break



    return bfs11377


