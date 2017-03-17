from os import listdir
from os.path import basename, dirname, join, splitext
import imp
import sys
def bfs10025():
  global bfs10024
  if (not bfs10024):
    if (sys.version_info[0] == 3):
      sys.meta_path.insert(0, bfs10026())

    bfs10024 = True


bfs10024 = False
def terminate():
  global bfs10024
  if bfs10024:
    bfs10027 = [bfs10030 for bfs10030 in sys.meta_path if isinstance(bfs10030, bfs10026) ]
    for bfs10031 in bfs10027:
      sys.meta_path.remove(bfs10031)

    bfs10024 = False


class bfs10026(object):
  def find_module(self, bfs10032, path=None):
    (bfs10033, bfs10035, bfs10034) = bfs10036(bfs10032, path)
    try:
      is_package = (bfs10034[2] == imp.PKG_DIRECTORY)
      if is_package:
        assert bfs10035
        bfs10035 = join(bfs10035, '__init__.py')

      if bfs10035:
        bfs10040 = (dirname(bfs10035) or '.')
        if ((basename(bfs10035) + '3') in listdir(bfs10040)):
          return bfs10037(bfs10032, (bfs10035 + '3'), bfs10034)


    finally:
      if bfs10033:
        bfs10033.close()




def bfs10036(name, path=None):
  bfs10041 = list(name.split('.'))
  bfs10042 = bfs10041[(-1)]
  bfs10043 = bfs10041[:(-1)]
  bfs10045 = path
  for (i, bfs10044) in enumerate(bfs10043):
    bfs10046 = '.'.join(bfs10043[:(i + 1)])
    try:
      bfs10047 = sys.modules[bfs10046]
    except KeyError:
      bfs10051 = imp.find_module(bfs10044, bfs10045)
      bfs10047 = imp.load_module(bfs10046, *bfs10051)

    bfs10045 = bfs10047.__path__

  return imp.find_module(bfs10042, bfs10045)

if (sys.version_info < (3, 1)):
  class bfs10037(object):
    def __init__(self, bfs10050, bfs10052, bfs10054):
      self.bfs10050 = bfs10050
      self.bfs10052 = bfs10052
      self.bfs10054 = bfs10054

    def load_module(self, bfs10050):
      if (bfs10050 != self.bfs10050):
        raise ImportError(('This loader cannot load module %s.' % bfs10050))

      bfs10053 = (self.bfs10054[1] or 'r')
      open_file = open(self.bfs10052, bfs10053)
      return imp.load_module(bfs10050, open_file, self.bfs10052, self.bfs10054)


else:
  try:
    from importlib.abc import SourceLoader
  except ImportError:
    from importlib.abc import PyLoader as SourceLoader

  class bfs10037(SourceLoader):
    def __init__(self, bfs10050, bfs10052, bfs10054):
      super(bfs10037, self).__init__()
      self.bfs10050 = bfs10050
      self.bfs10052 = bfs10052
      self.bfs10054 = bfs10054

    def get_data(self, file_path):
      return open(file_path, 'rb').read()

    def get_filename(self, bfs10050):
      if (bfs10050 != self.bfs10050):
        raise ImportError(('This loader cannot load module %s.' % bfs10050))

      return self.bfs10052

    def source_path(self, bfs10055):
      try:
        return self.get_filename(bfs10055)
      except ImportError:
        return None


    def is_package(self, bfs10056):
      bfs10057 = basename(self.get_filename(bfs10056))
      return (splitext(bfs10057)[0] == '__init__')

    @classmethod
    def module_repr(bfs10061, bfs10060):
      try:
        bfs10062 = (' from %r' % bfs10060.__file__)
      except AttributeError:
        bfs10062 = ''

      return ('<module %r%s>' % (bfs10060.__name__, bfs10062))



