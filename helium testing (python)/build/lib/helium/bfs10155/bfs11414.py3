from bfs.bfs10143 import bfs10145
from bfs.bfs10143.bfs10147 import LicensingError
from bfs.bfs10143.bfs10210 import bfs11175
from bfs.bfs10063.bfs10212 import bfs11273
from datetime import date
from helium.bfs11304 import bfs11305, bfs11303
from helium.bfs10155 import APIImpl
from helium.bfs11316 import bfs11321, bfs11320
from helium.bfs10143.bfs10147 import NoLicenseKeyFound
from helium.bfs10143.bfs11330 import bfs11337, bfs11335
from helium.bfs10143.bfs10202 import bfs10226
from helium.bfs10143.bfs11350 import bfs11375
from helium.bfs10063.path import bfs11411
from helium.bfs10063.system import bfs10450
from logging import StreamHandler, Formatter, getLogger
from os.path import pardir, join, exists, dirname, normpath, expanduser
from shutil import copyfile
from uuid import uuid1, UUID
import helium
import logging.config
import sys
def excepthook(bfs11416, value, traceback):
  if isinstance(value, LicensingError):
    print(value.message)
  else:
    sys.__excepthook__(bfs11416, value, traceback)


sys.excepthook = excepthook
def bfs11423():
  global bfs11417
  if (bfs11417 is None):
    if bfs11320():
      bfs11417 = bfs11420()
    else:
      bfs11417 = bfs11421()


  return bfs11417

bfs11417 = None
class bfs11422(object):
  def __init__(self):
    self.bfs11424()
    self.bfs10155 = None

  def bfs11424(self):
    raise NotImplementedError()

  def APIImpl(self):
    if (self.bfs10155 is None):
      self.bfs10155 = APIImpl(self.bfs11321(), self.License(), self.bfs11426())

    return self.bfs10155

  def License(self):
    raise NotImplementedError()

  def bfs11321(self):
    raise NotImplementedError()

  def bfs11426(self):
    raise NotImplementedError()


class bfs11420(bfs11422):
  def __init__(self):
    super(bfs11420, self).__init__()
    self.license = self.bfs10471 = None

  def bfs11424(self):
    bfs11425 = StreamHandler()
    bfs11427 = Formatter('%(name)s %(levelname)s: %(message)s')
    bfs11425.setFormatter(bfs11427)
    getLogger('helium').addHandler(bfs11425)
    getLogger('bfs').addHandler(bfs11425)

  def License(self):
    if (self.license is None):
      self.license = bfs11335()

    return self.license

  def bfs11321(self):
    if (self.bfs10471 is None):
      bfs11430 = join(dirname(__file__), pardir, pardir, pardir, pardir, pardir)
      def bfs11432(bfs11431):
        return normpath(join(bfs11430, *bfs11431.split('/')))

      return bfs11321(bfs11432('../src/main/resources/base'), bfs11432(('../src/main/resources/' + bfs10450())), bfs11432('../target'))

    return self.bfs10471

  def bfs11426(self):
    return None


class bfs11421(bfs11422):
  def __init__(self):
    self.bfs11351 = self.bfs10212 = self.license = self.bfs10472 = self.uuid = self.bfs11433 = self.bfs11347 = self.bfs11350 = self.bfs10471 = None
    super(bfs11421, self).__init__()

  def bfs11424(self):
    import helium.logging_
    bfs11435 = self.bfs11321().bfs10514('logging.conf')
    if exists(bfs11435):
      logging.config.fileConfig(bfs11435)


  def bfs11273(self):
    if (self.bfs10212 is None):
      self.bfs10212 = bfs11273()

    return self.bfs10212

  def License(self):
    if (self.license is None):
      bfs11434 = self.bfs11305().bfs11311
      self.license = bfs11337(self.bfs11175(), self.bfs11273(), self.bfs11375(), self.bfs11436(), self.bfs11440(bfs11434))

    return self.license

  def bfs11440(self, bfs11437):
    bfs11441 = int(bfs11437[13])
    bfs11442 = int(bfs11437[3])
    bfs11444 = int(bfs11437[18])
    bfs11443 = int(bfs11437[29])
    bfs11445 = int(bfs11437[11])
    bfs11447 = int(bfs11437[2])
    bfs11446 = int(bfs11437[17])
    bfs11450 = int(bfs11437[31])
    year = ((((bfs11441 * 1000) + (bfs11442 * 100)) + (bfs11444 * 10)) + bfs11443)
    month = ((bfs11445 * 10) + bfs11447)
    day = ((bfs11446 * 10) + bfs11450)
    return date(year, month, day)

  def bfs11426(self):
    if (self.bfs10472 is None):
      bfs11313 = self.bfs11305().bfs11313
      bfs11312 = self.bfs11305().bfs11312
      bfs11314 = self.bfs11305().bfs11314
      version = self.bfs11305().bfs11307
      bfs11452 = {'version': version, 'computer_name': self.bfs11273().bfs11275(), 'identifier': self.UUID()}
      self.bfs10472 = bfs10226(('http://%s:%s%slicenses/verify?' % (bfs11313, bfs11312, bfs11314)), bfs11452)

    return self.bfs10472

  def UUID(self):
    self.bfs11451()
    return self.uuid

  def bfs11436(self):
    self.bfs11451()
    return self.bfs11351

  def bfs11451(self):
    bfs11453 = self.bfs11321().bfs10514('uuid')
    if exists(bfs11453):
      with open(bfs11453) as bfs11455:
        self.uuid = UUID(bfs11455.read())
        self.bfs11351 = False

    else:
      bfs11454 = uuid1()
      with open(bfs11453, 'w') as bfs11455:
        bfs11455.write(str(bfs11454))

      self.uuid = uuid1()
      self.bfs11351 = True


  def bfs11305(self):
    if (self.bfs11433 is None):
      self.bfs11433 = bfs11305(self.bfs11321().bfs10514(bfs11303))

    return self.bfs11433

  def bfs11175(self):
    if (self.bfs11347 is None):
      bfs11456 = 'No Helium license key found. Please contact us at contact@heliumhq.com or visit http://heliumhq.com to obtain a new one.'
      bfs11457 = join(expanduser('~'), '.helium', bfs10145)
      if (not exists(bfs11457)):
        bfs11461 = bfs11457
        bfs11457 = self.bfs11321().bfs10514(bfs10145)
        if (not exists(bfs11457)):
          raise NoLicenseKeyFound(bfs11456)

        bfs11411(dirname(bfs11461))
        copyfile(bfs11457, bfs11461)

      self.bfs11347 = bfs11175(bfs11457)

    return self.bfs11347

  def bfs11375(self):
    if (self.bfs11350 is None):
      self.bfs11350 = bfs11375()

    return self.bfs11350

  def bfs11321(self):
    if (self.bfs10471 is None):
      bfs11460 = dirname(helium.__file__)
      bfs11462 = join(bfs11460, 'data')
      bfs11464 = (bfs11462 if exists(bfs11462) else bfs11460)
      self.bfs10471 = bfs11321(bfs11464, join(bfs11464, bfs10450()))

    return self.bfs10471


