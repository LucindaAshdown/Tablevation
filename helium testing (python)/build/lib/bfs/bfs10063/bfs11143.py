def bfs11145(x, bfs11144):
  if (x == 0):
    return bfs11144[0]

  bfs11146 = []
  while x:
    bfs11146.append(bfs11144[(x % len(bfs11144))])
    x //= len(bfs11144)

  bfs11146.reverse()
  return ''.join(bfs11146)

def bfs11153(x, bfs11147):
  bfs11150 = 0
  bfs11151 = 0
  for bfs11152 in reversed(x):
    bfs11154 = bfs11147.index(bfs11152)
    bfs11150 += (bfs11154 * (len(bfs11147) ** bfs11151))
    bfs11151 += 1

  return bfs11150

