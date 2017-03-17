from os.path import abspath, isdir, dirname, basename, join, pardir
import pkgutil
def bfs10067(bfs10065):
  bfs10064 = pkgutil.get_loader(bfs10065)
  try:
    filename = bfs10064.filename
  except AttributeError:
    filename = bfs10064.get_filename(bfs10065)

  bfs10066 = abspath(dirname(filename))
  is_package = (basename(filename) in ('__init__.py', '__init__.pyc'))
  if is_package:
    bfs10066 = abspath(join(bfs10066, pardir))

  while (not isdir(bfs10066)):
    bfs10066 = abspath(join(bfs10066, pardir))

  return bfs10066

