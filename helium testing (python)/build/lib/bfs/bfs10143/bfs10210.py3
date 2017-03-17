from base64 import b64decode
from bfs.bfs10143.bfs10147 import InvalidLicenseFile
from bfs.bfs10063.bfs11143 import bfs11153, bfs11145
from datetime import date, datetime
from math import ceil, log
from os import path
from pkcs1 import rsaes_oaep
from pkcs1.keys import RsaPrivateKey
bfs11155 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-/'
class bfs11156(object):
  bfs11157 = 32
  def __init__(self, bfs10214, code, bfs11161=None, encrypted_node_identifier='', bfs10211=True, bfs11160=True, bfs11162=False, bfs11163=None, bfs11165=None):
    self.bfs10214 = bfs10214
    self.code = code
    self.bfs11161 = bfs11161
    self.encrypted_node_identifier = encrypted_node_identifier
    self.bfs10211 = bfs10211
    self.bfs11160 = bfs11160
    self.bfs11162 = bfs11162
    self.bfs11163 = bfs11163
    self.bfs11165 = bfs11165

  @property
  def bfs11164(self):
    if (not self.encrypted_node_identifier):
      return self.encrypted_node_identifier

    return self.decrypt(self.encrypted_node_identifier)

  @classmethod
  def decrypt(bfs11166, bfs11170):
    n = 126552595132100767496431298900695851144633929478317947845463894147101930730111564183119259440078050133900835449855213073742144369102834189244736695982848189036861833523332376016102290780726072320885243610990871511351145548702602510026707584848724238826408910261032648966390926399187028038467973734166869523139
    d = 47620634886441811911279006701406234418386824768677219155850665937740218712105852942916277172463872230223057250543653350192334441406304742984336354420144630234029397102707344769401491936717749314553261859131919096126529291266317948550850549782633820140042213874431692820120174629881124487475541748108487115593
    bfs11167 = RsaPrivateKey(n, d)
    return rsaes_oaep.decrypt(bfs11167, b64decode(bfs11170)).decode('ascii')

  def bfs11173(self, bfs11171=None):
    if (not self.bfs11162):
      return False

    return (self.bfs11163 < (date.today() if (bfs11171 is None) else bfs11171))

  def bfs11172(self):
    return bool(self.encrypted_node_identifier)

  def bfs11174(self, encrypted_node_identifier):
    try:
      self.decrypt(encrypted_node_identifier)
    except:
      raise ValueError(('Not a valid encrypted node identifier: %s' % encrypted_node_identifier))

    if self.bfs10211:
      self.encrypted_node_identifier = encrypted_node_identifier



class bfs11175(object):
  def __init__(self, file_path, bfs11177=None):
    if (bfs11177 is None):
      bfs11177 = []

    self.file_path = file_path
    self.bfs11177 = bfs11177

  def read(self):
    (bfs11176, key) = self.bfs11200()
    bfs11202 = bfs11201(self.bfs11177)
    bfs11203 = bfs11202.parse(bfs11176, key)
    bfs11203.bfs11161 = self.bfs11161
    return bfs11203

  def bfs11200(self):
    with open(self.file_path, 'r') as bfs11205:
      bfs11204 = bfs11205.readline().rstrip()
      key = bfs11205.readline().rstrip()
      if ((not bfs11204) or (not key)):
        raise InvalidLicenseFile()

      return (bfs11204, key)


  def write(self, bfs11206):
    with open(self.file_path, 'w') as bfs11210:
      bfs11210.write((bfs11206.bfs10214 + '\n'))
      key = bfs11206.code
      if bfs11206.bfs10211:
        key += bfs11206.encrypted_node_identifier

      bfs11210.write((key + '\n'))


  def exists(self):
    return path.exists(self.file_path)

  @property
  def bfs11161(self):
    return datetime.fromtimestamp(path.getmtime(self.file_path))


