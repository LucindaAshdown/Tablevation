from helium.bfs10063.bfs10146 import lower, bfs10152
class bfs10156(object):
  def bfs10146(self, value, text):
    raise NotImplementedError()

  def text(self, value, text):
    raise NotImplementedError()


class bfs10160(bfs10156):
  def bfs10146(self, value, text):
    if (not text):
      return ''

    if ('*' in text):
      bfs10161 = value
    else:
      bfs10161 = ("translate(%s, '*', '')" % value)

    if ("'" in text):
      text = ("concat('%s')" % '\',"\'",\''.join(text.split("'")))
    else:
      text = ("'%s'" % text)

    return ('starts-with(normalize-space(%s), %s)' % (lower(bfs10152(bfs10161)), text.lower()))

  def text(self, value, text):
    if (not text):
      return True

    return value.lower().lstrip().startswith(text.lower())


