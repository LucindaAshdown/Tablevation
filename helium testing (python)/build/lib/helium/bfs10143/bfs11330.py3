from datetime import date
from bfs.bfs10143.bfs10147 import LicenseInvalid
from helium.bfs10143.bfs10147 import bfs10163
from logging import getLogger
from random import Random
class License(object):
  def bfs10530(self, bfs11327):
    bfs11331 = self.bfs11332(bfs11327)
    if (not bfs11331):
      raise LicenseInvalid(bfs11331.message)


  def bfs11332(self, bfs11333):
    raise NotImplementedError()


class bfs11335(License):
  def bfs11332(self, bfs11334):
    return bfs11336(True, 'Development license (eternally valid).')


class bfs11337(License):
  bfs11341 = 0
  bfs11340 = 1
  bfs11342 = 'dstn;heaf402321'
  bfs11343 = 'Unfortunately, your Helium license has expired. Please obtain a new one from\n\thttp://heliumhq.com'
  bfs11344 = 'Unfortunately, your Helium license is already in use on another computer. To use it on this machine, please contact support at\n\thttp://heliumhq.com'
  bfs11346 = 'Unfortunately, your Helium license is invalid. Please obtain a new one from\n\thttp://heliumhq.com'
  bfs11345 = 'Unfortunately, your license is not valid for this version of Helium. Please go to http://heliumhq.com/pricing or contact us at contact@heliumhq.com to renew.'
  def __init__(self, bfs11347, bfs10212, bfs11350, bfs11351, bfs11352, seed=None):
    self.bfs10210 = bfs11347.read()
    self.bfs11347 = bfs11347
    self.bfs10212 = bfs10212
    self.bfs11350 = bfs11350
    self.bfs11351 = bfs11351
    self.bfs11352 = bfs11352
    self.random = Random(seed)
    self.bfs11353 = None

  def bfs11332(self, bfs11355):
    if (self.bfs11353 is None):
      self.bfs11353 = self.bfs11354(bfs11355)

    return self.bfs11353

  def bfs11354(self, bfs11356):
    if self.bfs11360():
      return bfs11336(False, self.bfs11343)

    if (not self.bfs11357()):
      return bfs11336(False, self.bfs11345)

    if self.bfs11361():
      return self.bfs11362(bfs11356)

    return bfs11336(True, ('Licensed to ' + self.bfs10210.bfs10214))

  def bfs11360(self):
    bfs11363 = self.bfs11350.bfs11365()
    return self.bfs10210.bfs11173(bfs11363)

  def bfs11357(self):
    bfs11163 = self.bfs10210.bfs11163
    if (bfs11163 is None):
      bfs11364 = dict(((suffix, date(year, month, day))  for (suffix, year, month, day) in [('r7', 2017, 4, 18), ('dP', 2017, 3, 24), ('dx', 2017, 3, 8), ('K2', 2017, 3, 7), ('IU', 2016, 12, 22), ('Vu', 2016, 12, 16), ('ul', 2016, 12, 16), ('tp', 2016, 11, 23), ('bo', 2016, 10, 23), ('SD', 2016, 10, 6), ('b-', 2016, 10, 5), ('-m', 2016, 10, 5), ('ck', 2016, 10, 5), ('tv', 2016, 10, 5), ('MP', 2016, 10, 5), ('bl', 2016, 10, 5), ('Nw', 2016, 10, 5), ('mV', 2016, 10, 5), ('Wm', 2016, 10, 5), ('Rp', 2016, 10, 5), ('Wk', 2016, 10, 5), ('ZR', 2016, 10, 5), ('E3', 2016, 10, 5), ('at', 2016, 10, 5), ('m/', 2016, 10, 5), ('rG', 2016, 10, 5), ('4x', 2016, 10, 5), ('5d', 2016, 10, 5), ('6S', 2016, 10, 5), ('Af', 2016, 10, 5), ('Uo', 2016, 10, 5), ('tO', 2016, 10, 5), ('BN', 2016, 10, 5), ('aB', 2016, 10, 5), ('vi', 2016, 10, 5), ('RW', 2016, 10, 5), ('ft', 2016, 10, 5), ('gG', 2016, 10, 5), ('2n', 2016, 10, 5), ('a7', 2016, 10, 5), ('jH', 2016, 10, 5), ('h6', 2016, 10, 5), ('VW', 2016, 10, 5), ('DB', 2016, 10, 5), ('Kl', 2016, 10, 5), ('i/', 2016, 10, 5), ('FH', 2016, 10, 5), ('cE', 2016, 10, 5), ('af', 2016, 10, 5), ('iL', 2016, 10, 5), ('Io', 2016, 10, 5), ('l1', 2016, 10, 5), ('KP', 2016, 10, 5), ('WU', 2016, 10, 5), ('mK', 2016, 10, 5), ('SY', 2016, 10, 5), ('6-', 2016, 10, 5), ('0Q', 2016, 10, 5), ('Eq', 2016, 10, 5), ('s0', 2016, 10, 5), ('sZ', 2016, 10, 4), ('2O', 2016, 10, 4), ('tz', 2016, 10, 4), ('bf', 2016, 9, 30), ('eo', 2016, 9, 30), ('AE', 2016, 9, 20), ('Xf', 2016, 9, 20), ('G2', 2016, 8, 18), ('Rl', 2016, 6, 15), ('yZ', 2016, 6, 14), ('Bu', 2016, 5, 25), ('mD', 2016, 5, 7), ('Xn', 2016, 5, 5), ('xN', 2016, 5, 5), ('WA', 2016, 5, 5), ('Va', 2016, 4, 13), ('ct', 2016, 3, 23), ('H4', 2016, 3, 23), ('SK', 2016, 3, 23), ('O-', 2016, 2, 9), ('lS', 2015, 12, 29), ('qX', 2015, 12, 29), ('fY', 2016, 1, 1), ('Ru', 2016, 1, 1), ('y2', 2016, 1, 1), ('QL', 2015, 11, 6), ('eR', 2015, 11, 6), ('uB', 2023, 9, 8)]))
      bfs11163 = bfs11364[self.bfs10210.code[(-2):]]

    return (self.bfs11352 <= bfs11163)

  def bfs11361(self):
    if self.bfs10210.bfs10211:
      if (not self.bfs10210.bfs11172()):
        return True

      if self.bfs11366():
        return True


    if self.bfs10210.bfs11160:
      return (self.bfs11351 or (self.random.random() <= 0.05))

    return False

  def bfs11366(self):
    bfs11367 = self.bfs10212.bfs10213()
    bfs11371 = self.bfs10210.bfs11164
    return (bfs11367 != bfs11371)

  def bfs11362(self, bfs11370):
    bfs11372 = bfs11370.bfs10206(self.bfs10210, self.bfs10212)
    bfs10211 = self.bfs10210.bfs10211
    if (not bfs11372):
      if (bfs10211 and self.bfs11366()):
        return bfs11336(False, self.bfs11344)
      else:
        return bfs11336(False, self.bfs11346)

    else:
      if (bfs11372 == self.bfs11342):
        bfs11374 = (not bfs10211)
      else:
        if (not bfs10211):
          bfs11374 = False
        else:
          try:
            self.bfs10210.bfs11174(bfs11372)
          except ValueError as bfs11373:
            raise bfs10163(bfs11373)

          bfs11374 = (not self.bfs11366())
          if bfs11374:
            try:
              self.bfs11347.write(self.bfs10210)
            except (OSError, IOError):
              getLogger(__name__).warn('Could not write to license file %s.', self.bfs11347.file_path, exc_info=True)




      if bfs11374:
        message = ('Licensed to ' + self.bfs10210.bfs10214)
      else:
        message = self.bfs11346


    return bfs11336(bfs11374, message)


class bfs11336(object):
  def __init__(self, bfs11332, message):
    self.bfs11332 = bfs11332
    self.message = message

  def __bool__(self):
    return self.bfs11332


