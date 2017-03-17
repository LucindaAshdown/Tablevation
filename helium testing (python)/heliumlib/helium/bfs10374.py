from bfs.bfs10063.bfs10237 import bfs10236
from decorator import decorator
from selenium.common.exceptions import StaleElementReferenceException, NoSuchFrameException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from urllib2 import URLError
import sys
class bfs10376(object):
  def __init__(self, target):
    self.target = target

  def __getattr__(self, item):
    return getattr(self.target, item)

  def unwrap(self):
    return self.target

  def __hash__(self):
    return hash(self.target)

  def __eq__(self, bfs10375):
    return (self.target == bfs10375.target)

  def __ne__(self, bfs10377):
    return (not (self == bfs10377))


class bfs10400(bfs10376):
  def __init__(self, target):
    super(bfs10400, self).__init__(target)
    self.bfs10401 = None

  def bfs10402(self):
    return ActionChains(self.target)

  def bfs10403(self, web_element):
    if (not self.bfs10401):
      return 0

    if hasattr(self.bfs10401, 'location'):
      try:
        bfs10404 = self.bfs10401.location
      except StaleElementReferenceException:
        return 0
      else:
        return bfs10404.bfs10332(web_element.location)

    else:
      return 0


  def find_elements_by_name(self, name):
    return (self.target.find_elements_by_name(name) or [])

  def find_elements_by_xpath(self, bfs10405):
    return (self.target.find_elements_by_xpath(bfs10405) or [])

  def find_elements_by_css_selector(self, bfs10406):
    return (self.target.find_elements_by_css_selector(bfs10406) or [])

  def bfs10407(self):
    return (self.browser_name == 'firefox')

  @property
  def browser_name(self):
    return self.target.capabilities['browserName']

  def bfs10411(self):
    return (self.browser_name == 'internet explorer')


@decorator
def bfs10415(bfs10104, *args, **bfs10410):
  try:
    return bfs10104(*args, **bfs10410)
  except URLError, bfs10412:
    if bfs10413(bfs10412):
      raise StaleElementReferenceException('The Selenium server this element belonged to is no longer available.')
    else:
      raise 



def bfs10413(bfs10414):
  try:
    bfs10416 = 10061
    return (bfs10414.args[0][0] == bfs10416)
  except (IndexError, TypeError):
    return False


@decorator
def bfs10424(bfs10104, self, *args, **bfs10420):
  if (not self.bfs10417):
    return bfs10104(self, *args, **bfs10420)

  try:
    return bfs10104(self, *args, **bfs10420)
  except StaleElementReferenceException, bfs10421:
    try:
      bfs10423 = bfs10422(self.target.parent)
      bfs10423.switch_to_frame(self.bfs10417)
    except NoSuchFrameException:
      raise bfs10421
    else:
      return bfs10104(self, *args, **bfs10420)



class bfs10425(object):
  def __init__(self, target, bfs10417=None):
    self.target = target
    self.bfs10417 = bfs10417
    self.bfs10427 = None

  @property
  @bfs10424
  @bfs10415
  def location(self):
    if (self.bfs10427 is None):
      location = self.target.location
      (x, y) = (location['x'], location['y'])
      size = self.target.size
      (width, height) = (size['width'], size['height'])
      self.bfs10427 = bfs10236(x, y, width, height)

    return self.bfs10427

  def is_displayed(self):
    try:
      return (self.target.is_displayed() and self.location.bfs10302(bfs10236(0, 0, sys.maxint, sys.maxint)))
    except StaleElementReferenceException:
      return False


  @bfs10424
  def get_attribute(self, bfs10426):
    return self.target.get_attribute(bfs10426)

  @property
  @bfs10424
  def text(self):
    return self.target.text

  @bfs10424
  def clear(self):
    self.target.clear()

  @bfs10424
  def send_keys(self, keys):
    self.target.send_keys(keys)

  @property
  @bfs10424
  def tag_name(self):
    return self.target.tag_name

  def unwrap(self):
    return self.target

  def __repr__(self):
    return ('<%s>%s</%s>' % (self.tag_name, self.target.text, self.tag_name))


class bfs10422(object):
  def __init__(self, driver, bfs10430=None):
    if (bfs10430 is None):
      bfs10430 = []

    self.driver = driver
    self.bfs10430 = bfs10430

  def __iter__(self):
    yield []
    for bfs10432 in xrange(sys.maxint):
      try:
        self.driver.switch_to.frame(bfs10432)
      except WebDriverException:
        break
      else:
        bfs10431 = (self.bfs10430 + [bfs10432])
        for bfs10433 in bfs10422(self.driver, bfs10431):
          yield ([bfs10432] + bfs10433)

        try:
          self.switch_to_frame(self.bfs10430)
        except NoSuchFrameException:
          raise bfs10435()




  def switch_to_frame(self, bfs10434):
    self.driver.switch_to.default_content()
    for bfs10436 in bfs10434:
      self.driver.switch_to.frame(bfs10436)



class bfs10435(Exception):
  pass

