from bfs.bfs10143.bfs10147 import LicensingError
from copy import copy
from decorator import decorator
from errno import ESRCH as bfs10454, EACCES as bfs10456
from helium.bfs10155.bfs10157 import bfs10160
from helium.bfs10143.bfs10147 import bfs10163
from helium.bfs10143.bfs10202 import bfs10232, bfs10233
from helium.bfs10374 import bfs10425, bfs10400, bfs10422, bfs10435
from helium.bfs10063.bfs10440 import bfs10442
from helium.bfs10063.bfs10443 import bfs10444
from helium.bfs10063.system import bfs10445, bfs10446, bfs10447, bfs10453
from helium.bfs10063.bfs10146 import lower, predicate, bfs10154
from inspect import getargspec, ismethod, isfunction
from logging import getLogger
from os import access, X_OK
from os.path import exists
from selenium.common.exceptions import UnexpectedAlertPresentException, ElementNotVisibleException, MoveTargetOutOfBoundsException, WebDriverException, StaleElementReferenceException, NoAlertPresentException, NoSuchWindowException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Chrome, Ie, DesiredCapabilities, ChromeOptions
from selenium_2_53_6.webdriver.firefox.webdriver import WebDriver as Firefox
from time import sleep, time
import atexit
import re
@decorator
def bfs10463(bfs10104, self, *args, **bfs10455):
  driver = self.bfs10457()
  if (driver.bfs10411() and AlertImpl(driver).exists()):
    return bfs10104(self, *args, **bfs10455)

  bfs10461 = driver.window_handles[:]
  bfs10460 = bfs10104(self, *args, **bfs10455)
  if (not (driver.bfs10411() and AlertImpl(driver).exists())):
    bfs10462 = [bfs10464 for bfs10464 in driver.window_handles if (bfs10464 not in bfs10461) ]
    if bfs10462:
      driver.switch_to.window(bfs10462[0])


  return bfs10460

@decorator
def bfs10466(bfs10104, *args, **bfs10465):
  try:
    return bfs10104(*args, **bfs10465)
  except UnexpectedAlertPresentException:
    raise UnexpectedAlertPresentException("This command is not supported when an alert is present. To accept the alert (this usually corresponds to clicking 'OK') use `Alert().accept()`. To dismiss the alert (ie. 'cancel' it), use `Alert().dismiss()`. If the alert contains a text field, you can use write(...) to set its value. Eg.: `write('hi there!')`.")


