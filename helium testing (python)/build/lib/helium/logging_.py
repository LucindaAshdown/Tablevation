from helium.bfs10063.path import bfs11411
from logging import FileHandler
from os.path import dirname, join, expanduser
class FileHandlerRelativeToPackageOrUserDir(FileHandler):
  def __init__(self, bfs11410, bfs11412, mode='a'):
    if (bfs11410 == '~'):
      bfs11413 = join(expanduser(bfs11410), *bfs11412)
      bfs11411(dirname(bfs11413))
      FileHandler.__init__(self, bfs11413, mode=mode)
    else:
      bfs11415 = dirname(__import__(bfs11410).__file__)
      FileHandler.__init__(self, join(bfs11415, *bfs11412), mode=mode)