class bfs11201(object):
  def __init__(self, bfs11177=None):
    if (bfs11177 is None):
      bfs11177 = []

    self.bfs11177 = bfs11177

  def parse(self, bfs11207, key):
    code = key[:bfs11156.bfs11157]
    bfs11211 = key[bfs11156.bfs11157:]
    try:
      if (code in self.bfs11177):
        return self.bfs11212(bfs11207, code, bfs11211)
      else:
        return self.bfs11213(bfs11207, code, bfs11211)

    except ValueError:
      return bfs11156(bfs11207, code, encrypted_node_identifier=bfs11211)


  def bfs11212(self, bfs11214, code, encrypted_node_identifier):
    bfs11215 = True
    bfs11217 = True
    bfs11216 = False
    bfs11220 = None
    try:
      bfs11222 = int(code[:1])
    except ValueError:
      bfs11222 = None

    return bfs11156(bfs11214, code, None, encrypted_node_identifier, bfs11215, bfs11217, bfs11216, bfs11220, bfs11222)

  def bfs11213(self, bfs11221, code, encrypted_node_identifier):
    bfs11223 = bfs11224(code)
    bfs10211 = bfs11223.bfs10211
    bfs11160 = bfs11223.bfs11160
    bfs11162 = bfs11223.bfs11162
    bfs11163 = bfs11223.bfs11163
    bfs11165 = bfs11223.bfs11165
    return bfs11156(bfs11221, code, None, encrypted_node_identifier, bfs10211, bfs11160, bfs11162, bfs11163, bfs11165)


class bfs11226:
  bfs11225 = 0
  bfs11227 = 1
  bfs11231 = 2
  bfs11230 = 3
  bfs11232 = 4
  bfs11234 = 5
  bfs11233 = 6

class bfs11224(object):
  bfs11235 = [(bfs11226.bfs11225, 5), (bfs11226.bfs11227, 1), (bfs11226.bfs11231, 1), (bfs11226.bfs11230, 1), (bfs11226.bfs11232, 7), (bfs11226.bfs11234, 4), (bfs11226.bfs11233, 5)]
  def __init__(self, code):
    self.code = code
    bfs11236 = self.bfs11237(self.code)
    self.bfs11165 = self.bfs11241(bfs11236, bfs11226.bfs11225)
    self.bfs11160 = (self.bfs11241(bfs11236, bfs11226.bfs11227) > 0)
    self.bfs10211 = (self.bfs11241(bfs11236, bfs11226.bfs11231) > 0)
    self.bfs11162 = (self.bfs11241(bfs11236, bfs11226.bfs11230) > 0)
    bfs11240 = self.bfs11241(bfs11236, bfs11226.bfs11232)
    bfs11242 = self.bfs11241(bfs11236, bfs11226.bfs11234)
    bfs11243 = self.bfs11241(bfs11236, bfs11226.bfs11233)
    if ((bfs11240 != (-1)) and (bfs11242 != (-1)) and (bfs11243 != (-1))):
      self.bfs11163 = date((bfs11240 + 2000), bfs11242, bfs11243)
    else:
      self.bfs11163 = None


  def bfs11237(self, text):
    bfs11244 = 6
    assert (len(bfs11155) == (2 ** bfs11244))
    bfs11246 = ''
    for bfs11245 in text:
      bfs11247 = bfs11145(bfs11153(bfs11245, bfs11155), '01')
      while (len(bfs11247) < bfs11244):
        bfs11247 = ('0' + bfs11247)

      bfs11246 += bfs11247

    bfs11250 = (len(text) * bfs11244)
    bfs11251 = int(ceil((log(bfs11250) / log(2))))
    bfs11253 = bfs11246[:bfs11251]
    bfs11252 = bfs11153(bfs11253, '01')
    return bfs11246[bfs11251:(bfs11251 + bfs11252)]

  def bfs11241(self, bfs11254, bfs11256):
    offset = 0
    (bfs11255, bfs11257) = list(zip(*self.bfs11235))
    bfs11261 = bfs11255.index(bfs11256)
    for index in range(0, bfs11261):
      offset += bfs11257[index]

    if (len(bfs11254) <= offset):
      return (-1)

    return bfs11153(bfs11254[offset:(offset + bfs11257[bfs11255.index(bfs11256)])], '01')