class APIImpl(object):
  bfs10467 = 'This operation requires a browser window. Please call one of the following functions first:\n * start_chrome()\n * start_firefox()\n * start_ie()\n * set_driver(...)'
  def __init__(self, bfs10471, bfs10470, bfs10472=None):
    self.bfs10471 = bfs10471
    self.license = bfs10470
    self.bfs10472 = bfs10472
    self.driver = None

  def bfs10474(self, url=None):
    capabilities = {'browserName': 'firefox', 'version': '', 'platform': 'ANY', 'javascriptEnabled': True, 'marionette': False, 'unexpectedAlertBehaviour': 'ignore'}
    try:
      firefox = Firefox(capabilities=capabilities)
    except WebDriverException:
      raise WebDriverException('Could not start Firefox. Please note that Firefox versions greater than 47.0.1 are currently not supported.')

    return self.bfs10473(firefox, url)

  def bfs10477(self, url=None):
    bfs10476 = self.bfs10475()
    return self.bfs10473(bfs10476, url)

  def bfs10475(self):
    bfs10500 = self.bfs10501()
    bfs10503 = self.bfs10502(bfs10500)
    bfs10504 = Chrome(**bfs10503)
    atexit.register(self.bfs10506, bfs10504.service)
    return bfs10504

  def bfs10501(self):
    bfs10505 = ChromeOptions()
    bfs10505.add_argument('--test-type')
    bfs10505.add_argument('--disable-extensions')
    return bfs10505

  def bfs10502(self, bfs10507):
    bfs10511 = {'chrome_options': bfs10507}
    driver = self.bfs10510()
    if exists(driver):
      if (not access(driver, X_OK)):
        try:
          bfs10444(driver)
        except:
          raise RuntimeError(('The Chrome driver located at %s is not executable.' % driver))


      if bfs10445():
        bfs10511['service_args'] = [('--chromedriver-path=%s' % driver)]
        driver = self.bfs10512('silent-chromedriver.exe')

      bfs10511['executable_path'] = driver

    return bfs10511

  def bfs10510(self):
    if bfs10445():
      bfs10513 = 'chromedriver.exe'
    elif bfs10446():
      bfs10513 = ('chromedriver' + ('_x64' if bfs10453() else ''))
    else:
      assert bfs10447()
      bfs10513 = 'chromedriver'

    return self.bfs10512(bfs10513)

  def bfs10512(self, bfs10515):
    return self.bfs10471.bfs10514('webdrivers', bfs10515)

  def bfs10506(self, service):
    if (service and hasattr(service, 'process') and service.process):
      try:
        service.process.kill()
      except OSError, e:
        if (e.errno not in (bfs10454, bfs10456)):
          raise 




  def bfs10523(self, url=None):
    bfs10516 = self.bfs10512('IEDriverServer.exe')
    capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
    capabilities['ignoreZoomSetting'] = True
    bfs10517 = {'capabilities': capabilities}
    if exists(bfs10516):
      getLogger(__name__).info('Using IE driver located at %s.', bfs10516)
      bfs10517['executable_path'] = bfs10516
    else:
      getLogger(__name__).warn('Could not find IE driver at expected location %s.', bfs10516)

    try:
      bfs10520 = Ie(**bfs10517)
    except WebDriverException, e:
      bfs10521 = e
      msg = e.msg
      if ('Protected Mode settings are not the same for all zones.' in msg):
        bfs10521 = WebDriverException('Error launching IE: Protected Mode settings are not the same for all zones. Please follow these steps: http://heliumhq.com/docs/internet_explorer#protected_mode')

      raise bfs10521

    atexit.register(self.bfs10506, bfs10520.iedriver)
    return self.bfs10473(bfs10520, url)

  def bfs10473(self, bfs10522, url=None):
    try:
      self.bfs10524(bfs10522)
    except LicensingError:
      bfs10522.quit()
      raise 

    if (url is not None):
      self.bfs10525(url)

    return self.bfs10527()

  @bfs10463
  @bfs10466
  def bfs10525(self, url):
    if ('://' not in url):
      url = ('http://' + url)

    self.bfs10457().get(url)

  def bfs10524(self, driver):
    self.bfs10526(driver)
    self.driver = bfs10400(driver)

  def bfs10526(self, driver):
    try:
      self.license.bfs10530(bfs10232(self.bfs10472))
    except bfs10163:
      try:
        self.license.bfs10530(bfs10233(self.bfs10472, driver))
      except bfs10163:
        raise LicensingError('Unfortunately, Helium could not verify your license key. Please activate your internet connection and try again.')



  def bfs10527(self):
    if (self.driver is not None):
      return self.driver.unwrap()


  @bfs10463
  @bfs10466
  def bfs10535(self, text, into=None):
    if (into is not None):
      from helium.api import GUIElement
      if isinstance(into, GUIElement):
        into = into.bfs10531


    self.bfs10532(self.bfs10534, self.bfs10533, text, into=into)

  def bfs10534(self, text, into=None):
    if into:
      if isinstance(into, basestring):
        into = TextFieldImpl(self.bfs10457(), into)

      def bfs10540(bfs10536):
        if (hasattr(bfs10536, 'clear') and callable(bfs10536.clear)):
          bfs10536.clear()

        bfs10536.send_keys(text)

      self.bfs10537(into, bfs10540)
    else:
      self.bfs10457().switch_to.active_element.send_keys(text)


  def bfs10533(self, text, into=None):
    if (into is None):
      into = AlertImpl(self.bfs10457())

    if (not isinstance(into, AlertImpl)):
      raise UnexpectedAlertPresentException(('into=%r is not allowed when an alert is present.' % into))

    into.bfs10540(text)

  def bfs10532(self, bfs10541, bfs10543, *args, **bfs10542):
    driver = self.bfs10457()
    if (driver.bfs10407() or (not AlertImpl(driver).exists())):
      try:
        return bfs10541(*args, **bfs10542)
      except UnexpectedAlertPresentException:
        if (driver.bfs10407() and (not AlertImpl(driver).exists())):
          raise RuntimeError("An alert dialog was open but was closed by an expected exception. This normally happens when you called set_driver(...) with a Firefox driver you instantiated yourself without first setting selenium.webdriver.common.desired_capabilities.DesiredCapabilities.FIREFOX['unexpectedAlertBehaviour'] to 'ignore'. If this is not the case, please file a bug report at http://heliumhq.com.")



    return bfs10543(*args, **bfs10542)

  @bfs10463
  @bfs10466
  def bfs10544(self, key):
    self.bfs10457().switch_to.active_element.send_keys(key)

  def bfs10547(self, element):
    self.bfs10546(element, (lambda bfs10545: bfs10545.click()), (lambda action_chains: action_chains.click()))

  def bfs10551(self, element):
    driver = self.bfs10457()
    self.bfs10546(element, (lambda bfs10550: driver.bfs10402().double_click(bfs10550).perform()), (lambda action_chains: action_chains.double_click()))

  def bfs10553(self, element):
    driver = self.bfs10457()
    self.bfs10546(element, (lambda bfs10552: driver.bfs10402().move_to_element(bfs10552).perform()), (lambda action_chains: action_chains))

  def bfs10554(self, element):
    driver = self.bfs10457()
    self.bfs10546(element, (lambda bfs10555: driver.bfs10402().context_click(bfs10555).perform()), (lambda action_chains: action_chains.context_click()))

  def bfs10560(self, element):
    driver = self.bfs10457()
    self.bfs10546(element, (lambda bfs10556: driver.bfs10402().click_and_hold(bfs10556).perform()), (lambda action_chains: action_chains.click_and_hold()))

  def bfs10563(self, element):
    bfs10557 = self.bfs10457()
    self.bfs10546(element, (lambda bfs10561: bfs10557.bfs10402().move_to_element(bfs10561).release().perform()), (lambda action_chains, bfs10562: action_chains.release(bfs10562)))

  @bfs10463
  @bfs10466
  def bfs10546(self, element, bfs10565, bfs10564):
    (element, offset) = self.bfs10566(element)
    driver = self.bfs10457()
    if (offset is not None):
      def bfs10402(bfs10567):
        action_chains = driver.bfs10402().move_to_element_with_offset(bfs10567.unwrap(), *offset)
        bfs10564(action_chains).perform()

    else:
      bfs10402 = (lambda bfs10571: bfs10565(bfs10571.unwrap()))

    self.bfs10537(element, bfs10402)

  def bfs10566(self, bfs10536):
    from helium.api import HTMLElement, Point
    offset = None
    if isinstance(bfs10536, basestring):
      bfs10536 = bfs10570(self.bfs10457(), bfs10536)
    elif isinstance(bfs10536, HTMLElement):
      bfs10536 = bfs10536.bfs10531
    elif isinstance(bfs10536, Point):
      (bfs10536, offset) = self.bfs10572(bfs10536)

    return (bfs10536, offset)

  def bfs10572(self, bfs10573):
    driver = self.bfs10457()
    element = bfs10425(driver.execute_script(('return document.elementFromPoint(%r, %r);' % (bfs10573.x, bfs10573.y))))
    offset = (bfs10573 - (element.location.bfs10240, element.location.bfs10242))
    if ((offset == (0, 0)) and driver.bfs10407()):
      offset = (1, 1)

    return (element, offset)

  def bfs10601(self, element, to):
    with bfs10574(self) as bfs10576:
      (element, bfs10575) = self.bfs10566(element)
      self.bfs10537(element, bfs10576.bfs10577)
      (to, bfs10575) = self.bfs10566(to)
      self.bfs10537(to, bfs10576.bfs10600)


  @bfs10466
  def bfs10605(self, predicate):
    return [predicate.bfs10602(bfs10603) for bfs10603 in predicate.bfs10531.find_all()]

  def bfs10606(self, num_pixels):
    self.bfs10604(0, num_pixels)

  def bfs10610(self, num_pixels):
    self.bfs10604(0, (-num_pixels))

  def bfs10607(self, num_pixels):
    self.bfs10604(num_pixels, 0)

  def bfs10611(self, num_pixels):
    self.bfs10604((-num_pixels), 0)

  @bfs10466
  def bfs10604(self, bfs10612, bfs10613):
    self.bfs10457().execute_script('window.scrollBy(arguments[0], arguments[1]);', bfs10612, bfs10613)

  @bfs10463
  @bfs10466
  def bfs10614(self, combo_box, value):
    from helium.api import ComboBox
    if isinstance(combo_box, basestring):
      combo_box = ComboBoxImpl(self.bfs10457(), combo_box)
    elif isinstance(combo_box, ComboBox):
      combo_box = combo_box.bfs10531

    def bfs10615(web_element):
      if isinstance(web_element, bfs10425):
        web_element = web_element.unwrap()

      Select(web_element).select_by_visible_text(value)

    self.bfs10537(combo_box, bfs10615)

  def bfs10537(self, bfs10616, bfs10402):
    driver = self.bfs10457()
    if (hasattr(bfs10616, 'perform') and callable(bfs10616.perform)):
      driver.bfs10401 = bfs10616.perform(bfs10402)
    else:
      if isinstance(bfs10616, WebElement):
        bfs10616 = bfs10425(bfs10616)

      bfs10402(bfs10616)
      driver.bfs10401 = bfs10616


  @bfs10466
  def bfs10623(self, file_path, to):
    (to, bfs10617) = self.bfs10566(to)
    drag_and_drop = bfs10621(self.bfs10457(), file_path)
    drag_and_drop.begin()
    try:
      drag_and_drop.bfs10620()
      self.bfs10537(to, (lambda bfs10622: drag_and_drop.bfs10624(bfs10622)))
    finally:
      drag_and_drop.end()


  @bfs10463
  @bfs10466
  def bfs10627(self, file_path, to=None):
    from helium.api import Point
    driver = self.bfs10457()
    if (to is None):
      to = bfs10625(driver)
    elif isinstance(to, basestring):
      to = bfs10625(driver, to)
    elif isinstance(to, Point):
      (to, bfs10617) = self.bfs10572(to)

    self.bfs10537(to, (lambda bfs10626: bfs10626.send_keys(file_path)))

  def bfs10632(self):
    self.bfs10532(self.bfs10631, self.bfs10630)

  def bfs10631(self):
    self.bfs10457().refresh()

  def bfs10630(self):
    AlertImpl(self.bfs10457()).accept()
    self.bfs10631()

  def bfs10637(self, condition_fn, timeout_secs=10, interval_secs=0.5):
    if ismethod(condition_fn):
      bfs10633 = (condition_fn.im_self is not None)
      bfs10635 = getargspec(condition_fn).args
      bfs10634 = (len(bfs10635) - (1 if bfs10633 else 0))
    else:
      if (not isfunction(condition_fn)):
        condition_fn = condition_fn.__call__

      bfs10635 = getargspec(condition_fn).args
      bfs10634 = len(bfs10635)

    bfs10636 = (condition_fn if bfs10634 else (lambda driver: condition_fn()))
    wait = WebDriverWait(self.bfs10457().unwrap(), timeout_secs, poll_frequency=interval_secs)
    wait.until(bfs10636)

  @bfs10466
  def bfs10641(self, window):
    driver = self.bfs10457()
    from helium.api import Window
    if isinstance(window, basestring):
      window = WindowImpl(driver, window)
    elif isinstance(window, Window):
      window = window.bfs10531

    driver.switch_to.window(window.handle)

  def bfs10640(self):
    self.bfs10457().quit()
    self.driver = None

  @bfs10466
  def bfs10643(self, element):
    driver = self.bfs10457()
    from helium.api import HTMLElement, Text
    if isinstance(element, basestring):
      element = Text(element)

    if isinstance(element, HTMLElement):
      element = element.bfs10531

    try:
      element = element.first_occurrence
    except AttributeError:
      pass

    bfs10642 = element.get_attribute('style')
    if isinstance(element, bfs10425):
      element = element.unwrap()

    driver.execute_script("arguments[0].setAttribute('style', 'border: 2px solid red; font-weight: bold;');", element)
    driver.execute_script("var target = arguments[0];var previousStyle = arguments[1];setTimeout(function() {target.setAttribute('style', previousStyle);}, 2000);", element, bfs10642)

  def bfs10457(self):
    if (not self.driver):
      raise RuntimeError(self.bfs10467)

    return self.driver


