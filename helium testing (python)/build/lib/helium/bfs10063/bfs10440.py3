def bfs10442(bfs10437):
  bfs10441 = {}
  for (key, values) in list(bfs10437.items()):
    for value in values:
      if (value not in bfs10441):
        bfs10441[value] = set()

      bfs10441[value].add(key)


  return bfs10441

