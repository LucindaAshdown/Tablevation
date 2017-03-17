from __future__ import absolute_import
from collections import namedtuple
from math import sqrt
class bfs10236(object):
  def __init__(self, bfs10240=0, bfs10242=0, width=0, height=0):
    self.bfs10240 = bfs10240
    self.bfs10242 = bfs10242
    self.bfs10241 = (bfs10240 + width)
    self.bfs10243 = (bfs10242 + height)

  @classmethod
  def bfs10245(bfs10244, width, height):
    return bfs10244(0, 0, width, height)

  @classmethod
  def bfs10250(bfs10244, bfs10246=None):
    if (bfs10246 is None):
      bfs10246 = (0, 0, 0, 0)

    return bfs10244(*bfs10246)

  @classmethod
  def bfs10253(bfs10247, bfs10251):
    return bfs10247.bfs10245(*bfs10251)

  @classmethod
  def bfs10255(bfs10252, struct):
    return bfs10252.bfs10254(struct.bfs10240, struct.bfs10242, struct.bfs10241, struct.bfs10243)

  @classmethod
  def bfs10254(bfs10244, bfs10256, bfs10257, bfs10261, bfs10260):
    return bfs10244(bfs10256, bfs10257, (bfs10261 - bfs10256), (bfs10260 - bfs10257))

  @property
  def width(self):
    return (self.bfs10241 - self.bfs10240)

  @property
  def height(self):
    return (self.bfs10243 - self.bfs10242)

  @property
  def center(self):
    return Point((self.bfs10240 + (self.width / 2)), (self.bfs10242 + (self.height / 2)))

  @property
  def bfs10263(self):
    return self.bfs10262(Point((self.bfs10241 - 1), self.center.y))

  @property
  def bfs10264(self):
    return Point(self.bfs10240, self.center.y)

  @property
  def bfs10266(self):
    return Point(self.center.x, self.bfs10242)

  @property
  def bfs10265(self):
    return self.bfs10262(Point(self.center.x, (self.bfs10243 - 1)))

  @property
  def bfs10267(self):
    return Point(self.bfs10263.x, self.bfs10266.y)

  @property
  def bfs10270(self):
    return Point(self.bfs10263.x, self.bfs10265.y)

  @property
  def bfs10272(self):
    return Point(self.bfs10264.x, self.bfs10265.y)

  @property
  def bfs10271(self):
    return Point(self.bfs10264.x, self.bfs10266.y)

  @property
  def bfs10273(self):
    if (not self):
      return 0

    return (self.width * self.height)

  def __contains__(self, bfs10274):
    return ((self.bfs10240 <= bfs10274.x < self.bfs10241) and (self.bfs10242 <= bfs10274.y < self.bfs10243))

  def translate(self, bfs10275, bfs10277):
    self.bfs10240 += bfs10275
    self.bfs10241 += bfs10275
    self.bfs10242 += bfs10277
    self.bfs10243 += bfs10277
    return self

  def bfs10262(self, bfs10276):
    return Point(min(max(bfs10276[0], self.bfs10240), max(self.bfs10240, (self.bfs10241 - 1))), min(max(bfs10276[1], self.bfs10242), max(self.bfs10242, (self.bfs10243 - 1))))

  def bfs10301(self, bfs10300):
    bfs10240 = max(self.bfs10240, bfs10300.bfs10240)
    bfs10242 = max(self.bfs10242, bfs10300.bfs10242)
    bfs10241 = min(self.bfs10241, bfs10300.bfs10241)
    bfs10243 = min(self.bfs10243, bfs10300.bfs10243)
    return (self.bfs10254(bfs10240, bfs10242, bfs10241, bfs10243) or bfs10236())

  def bfs10302(self, bfs10303):
    return bool(self.bfs10301(bfs10303))

  def bfs10304(self):
    return (slice(self.bfs10242, self.bfs10243), slice(self.bfs10240, self.bfs10241))

  def is_to_left_of(self, bfs10306):
    bfs10305 = (self.bfs10240 < bfs10306.bfs10240)
    bfs10307 = (self.bfs10242 <= bfs10306.bfs10242 < self.bfs10243)
    bfs10311 = (bfs10306.bfs10242 <= self.bfs10242 < bfs10306.bfs10243)
    return (bfs10305 and (bfs10307 or bfs10311))

  def is_to_right_of(self, bfs10310):
    return bfs10310.is_to_left_of(self)

  def is_above(self, bfs10312):
    bfs10314 = (self.bfs10242 < bfs10312.bfs10242)
    bfs10313 = (self.bfs10240 <= bfs10312.bfs10240 < self.bfs10241)
    bfs10315 = (bfs10312.bfs10240 <= self.bfs10240 < bfs10312.bfs10241)
    return (bfs10314 and (bfs10313 or bfs10315))

  def is_below(self, bfs10317):
    return bfs10317.is_above(self)

  def bfs10321(self, bfs10316, bfs10320):
    return getattr(self, ('is_' + bfs10316))(bfs10320)

  def bfs10332(self, bfs10323):
    bfs10322 = (self if (self.bfs10240 < bfs10323.bfs10240) else bfs10323)
    bfs10324 = (self if (bfs10322 == bfs10323) else bfs10323)
    bfs10325 = max(0, (bfs10324.bfs10240 - bfs10322.bfs10241))
    bfs10327 = (self if (self.bfs10242 < bfs10323.bfs10242) else bfs10323)
    bfs10326 = (self if (bfs10327 == bfs10323) else bfs10323)
    bfs10330 = max(0, (bfs10326.bfs10242 - bfs10327.bfs10243))
    return sqrt(((bfs10325 ** 2) + (bfs10330 ** 2)))

  def __eq__(self, bfs10331):
    if (not isinstance(bfs10331, bfs10236)):
      return False

    return ((self.bfs10240 == bfs10331.bfs10240) and (self.bfs10242 == bfs10331.bfs10242) and (self.bfs10241 == bfs10331.bfs10241) and (self.bfs10243 == bfs10331.bfs10243))

  def __ne__(self, bfs10333):
    return (not self.__eq__(bfs10333))

  def __nonzero__(self):
    return bool(((self.width > 0) and (self.height > 0)))

  def __repr__(self):
    return (type(self).__name__ + ('(left=%d, top=%d, width=%d, height=%d)' % (self.bfs10240, self.bfs10242, self.width, self.height)))

  def __hash__(self):
    return (((self.bfs10240 + (7 * self.bfs10242)) + (11 * self.bfs10241)) + (13 * self.bfs10243))