class bfs10574(object):
  def __init__(self, bfs10155):
    self.bfs10155 = bfs10155
    self.bfs10645 = None

  def __enter__(self):
    self.bfs10644("window.helium = {};window.helium.dragHelper = {    createEvent: function(type) {        var event = document.createEvent('CustomEvent');        event.initCustomEvent(type, true, true, null);        event.dataTransfer = {            data: {},            setData: function(type, val) {                this.data[type] = val;            },            getData: function(type) {                return this.data[type];            }        };        return event;    }};")
    return self

  def bfs10577(self, element):
    if self.bfs10646(element):
      self.bfs10645 = True
    else:
      self.bfs10155.bfs10560(element)


  def bfs10600(self, target):
    if self.bfs10645:
      self.bfs10647(target)
    else:
      self.bfs10155.bfs10563(target)


  def __exit__(self, *bfs10650):
    self.bfs10644('delete window.helium;')

  def bfs10646(self, bfs10651):
    return self.bfs10644("var source = arguments[0];function getDraggableParent(element) {    var previousParent = null;    while (element != null && element != previousParent) {        previousParent = element;        if ('draggable' in element) {            var draggable = element.draggable;            if (draggable === true)                return element;            if (typeof draggable == 'string'                     || draggable instanceof String)                if (draggable.toLowerCase() == 'true')                    return element;        }        element = element.parentNode;    }    return null;}var draggableParent = getDraggableParent(source);if (draggableParent == null)    return false;window.helium.dragHelper.draggedElement = draggableParent;var dragStart = window.helium.dragHelper.createEvent('dragstart');source.dispatchEvent(dragStart);window.helium.dragHelper.dataTransfer = dragStart.dataTransfer;return true;", bfs10651.unwrap())

  def bfs10647(self, bfs10653):
    self.bfs10644("var target = arguments[0];var drop = window.helium.dragHelper.createEvent('drop');drop.dataTransfer = window.helium.dragHelper.dataTransfer;target.dispatchEvent(drop);var dragEnd = window.helium.dragHelper.createEvent('dragend');dragEnd.dataTransfer = window.helium.dragHelper.dataTransfer;window.helium.dragHelper.draggedElement.dispatchEvent(dragEnd);", bfs10653.unwrap())

  def bfs10644(self, bfs10652, *args):
    return self.bfs10155.bfs10457().execute_script(bfs10652, *args)


