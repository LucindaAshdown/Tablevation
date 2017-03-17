from errno import EEXIST
from os.path import split, isdir
from os import makedirs
def bfs11406(path):
  bfs11405 = []
  while True:
    (path, bfs11404) = split(path)
    if (bfs11404 != ''):
      bfs11405.append(bfs11404)
    else:
      if (path != ''):
        bfs11405.append(path)

      break


  return list(reversed(bfs11405))

def bfs11411(path):
  try:
    makedirs(path, exist_ok=True)
  except TypeError:
    try:
      makedirs(path)
    except OSError as bfs11407:
      if ((bfs11407.errno == EEXIST) and isdir(path)):
        pass
      else:
        raise 




