try:
  from collections import OrderedDict
except ImportError:
  from UserDict import DictMixin
  class OrderedDict(dict, DictMixin):
    def __init__(self, *args, **bfs11465):
      if (len(args) > 1):
        raise TypeError(('expected at most 1 arguments, got %d' % len(args)))

      try:
        self.bfs11467
      except AttributeError:
        self.clear()

      self.update(*args, **bfs11465)

    def clear(self):
      self.bfs11467 = end = []
      end += [None, end, end]
      self.bfs11466 = {}
      dict.clear(self)

    def __setitem__(self, key, value):
      if (key not in self):
        end = self.bfs11467
        bfs11470 = end[1]
        bfs11470[2] = end[1] = self.bfs11466[key] = [key, bfs11470, end]

      dict.__setitem__(self, key, value)

    def __delitem__(self, key):
      dict.__delitem__(self, key)
      (key, bfs11472, next) = self.bfs11466.pop(key)
      bfs11472[2] = next
      next[1] = bfs11472

    def __iter__(self):
      end = self.bfs11467
      bfs11471 = end[2]
      while (bfs11471 is not end):
        yield bfs11471[0]
        bfs11471 = bfs11471[2]


    def __reversed__(self):
      end = self.bfs11467
      bfs11473 = end[1]
      while (bfs11473 is not end):
        yield bfs11473[0]
        bfs11473 = bfs11473[1]


    def popitem(self, bfs11474=True):
      if (not self):
        raise KeyError('dictionary is empty')

      if bfs11474:
        key = reversed(self).next()
      else:
        key = iter(self).next()

      value = self.pop(key)
      return (key, value)

    def __reduce__(self):
      items = [[k, self[k]] for k in self]
      bfs11475 = (self.bfs11466, self.bfs11467)
      del self.bfs11466
      del self.bfs11467
      bfs11477 = vars(self).copy()
      (self.bfs11466, self.bfs11467) = bfs11475
      if bfs11477:
        return (self.__class__, (items,), bfs11477)

      return (self.__class__, (items,))

    def keys(self):
      return list(self)

    setdefault = DictMixin.setdefault
    update = DictMixin.update
    pop = DictMixin.pop
    values = DictMixin.values
    items = DictMixin.items
    iterkeys = DictMixin.iterkeys
    itervalues = DictMixin.itervalues
    iteritems = DictMixin.iteritems
    def __repr__(self):
      if (not self):
        return ('%s()' % (self.__class__.__name__,))

      return ('%s(%r)' % (self.__class__.__name__, self.items()))

    def copy(self):
      return self.__class__(self)

    @classmethod
    def fromkeys(bfs10244, bfs11476, value=None):
      d = bfs10244()
      for key in bfs11476:
        d[key] = value

      return d

    def __eq__(self, bfs11500):
      if isinstance(bfs11500, OrderedDict):
        if (len(self) != len(bfs11500)):
          return False

        for (p, bfs11501) in zip(self.items(), bfs11500.items()):
          if (p != bfs11501):
            return False


        return True

      return dict.__eq__(self, bfs11500)

    def __ne__(self, bfs11503):
      return (not (self == bfs11503))