class bfs10621(object):
  def __init__(self, driver, file_path):
    self.driver = driver
    self.file_path = file_path
    self.bfs10654 = None
    self.bfs10656 = None

  def begin(self):
    self.bfs10655()
    try:
      self.bfs10654.send_keys(self.file_path)
    except:
      self.end()
      raise 


  def bfs10655(self):
    self.bfs10654 = self.driver.execute_script("var input = document.createElement('input');input.type = 'file';input.style.display = 'block';input.style.opacity = '1';input.style.visibility = 'visible';input.style.height = '1px';input.style.width = '1px';if (document.body.childElementCount > 0) {   document.body.insertBefore(input, document.body.childNodes[0]);} else {   document.body.appendChild(input);}return input;")

  def bfs10620(self):
    self.bfs10657('dragenter', to='document.body')
    self.bfs10656 = self.bfs10660('dragover', 'document', interval_msecs=300)
    self.bfs10656.start()

  def bfs10657(self, bfs10661, to):
    (bfs10662, args) = self.bfs10663(bfs10661, to)
    self.driver.execute_script(bfs10662, *args)

  def bfs10660(self, bfs10665, to, interval_msecs):
    (bfs10664, args) = self.bfs10663(bfs10665, to)
    return bfs10666(self.driver, bfs10664, args, interval_msecs)

  def bfs10663(self, bfs10670, to):
    bfs10667 = "var files = arguments[0].files;var items = [];var types = [];for (var i = 0; i < files.length; i++) {   items[i] = {kind: 'file', type: files[i].type};   types[i] = 'Files';}var event = document.createEvent('CustomEvent');event.initCustomEvent(arguments[1], true, true, 0);event.dataTransfer = {\tfiles: files,\titems: items,\ttypes: types};arguments[2].dispatchEvent(event);"
    if isinstance(to, basestring):
      bfs10667 = bfs10667.replace('arguments[2]', to)
      args = (self.bfs10654, bfs10670)
    else:
      args = (self.bfs10654, bfs10670, to.unwrap())

    return (bfs10667, args)

  def bfs10624(self, target):
    self.bfs10656.stop()
    self.bfs10657('drop', to=target)

  def end(self):
    if (self.bfs10654 is not None):
      self.driver.execute_script('arguments[0].parentNode.removeChild(arguments[0]);', self.bfs10654)

    self.bfs10654 = None


class bfs10666(object):
  def __init__(self, driver, bfs10671, args, interval_msecs):
    self.driver = driver
    self.bfs10671 = bfs10671
    self.args = args
    self.interval_msecs = interval_msecs
    self.bfs10672 = None

  def start(self):
    bfs10674 = ('var originalArguments = arguments;return setInterval(function() {\targuments = originalArguments;\t%s}, %d);' % (self.bfs10671, self.interval_msecs))
    self.bfs10672 = self.driver.execute_script(bfs10674, *self.args)

  def stop(self):
    self.driver.execute_script('clearInterval(arguments[0]);', self.bfs10672)
    self.bfs10672 = None


