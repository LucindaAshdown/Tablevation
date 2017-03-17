from helium.bfs10143.bfs10147 import bfs10163
from http.client import BadStatusLine
from base64 import b64encode
from logging import getLogger
from selenium.common.exceptions import WebDriverException
from socket import timeout
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import URLError
from helium.bfs10063.bfs10162 import bfs10166
class bfs10204(object):
  def bfs10206(self, bfs10203, bfs10205):
    raise NotImplementedError()


class bfs10207(bfs10204):
  def __init__(self, config):
    self.config = config

  def bfs10206(self, bfs10210, bfs10212):
    key = bfs10210.code
    if bfs10210.bfs10211:
      key += bfs10212.bfs10213()

    encode = (lambda s: b64encode(str(s).encode('ascii')))
    bfs10215 = {'email': bfs10210.bfs10214, 'key': key, 'p1': encode(bfs10212.bfs10216()), 'p2': encode(bfs10212.bfs10220()), 'p3': encode(bfs10212.bfs10217()), 'p4': encode(bfs10212.bfs10221()), 'p5': encode(bfs10212.bfs10222()), 'p6': encode(bfs10212.bfs10223()), 'p7': encode(bfs10212.bfs10225())}
    return self.get(self.config.bfs10224(bfs10215))

  def get(self, url):
    raise NotImplementedError()


class bfs10226(object):
  def __init__(self, url, bfs10230=None):
    self.url = url
    self.bfs10230 = (bfs10230 or {})

  def bfs10224(self, bfs10227):
    bfs10231 = self.bfs10230.copy()
    bfs10231.update(bfs10227)
    return (self.url + urlencode(bfs10231))


class bfs10232(bfs10207):
  def get(self, url):
    try:
      bfs10234 = urlopen(url, timeout=10)
    except URLError:
      getLogger(__name__).debug('Got URLError while trying to validate license online.', exc_info=True)
      raise bfs10163()
    except timeout:
      getLogger(__name__).warning('Connection to licensing server timed out.', exc_info=True)
      raise bfs10163()
    except BadStatusLine:
      raise bfs10163()

    return bfs10166(bfs10234.read().decode('ascii'))


class bfs10233(bfs10207):
  def __init__(self, config, bfs10235):
    super(bfs10233, self).__init__(config)
    self.bfs10235 = bfs10235

  def get(self, url):
    try:
      return self.bfs10235.execute_script(((('var request = new XMLHttpRequest();' + "request.open('GET', arguments[0], false);") + 'request.send(null);') + 'return request.responseText;'), url)
    except WebDriverException:
      raise bfs10163()



