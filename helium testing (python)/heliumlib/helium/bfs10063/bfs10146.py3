def lower(text):
  bfs10150 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd'
  return ("translate(%s, '%s', '%s')" % (text, bfs10150, bfs10150.lower()))

def bfs10152(text, by=' '):
  return ("translate(%s, '\xa0', %r)" % (text, by))

def predicate(bfs10151):
  return (('[%s]' % bfs10151) if bfs10151 else '')

def bfs10154(*bfs10153):
  return predicate(' or '.join([c for c in bfs10153 if c ]))