class bfs10673(object):
  def __init__(self, driver):
    self.bfs10675 = None
    self.bfs10677 = driver

  def find_all(self):
    if self.bfs10676():
      yield self
    else:
      for bfs10700 in self.bfs10702():
        yield self.bfs10701(bfs10700)



  def bfs10676(self):
    return (self.bfs10675 is not None)

  def bfs10702(self):
    raise NotImplementedError()

  def bfs10701(self, bfs10703):
    bfs10705 = copy(self)
    bfs10705.bfs10675 = bfs10703
    return bfs10705

  def exists(self):
    try:
      next(self.find_all())
    except StopIteration:
      return False
    else:
      return True


  @property
  def first_occurrence(self):
    if (not self.bfs10676()):
      self.bfs10704()

    return self.bfs10675

  def bfs10704(self):
    self.perform((lambda bfs10706: None))

  def perform(self, bfs10402):
    from helium.api import Config
    bfs10707 = (time() + Config.implicit_wait_secs)
    bfs10711 = self.bfs10710(bfs10402)
    while ((bfs10711 is None) and (time() < bfs10707)):
      bfs10711 = self.bfs10710(bfs10402)

    if (bfs10711 is not None):
      return bfs10711

    raise LookupError()

  def bfs10710(self, bfs10402):
    for bfs10712 in self.find_all():
      bfs10714 = bfs10712.first_occurrence
      try:
        bfs10402(bfs10714)
      except Exception, e:
        if self.bfs10713(e):
          continue
        else:
          raise 

      else:
        self.bfs10675 = bfs10714
        return bfs10714



  def bfs10713(self, exception):
    if isinstance(exception, ElementNotVisibleException):
      return True

    if isinstance(exception, MoveTargetOutOfBoundsException):
      return True

    if isinstance(exception, WebDriverException):
      msg = exception.msg
      if (('Element is not clickable at point' in msg) and ('Other element would receive the click' in msg)):
        getLogger(__name__).info('Ignoring exception %r while trying to click element. It could be that the element has moved.', msg, exc_info=True)
        return True


    return False


class bfs10715(bfs10673):
  def __init__(self, driver, below=None, to_right_of=None, above=None, to_left_of=None):
    super(bfs10715, self).__init__(driver)
    self.below = self.bfs10717(below)
    self.to_right_of = self.bfs10717(to_right_of)
    self.above = self.bfs10717(above)
    self.to_left_of = self.bfs10717(to_left_of)
    self.bfs10716 = bfs10160()

  def bfs10717(self, element):
    if isinstance(element, basestring):
      return TextImpl(self.bfs10677, element)

    from helium.api import HTMLElement
    if isinstance(element, HTMLElement):
      return element.bfs10531

    return element

  @property
  def width(self):
    return self.first_occurrence.location.width

  @property
  def height(self):
    return self.first_occurrence.location.height

  @property
  def x(self):
    return self.first_occurrence.location.bfs10240

  @property
  def y(self):
    return self.first_occurrence.location.bfs10242

  @property
  def top_left(self):
    from helium.api import Point
    return Point(self.x, self.y)

  @property
  def web_element(self):
    return self.first_occurrence.unwrap()

  def bfs10702(self):
    self.bfs10720()
    self.bfs10677.switch_to.default_content()
    try:
      for bfs10417 in bfs10422(self.bfs10677):
        bfs10722 = self.bfs10721()
        for bfs10723 in self.bfs10724():
          if self.bfs10725(bfs10723, bfs10722):
            bfs10723.bfs10417 = bfs10417
            yield bfs10723



    except bfs10435:
      pass


  def bfs10720(self):
    window_handles = self.bfs10677.window_handles
    try:
      bfs10727 = self.bfs10677.current_window_handle
    except NoSuchWindowException:
      bfs10726 = True
    else:
      bfs10726 = (bfs10727 not in window_handles)

    if bfs10726:
      self.bfs10677.switch_to_window(window_handles[0])


  def bfs10721(self):
    bfs10711 = []
    if self.below:
      bfs10711.append(map((lambda bfs10730: bfs10730.location.is_above), self.below.bfs10724()))

    if self.to_right_of:
      bfs10711.append(map((lambda bfs10731: bfs10731.location.is_to_left_of), self.to_right_of.bfs10724()))

    if self.above:
      bfs10711.append(map((lambda bfs10733: bfs10733.location.is_below), self.above.bfs10724()))

    if self.to_left_of:
      bfs10711.append(map((lambda bfs10732: bfs10732.location.is_to_right_of), self.to_left_of.bfs10724()))

    return bfs10711

  def bfs10725(self, bfs10734, bfs10735):
    return (bfs10734.is_displayed() and self.bfs10736(bfs10734, bfs10735))

  def bfs10736(self, element, bfs10740):
    for bfs10737 in bfs10740:
      bfs10741 = False
      for bfs10742 in bfs10737:
        if bfs10742(element.location):
          bfs10741 = True
          break


      if (not bfs10741):
        return False


    return True

  def bfs10724(self):
    raise NotImplementedError()

  def bfs10744(self):
    return (self.first_occurrence.get_attribute('disabled') is None)


class SImpl(bfs10715):
  def __init__(self, driver, bfs10743, **bfs10745):
    super(SImpl, self).__init__(driver, **bfs10745)
    self.bfs10743 = bfs10743

  def bfs10724(self):
    wrap = (lambda bfs10746: map(bfs10425, bfs10746))
    if self.bfs10743.startswith('@'):
      return wrap(self.bfs10677.find_elements_by_name(self.bfs10743[1:]))

    if self.bfs10743.startswith('//'):
      return wrap(self.bfs10677.find_elements_by_xpath(self.bfs10743))

    return wrap(self.bfs10677.find_elements_by_css_selector(self.bfs10743))