class Point(namedtuple('Point', ['x', 'y'])):
  def __new__(bfs10334, x=0, y=0):
    return bfs10334.__bases__[0].__new__(bfs10334, x, y)

  def __init__(self, x=0, y=0):
    pass

  @classmethod
  def bfs10337(bfs10244, bfs10335):
    return bfs10244(*bfs10335)

  def __eq__(self, bfs10336):
    return ((self.x, self.y) == bfs10336)

  def __ne__(self, bfs10340):
    return (not (self == bfs10340))

  def __add__(self, bfs10342):
    (bfs10341, bfs10343) = bfs10342
    return Point((self.x + bfs10341), (self.y + bfs10343))

  def __radd__(self, bfs10345):
    return self.__add__(bfs10345)

  def __sub__(self, bfs10344):
    (bfs10346, bfs10347) = bfs10344
    return Point((self.x - bfs10346), (self.y - bfs10347))

  def __rsub__(self, bfs10351):
    (x, y) = bfs10351
    (bfs10350, bfs10352) = self
    return Point((x - bfs10350), (y - bfs10352))

  def __mul__(self, bfs10354):
    if isinstance(bfs10354, (int, long, float)):
      return Point((self.x * bfs10354), (self.y * bfs10354))
    else:
      raise ValueError('Invalid argument')


  def __rmul__(self, bfs10353):
    return self.__mul__(bfs10353)

  def __div__(self, bfs10355):
    if isinstance(bfs10355, (int, long, float)):
      return Point((self.x / bfs10355), (self.y / bfs10355))
    else:
      raise ValueError('Invalid argument')


  def __nonzero__(self):
    return (bool(self.x) or bool(self.y))


class bfs10357(object):
  def __init__(self, bfs10356):
    self.bfs10356 = bfs10356

  def bfs10362(self, bfs10360, bfs10361):
    for offset in bfs10361:
      yield (bfs10360 + (offset * self.bfs10356))


  def bfs10364(self):
    return bool(self.bfs10356.x)

  def bfs10363(self):
    return (not self.bfs10364())

  @property
  def bfs10365(self):
    return Point((-self.bfs10356[1]), self.bfs10356[0])

  def __eq__(self, bfs10367):
    return (self.bfs10356 == bfs10367.bfs10356)

  def __repr__(self):
    for bfs10366 in dir(self.__module__):
      if (self == getattr(self.__module__, bfs10366)):
        return bfs10366




bfs10370 = bfs10357(Point(0, (-1)))
bfs10371 = bfs10357(Point(1, 0))
bfs10372 = bfs10357(Point(0, 1))
bfs10373 = bfs10357(Point((-1), 0))
