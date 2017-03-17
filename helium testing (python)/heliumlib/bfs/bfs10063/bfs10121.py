from bfs.bfs10063.bfs10103 import bfs10117
import inspect
def bfs10141(bfs10122, args=None, bfs10124=None, bfs10123=repr):
  if (args is None):
    args = []

  if (bfs10124 is None):
    bfs10124 = {}

  (bfs10125, bfs10127, bfs10127, defaults) = inspect.getargspec(bfs10122)
  if bfs10117(bfs10122):
    bfs10125 = bfs10125[1:]

  bfs10126 = (0 if (defaults is None) else len(defaults))
  bfs10130 = (len(bfs10125) - bfs10126)
  bfs10132 = []
  for (i, bfs10131) in enumerate(bfs10125):
    bfs10133 = (i >= (len(bfs10125) - bfs10126))
    if bfs10133:
      bfs10135 = defaults[(i - bfs10130)]

    if (i < len(args)):
      value = args[i]
      prefix = ''
      bfs10134 = (bfs10133 and (value == bfs10135))
    elif (bfs10131 in bfs10124):
      value = bfs10124[bfs10131]
      prefix = (bfs10131 + '=')
      bfs10134 = (bfs10133 and (value == bfs10135))
    else:
      bfs10134 = True

    if (not bfs10134):
      bfs10132.append((prefix + bfs10123(value)))


  for bfs10136 in args[len(bfs10125):]:
    bfs10132.append(bfs10123(bfs10136))

  for bfs10137 in bfs10124:
    if (bfs10137 not in bfs10125):
      bfs10132.append(((bfs10137 + '=') + bfs10123(bfs10124[bfs10137])))


  return ', '.join(bfs10132)

def bfs10144(bfs10140, *args, **bfs10142):
  return ('%s(%s)' % (bfs10140.__name__, bfs10141(bfs10140, args, bfs10142)))