class bfs10750(bfs10715):
  def bfs10724(self):
    bfs10747 = self.bfs10751()
    getLogger(__name__).debug('Looking for HTML element using xpath: %s.', bfs10747)
    return self.bfs10752(map(bfs10425, self.bfs10677.find_elements_by_xpath(bfs10747)))

  def bfs10752(self, bfs10754):
    bfs10753 = []
    for bfs10755 in bfs10754:
      try:
        key = self.bfs10756(bfs10755)
      except StaleElementReferenceException:
        pass
      else:
        bfs10753.append((key, bfs10755))


    bfs10757 = (lambda bfs10760: bfs10760[0])
    bfs10753.sort(key=bfs10757)
    bfs10762 = (lambda bfs10761: bfs10761[1])
    return map(bfs10762, bfs10753)

  def bfs10751(self):
    raise NotImplementedError()

  def bfs10756(self, web_element):
    return (self.bfs10677.bfs10403(web_element) + 1)


class bfs10763(bfs10750):
  def __init__(self, driver, text=None, **bfs10765):
    super(bfs10763, self).__init__(driver, **bfs10765)
    self.search_text = text

  def bfs10751(self):
    bfs10764 = (('//' + self.bfs10766()) + predicate(self.bfs10716.bfs10146('.', self.search_text)))
    return ('%s[not(self::script)][not(.%s)]' % (bfs10764, bfs10764))

  def bfs10766(self):
    return '*'


class TextImpl(bfs10763):
  def __init__(self, driver, text=None, include_free_text=True, **bfs10770):
    super(TextImpl, self).__init__(driver, text, **bfs10770)
    self.include_free_text = include_free_text

  @property
  def value(self):
    return self.first_occurrence.text

  def bfs10751(self):
    bfs10767 = ButtonImpl(self.bfs10677, self.search_text)
    bfs10771 = LinkImpl(self.bfs10677, self.search_text)
    bfs10772 = [self.bfs10773(), bfs10767.bfs10775(), bfs10771.bfs10751()]
    if (self.search_text and self.include_free_text):
      bfs10772.append(bfs10774(self.bfs10677, self.search_text).bfs10751())

    return ' | '.join(bfs10772)

  def bfs10773(self):
    if self.search_text:
      bfs10776 = super(TextImpl, self).bfs10751()
    else:
      bfs11000 = 'not(.//*[normalize-space(.)=normalize-space(self::*)])'
      bfs10776 = ('//*[text() and %s]' % bfs11000)

    return ((bfs10776 + '[not(self::option)]') + ('' if self.include_free_text else '[count(*) <= 1]'))


class bfs10774(bfs10763):
  def bfs10766(self):
    return 'text()'

  def bfs10751(self):
    return (super(bfs10774, self).bfs10751() + '/..')


class LinkImpl(bfs10763):
  def bfs10766(self):
    return 'a'

  def bfs10751(self):
    return ((((((super(LinkImpl, self).bfs10751() + ' | ') + '//a') + predicate(self.bfs10716.bfs10146('@title', self.search_text))) + ' | ') + "//*[@role='link']") + predicate(self.bfs10716.bfs10146('.', self.search_text)))

  @property
  def href(self):
    return self.web_element.get_attribute('href')


class ListItemImpl(bfs10763):
  def bfs10766(self):
    return 'li'


class ButtonImpl(bfs10763):
  def bfs10766(self):
    return 'button'

  def is_enabled(self):
    bfs10777 = self.first_occurrence.get_attribute('aria-disabled')
    return (self.bfs10744() and ((not bfs10777) or (bfs10777.lower() == 'false')))

  def bfs10751(self):
    bfs11001 = self.bfs10716.bfs10146('@aria-label', self.search_text)
    bfs11002 = self.bfs10716.bfs10146('.', self.search_text)
    bfs11004 = bfs10154(bfs11001, bfs11002)
    return ' | '.join([super(ButtonImpl, self).bfs10751(), self.bfs10775(), ("//*[@role='button']" + bfs11004), ('//button' + predicate(bfs11001))])

  def bfs10775(self):
    if self.search_text:
      bfs11003 = self.bfs10716.bfs10146('@value', self.search_text)
      bfs11005 = self.bfs10716.bfs10146('@label', self.search_text)
      bfs11007 = self.bfs10716.bfs10146('@aria-label', self.search_text)
      bfs11006 = self.bfs10716.bfs10146('@title', self.search_text)
      bfs11010 = bfs10154(bfs11003, bfs11005, bfs11007, bfs11006)
    else:
      bfs11010 = ''

    return ("//input[@type='submit' or @type='button']" + bfs11010)


class ImageImpl(bfs10750):
  def __init__(self, driver, alt, **bfs11012):
    super(ImageImpl, self).__init__(driver, **bfs11012)
    self.alt = alt

  def bfs10751(self):
    return ('//img' + predicate(self.bfs10716.bfs10146('@alt', self.alt)))


