import re
import sys
def bfs10071(default=None):
  try:
    return (sys.stdout.encoding or default)
  except AttributeError:
    return default


def bfs10101(obj):
  if (isinstance(obj, str) and (sys.version_info[0] == 2)):
    bfs10070 = repr(obj)
    bfs10072 = re.search('[\'"]', bfs10070).start()
    bfs10073 = bfs10070[bfs10072]
    bfs10075 = False
    bfs10074 = (bfs10072 + 1)
    while (bfs10074 < len(bfs10070)):
      bfs10076 = bfs10070[bfs10074]
      if (bfs10076 == '\\'):
        bfs10075 = (not bfs10075)
      else:
        if ((bfs10076 == bfs10073) and (not bfs10075)):
          break

        bfs10075 = False

      bfs10074 += 1

    bfs10077 = bfs10071(default='unicode-escape')
    bfs10100 = obj.encode(bfs10077)
    if (bfs10077 == 'unicode-escape'):
      bfs10100 = bfs10100.replace('\\\\', '\\')

    return ((bfs10073 + bfs10100) + bfs10070[bfs10074:])

  return repr(obj)