class bfs11011(bfs10715):
  bfs11013 = 1.5
  def __init__(self, driver, label=None, **bfs11014):
    super(bfs11011, self).__init__(driver, **bfs11014)
    self.label = label

  def bfs10724(self):
    if (not self.label):
      bfs11015 = self.bfs11016()
    else:
      bfs11020 = TextImpl(self.bfs10677, self.label, include_free_text=False).bfs10724()
      if bfs11020:
        bfs11015 = list(self.bfs11017(self.bfs11016(), bfs11020))
      else:
        bfs11015 = self.bfs11021()


    return sorted(bfs11015, key=self.bfs10677.bfs10403)

  def bfs11016(self, bfs11023=None):
    if (bfs11023 is None):
      bfs11023 = self.bfs10751()

    return map(bfs10425, self.bfs10677.find_elements_by_xpath(bfs11023))

  def bfs11021(self):
    bfs11022 = [bfs10146.strip().lstrip('/') for bfs10146 in self.bfs10751().split('|')]
    bfs11024 = ('//text()' + predicate(self.bfs10716.bfs10146('.', self.label)))
    bfs10146 = ' | '.join([((((bfs11024 + '/%s::') + bfs11025) + '[1]') % ('preceding-sibling' if (('checkbox' in bfs11025) or ('radio' in bfs11025)) else 'following')) for bfs11025 in bfs11022])
    return self.bfs11016(bfs10146)

  def bfs10751(self):
    raise NotImplementedError()

  def bfs11026(self):
    return 'to_right_of'

  def bfs11027(self):
    return 'below'

  def bfs11017(self, bfs11031, bfs11030):
    for (label, bfs11032) in self.bfs11033(bfs11031, bfs11030):
      yield bfs11032
      bfs11030.remove(label)
      bfs11031.remove(bfs11032)

    bfs11034 = self.bfs11036(bfs11031, bfs11030)
    bfs11034 = self.bfs11035(bfs11034)
    self.bfs11037(bfs11034)
    for bfs11040 in bfs11034.values():
      assert (len(bfs11040) <= 1)
      if bfs11040:
        yield next(iter(bfs11040))



  def bfs11033(self, bfs11042, bfs11041):
    for label in bfs11041:
      if (label.tag_name == 'label'):
        bfs11043 = label.get_attribute('for')
        if bfs11043:
          for bfs11044 in bfs11042:
            bfs11045 = bfs11044.get_attribute('id')
            if (bfs11045.lower() == bfs11043.lower()):
              yield (label, bfs11044)






  def bfs11036(self, bfs11047, bfs11046):
    bfs11050 = {}
    for label in bfs11046:
      for bfs11051 in bfs11047:
        if self.bfs11053(bfs11051, label):
          if (label not in bfs11050):
            bfs11050[label] = set()

          bfs11050[label].add(bfs11051)



    return bfs11050

  def bfs11053(self, bfs11052, label):
    if bfs11052.location.bfs10302(label.location):
      return True

    bfs11054 = self.bfs11026()
    bfs11056 = self.bfs11027()
    return ((label.location.bfs10332(bfs11052.location) <= 150) and (bfs11052.location.bfs10321(bfs11054, label.location) or bfs11052.location.bfs10321(bfs11056, label.location)))

  def bfs11035(self, bfs11055):
    bfs11057 = bfs10442(bfs11055)
    self.bfs11037(bfs11057)
    return bfs10442(bfs11057)

  def bfs11037(self, bfs11061):
    for (bfs11060, bfs11062) in bfs11061.items():
      if bfs11062:
        bfs11061[bfs11060] = set([self.bfs11064(bfs11060, bfs11062)])



  def bfs11064(self, bfs11063, bfs11065):
    bfs11067 = iter(bfs11065)
    bfs11066 = next(bfs11067)
    bfs11070 = self.bfs11071(bfs11066, bfs11063)
    for element in bfs11067:
      bfs11073 = self.bfs11071(element, bfs11063)
      if (bfs11073 < bfs11070):
        bfs11066 = element
        bfs11070 = bfs11073


    return bfs11066

  def bfs11071(self, bfs11072, bfs11074):
    bfs11075 = bfs11072.location
    bfs11077 = bfs11074.location
    if bfs11075.bfs10321(self.bfs11027(), bfs11077):
      bfs11076 = self.bfs11013
    else:
      bfs11076 = 1

    return (bfs11076 * bfs11075.bfs10332(bfs11077))


class bfs11100(bfs10715):
  def __init__(self, driver, *args, **bfs10106):
    super(bfs11100, self).__init__(driver, **bfs10106)
    self.args = ([driver] + list(args))
    self.bfs10106 = bfs10106
    self.bfs11102 = None

  @property
  def bfs11101(self):
    if (self.bfs11102 is None):
      self.bfs10704()

    return self.bfs11102

  def bfs10724(self):
    bfs11103 = []
    for element in self.bfs11104():
      for bfs11105 in element.bfs10724():
        if (self.bfs11102 is None):
          self.bfs11102 = element

        if (bfs11105 not in bfs11103):
          yield bfs11105
          bfs11103.append(bfs11105)




  def bfs11104(self):
    for bfs11107 in self.bfs11106():
      yield bfs11107(*self.args, **self.bfs10106)


  def bfs11106(self):
    raise NotImplementedError()


class bfs10570(bfs11100):
  def __init__(self, driver, text, **bfs11110):
    super(bfs10570, self).__init__(driver, text, **bfs11110)

  def bfs11106(self):
    return [ButtonImpl, TextImpl, ImageImpl]


class TextFieldImpl(bfs11100):
  def __init__(self, driver, label=None, **bfs11112):
    super(TextFieldImpl, self).__init__(driver, label, **bfs11112)

  def bfs11106(self):
    return [bfs11111, bfs11113, bfs11115]

  @property
  def value(self):
    return self.bfs11101.value

  def is_enabled(self):
    return self.bfs11101.is_enabled()

  def is_editable(self):
    return self.bfs11101.is_editable()


class bfs11113(bfs11011):
  @property
  def value(self):
    return (self.first_occurrence.get_attribute('value') or '')

  def is_enabled(self):
    return self.bfs10744()

  def is_editable(self):
    return (self.first_occurrence.get_attribute('readOnly') is None)

  def bfs10751(self):
    return (("//input[%s='text' or %s='email' or %s='password' or %s='number' or %s='tel' or string-length(@type)=0]" % ((lower('@type'),) * 5)) + " | //textarea | //*[@contenteditable='true']")


class bfs11115(bfs11011):
  @property
  def value(self):
    return self.first_occurrence.text

  def is_enabled(self):
    return self.bfs10744()

  def is_editable(self):
    return (self.first_occurrence.get_attribute('readOnly') is None)

  def bfs10751(self):
    return "//*[@role='textbox']"


class bfs11111(bfs10750):
  def __init__(self, driver, label, **bfs11114):
    super(bfs11111, self).__init__(driver, **bfs11114)
    self.label = label

  @property
  def value(self):
    return (self.first_occurrence.get_attribute('value') or '')

  def is_enabled(self):
    return self.bfs10744()

  def is_editable(self):
    return (self.first_occurrence.get_attribute('readOnly') is None)

  def bfs10751(self):
    return ('(%s)%s' % (bfs11113(self.label).bfs10751(), predicate(self.bfs10716.bfs10146('@placeholder', self.label))))


class bfs10625(bfs11011):
  def bfs10751(self):
    return "//input[@type='file']"


class ComboBoxImpl(bfs11100):
  def __init__(self, driver, label=None, **bfs11116):
    super(ComboBoxImpl, self).__init__(driver, label, **bfs11116)

  def bfs11106(self):
    return [bfs11117, bfs11121]

  def is_editable(self):
    return (self.first_occurrence.tag_name != 'select')

  @property
  def value(self):
    bfs11120 = self.bfs11122.first_selected_option
    if bfs11120:
      return bfs11120.text

    return None

  @property
  def options(self):
    return [bfs11124.text for bfs11124 in self.bfs11122.options]

  @property
  def bfs11122(self):
    return Select(self.web_element)


class bfs11121(bfs11011):
  def bfs10751(self):
    return '//select | //input[@list]'


class bfs11117(bfs10763):
  def bfs10766(self):
    return 'option'

  def bfs10751(self):
    bfs11123 = super(bfs11117, self).bfs10751()
    return (bfs11123 + '/ancestor::select[1]')

  def bfs10724(self):
    bfs11125 = super(bfs11117, self).bfs10724()
    bfs11127 = []
    for bfs11126 in bfs11125:
      for bfs11130 in Select(bfs11126.unwrap()).all_selected_options:
        if self.bfs10716.text(bfs11130.text, self.search_text):
          bfs11127.append(bfs11126)
          break



    return bfs11127


class CheckBoxImpl(bfs11011):
  def is_enabled(self):
    return self.bfs10744()

  def is_checked(self):
    return (self.first_occurrence.get_attribute('checked') is not None)

  def bfs10751(self):
    return "//input[@type='checkbox']"

  def bfs11026(self):
    return 'to_left_of'

  def bfs11027(self):
    return 'to_right_of'


class RadioButtonImpl(bfs11011):
  def is_selected(self):
    return (self.first_occurrence.get_attribute('checked') is not None)

  def bfs10751(self):
    return "//input[@type='radio']"

  def bfs11026(self):
    return 'to_left_of'

  def bfs11027(self):
    return 'to_right_of'


class WindowImpl(bfs10673):
  def __init__(self, driver, title=None):
    super(WindowImpl, self).__init__(driver)
    self.bfs11131 = title

  def bfs10702(self):
    bfs11132 = []
    for handle in self.bfs10677.window_handles:
      window = WindowImpl.bfs11134(self.bfs10677, handle)
      if (self.bfs11131 is None):
        bfs11132.append((0, window))
      else:
        title = window.title
        if title.startswith(self.bfs11131):
          bfs11133 = (len(title) - len(self.bfs11131))
          bfs11132.append((bfs11133, window))



    bfs11133 = (lambda bfs11135: bfs11135[0])
    bfs11132.sort(key=bfs11133)
    for (bfs11133, window) in bfs11132:
      yield window


  @property
  def title(self):
    return self.first_occurrence.title

  @property
  def handle(self):
    return self.first_occurrence.handle

  class bfs11134(object):
    def __init__(self, driver, handle):
      self.driver = driver
      self.handle = handle
      self.bfs11137 = None

    @property
    def title(self):
      with self:
        return self.driver.title


    def __enter__(self):
      try:
        self.bfs11137 = self.driver.current_window_handle
      except NoSuchWindowException, bfs11136:
        bfs11140 = True
      else:
        bfs11140 = (self.bfs11137 != self.handle)

      if bfs11140:
        self.driver.switch_to.window(self.handle)


    def __exit__(self, *bfs11141):
      if (self.bfs11137 and (self.driver.current_window_handle != self.bfs11137)):
        self.driver.switch_to.window(self.bfs11137)




class AlertImpl(bfs10673):
  def __init__(self, driver, search_text=None):
    super(AlertImpl, self).__init__(driver)
    self.search_text = search_text

  def bfs10702(self):
    bfs11142 = self.bfs10677.switch_to.alert
    try:
      text = bfs11142.text
      if ((self.search_text is None) or text.startswith(self.search_text)):
        yield bfs11142

    except NoAlertPresentException:
      pass


  @property
  def text(self):
    return self.first_occurrence.text

  def accept(self):
    first_occurrence = self.first_occurrence
    try:
      first_occurrence.accept()
    except WebDriverException, e:
      msg = e.msg
      if (msg and re.match('a\\.document\\.getElementsByTagName\\([^\\)]*\\)\\[0\\] is undefined', msg)):
        getLogger(__name__).warn('Got %r when trying to accept alert. Trying again after 0.25s.', e)
        sleep(0.25)
        first_occurrence.accept()
      else:
        raise 



  def dismiss(self):
    self.first_occurrence.dismiss()

  def bfs10540(self, text):
    self.first_occurrence.send_keys(text)


