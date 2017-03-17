"""EXPORT
Helium Copyright (c) 2012-2014 BugFree Software. All Rights Reserved.

Helium's API is contained in module ``helium.api``. It is a simple Python API
that makes specifying web automation cases as simple as describing them to
someone looking over their shoulder at a screen.

The public functions and classes of Helium are listed below. If you wish to use
Helium functions in your Python scripts you can import them from the
``helium.api`` module::

	from helium.api import *
"""
from bfs.bfs10063.encoding import bfs10101
from bfs.bfs10063.bfs10121 import bfs10144, bfs10141
from collections import namedtuple
from copy import copy
from helium.bfs10155.bfs11414 import bfs11423
from helium.bfs10063.bfs11463 import OrderedDict
from helium.bfs10063.bfs10162 import bfs10200
from logging import getLogger
from selenium.webdriver.common.keys import Keys
import helium.bfs10155
__all__ = ['attach_file', 'click', 'doubleclick', 'drag', 'drag_file', 'find_all', 'get_driver', 'go_to', 'highlight', 'hover', 'kill_browser', 'press', 'refresh', 'rightclick', 'scroll_down', 'scroll_left', 'scroll_right', 'scroll_up', 'select', 'set_driver', 'start_chrome', 'start_firefox', 'start_ie', 'switch_to', 'wait_until', 'write', 'Alert', 'Button', 'CheckBox', 'ComboBox', 'Config', 'Image', 'Link', 'ListItem', 'Point', 'S', 'RadioButton', 'Text', 'TextField', 'Window', 'ADD', 'ALT', 'ARROW_DOWN', 'ARROW_LEFT', 'ARROW_RIGHT', 'ARROW_UP', 'BACK_SPACE', 'CANCEL', 'CLEAR', 'COMMAND', 'CONTROL', 'DECIMAL', 'DELETE', 'DIVIDE', 'DOWN', 'END', 'ENTER', 'EQUALS', 'ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'HELP', 'HOME', 'INSERT', 'LEFT', 'LEFT_ALT', 'LEFT_CONTROL', 'LEFT_SHIFT', 'META', 'MULTIPLY', 'NULL', 'NUMPAD0', 'NUMPAD1', 'NUMPAD2', 'NUMPAD3', 'NUMPAD4', 'NUMPAD5', 'NUMPAD6', 'NUMPAD7', 'NUMPAD8', 'NUMPAD9', 'PAGE_DOWN', 'PAGE_UP', 'PAUSE', 'RETURN', 'RIGHT', 'SEMICOLON', 'SEPARATOR', 'SHIFT', 'SPACE', 'SUBTRACT', 'TAB', 'UP']
def start_firefox(url=None):
  """EXPORT
	:param url: URL to open.
	:type url: str

	Starts an instance of Firefox, optionally opening the specified URL.
	For instance::

		start_firefox()
		start_firefox("google.com")

	Helium does not close the browser window on shutdown of the Python
	interpreter. If you want to close the browser at the end of your script, use
	the following command::

		kill_browser()
	"""
  getLogger(__name__).info(bfs10144(start_firefox, url))
  return bfs11502().bfs10474(url)

def start_chrome(url=None):
  """EXPORT
	:param url: URL to open.
	:type url: str

	Starts an instance of Google Chrome, optionally opening the specified URL.
	For instance::

		start_chrome()
		start_chrome("google.com")

	On shutdown of the Python interpreter, Helium cleans up all resources used
	for controlling the browser (such as the ChromeDriver process), but does
	not close the browser itself. If you want to terminate the browser at the
	end of your script, use the following command::

		kill_browser()
	"""
  getLogger(__name__).info(bfs10144(start_chrome, url))
  return bfs11502().bfs10477(url)

def start_ie(url=None):
  """EXPORT
	:param url: URL to open.
	:type url: str

	(Windows only) Starts Internet Explorer, optionally opening the specified
	URL. For instance::

		start_ie()
		start_ie("google.com")

	On shutdown of the Python interpreter, Helium cleans up all resources used
	for controlling the browser (such as the IEDriverServer process), but does
	not close the browser itself. If you want to terminate the browser at the
	end of your script, use the following command::

		kill_browser()
	"""
  getLogger(__name__).info(bfs10144(start_ie, url))
  return bfs11502().bfs10523(url)

def go_to(url):
  """EXPORT
	:param url: URL to open.
	:type url: str

	Opens the specified URL in the current web browser window. For instance::

		go_to("google.com")
	"""
  getLogger(__name__).info(bfs10144(go_to, url))
  bfs11502().bfs10525(url)

def set_driver(driver):
  """EXPORT
	Sets the Selenium WebDriver used to execute Helium commands. See also
	:py:func:`get_driver`.
	"""
  bfs11502().bfs10524(driver)

def get_driver():
  """EXPORT
	Returns the Selenium WebDriver currently used by Helium to execute all
	commands. Each Helium command such as ``click("Login")`` is translated to a
	sequence of Selenium commands that are issued to this driver.
	"""
  return bfs11502().bfs10527()

def write(text, into=None):
  """EXPORT
	:param text: The text to be written.
	:type text: one of str, unicode
	:param into: The element to write into.
	:type into: one of str, unicode, :py:class:`HTMLElement`, :py:class:`selenium.webdriver.remote.webelement.WebElement`, :py:class:`Alert`

	Types the given text into the active window. If parameter 'into' is given,
	writes the text into the text field or element identified by that parameter.
	Common examples of 'write' are::

		write("Hello World!")
		write("user12345", into="Username:")
		write("Michael", into=Alert("Please enter your name"))
	"""
  getLogger(__name__).info(bfs10144(write, text, into=into))
  bfs11502().bfs10535(text, into)

def press(key):
  "EXPORT\n\t:param \\key: Key or combination of keys to be pressed.\n\n\tPresses the given key or key combination. To press a normal letter key such\n\tas 'a' simply call `press` for it::\n\n\t\tpress('a')\n\n\tYou can also simulate the pressing of upper case characters that way::\n\n\t\tpress('A')\n\n\tThe special keys you can press are those given by Selenium's class\n\t:py:class:`selenium.webdriver.common.keys.Keys`. Helium makes all those keys\n\tavailable through its namespace, so you can just use them without having to\n\trefer to :py:class:`selenium.webdriver.common.keys.Keys`. For instance, to\n\tpress the Enter key::\n\n\t\tpress(ENTER)\n\n\tTo press multiple keys at the same time, concatenate them with `+`. For\n\texample, to press Control + a, call::\n\n\t\tpress(CONTROL + 'a')\n\t"
  getLogger(__name__).info(bfs10144(press, key))
  bfs11502().bfs10544(key)

NULL = Keys.NULL
CANCEL = Keys.CANCEL
HELP = Keys.HELP
BACK_SPACE = Keys.BACK_SPACE
TAB = Keys.TAB
CLEAR = Keys.CLEAR
RETURN = Keys.RETURN
ENTER = Keys.ENTER
SHIFT = Keys.SHIFT
LEFT_SHIFT = Keys.LEFT_SHIFT
CONTROL = Keys.CONTROL
LEFT_CONTROL = Keys.LEFT_CONTROL
ALT = Keys.ALT
LEFT_ALT = Keys.LEFT_ALT
PAUSE = Keys.PAUSE
ESCAPE = Keys.ESCAPE
SPACE = Keys.SPACE
PAGE_UP = Keys.PAGE_UP
PAGE_DOWN = Keys.PAGE_DOWN
END = Keys.END
HOME = Keys.HOME
LEFT = Keys.LEFT
ARROW_LEFT = Keys.ARROW_LEFT
UP = Keys.UP
ARROW_UP = Keys.ARROW_UP
RIGHT = Keys.RIGHT
ARROW_RIGHT = Keys.ARROW_RIGHT
DOWN = Keys.DOWN
ARROW_DOWN = Keys.ARROW_DOWN
INSERT = Keys.INSERT
DELETE = Keys.DELETE
SEMICOLON = Keys.SEMICOLON
EQUALS = Keys.EQUALS
NUMPAD0 = Keys.NUMPAD0
NUMPAD1 = Keys.NUMPAD1
NUMPAD2 = Keys.NUMPAD2
NUMPAD3 = Keys.NUMPAD3
NUMPAD4 = Keys.NUMPAD4
NUMPAD5 = Keys.NUMPAD5
NUMPAD6 = Keys.NUMPAD6
NUMPAD7 = Keys.NUMPAD7
NUMPAD8 = Keys.NUMPAD8
NUMPAD9 = Keys.NUMPAD9
MULTIPLY = Keys.MULTIPLY
ADD = Keys.ADD
SEPARATOR = Keys.SEPARATOR
SUBTRACT = Keys.SUBTRACT
DECIMAL = Keys.DECIMAL
DIVIDE = Keys.DIVIDE
F1 = Keys.F1
F2 = Keys.F2
F3 = Keys.F3
F4 = Keys.F4
F5 = Keys.F5
F6 = Keys.F6
F7 = Keys.F7
F8 = Keys.F8
F9 = Keys.F9
F10 = Keys.F10
F11 = Keys.F11
F12 = Keys.F12
META = Keys.META
COMMAND = Keys.COMMAND
def click(element):
  """EXPORT
	:param element: The element or point to click.
	:type element: str, unicode, :py:class:`HTMLElement`, :py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Clicks on the given element or point. Common examples are::

		click("Sign in")
		click(Button("OK"))
		click(Point(200, 300))
		click(ComboBox("File type").top_left + (50, 0))
	"""
  getLogger(__name__).info(bfs10144(click, element))
  bfs11502().bfs10547(element)

def doubleclick(element):
  """EXPORT
	:param element: The element or point to click.
	:type element: str, unicode, :py:class:`HTMLElement`, :py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Performs a double-click on the given element or point. For example::

		doubleclick("Double click here")
		doubleclick(Image("Directories"))
		doubleclick(Point(200, 300))
		doubleclick(TextField("Username").top_left - (0, 20))
	"""
  getLogger(__name__).info(bfs10144(doubleclick, element))
  bfs11502().bfs10551(element)

def drag(element, to):
  """EXPORT
	:param element: The element or point to drag.
	:type element: str, unicode, :py:class:`HTMLElement`, :py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`
	:param to: The element or point to drag to.
	:type to: str, unicode, :py:class:`HTMLElement`, :py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Drags the given element or point to the given location. For example::

		drag("Drag me!", to="Drop here.")

	The dragging is performed by hovering the mouse cursor over ``element``,
	pressing and holding the left mouse button, moving the mouse cursor over
	``to``, and then releasing the left mouse button again.

	This function is exclusively used for dragging elements inside one web page.
	If you wish to drag a file from the hard disk onto the browser window (eg.
	to initiate a file upload), use function :py:func:`drag_file`.
	"""
  getLogger(__name__).info(bfs10144(drag, element, to))
  bfs11502().bfs10601(element, to)

def bfs10560(element):
  getLogger(__name__).info(bfs10144(bfs10560, element))
  bfs11502().bfs10560(element)

def bfs10563(element):
  getLogger(__name__).info(bfs10144(bfs10563, element))
  bfs11502().bfs10563(element)

def find_all(predicate):
  """EXPORT
	Lets you find all occurrences of the given GUI element predicate. For
	instance, the following statement returns a list of all buttons with label
	"Open"::

		find_all(Button("Open"))

	Other examples are::

		find_all(Window())
		find_all(TextField("Address line 1"))

	The function returns a list of elements of the same type as the passed-in
	parameter. For instance, ``find_all(Button(...))`` yields a list whose
	elements are of type :py:class:`Button`.

	In a typical usage scenario, you want to pick out one of the occurrences
	returned by :py:func:`find_all`. In such cases, :py:func:`list.sort` can
	be very useful. For example, to find the leftmost "Open" button, you can
	write::

		buttons = find_all(Button("Open"))
		leftmost_button = sorted(buttons, key=lambda button: button.x)[0]
	"""
  getLogger(__name__).info(bfs10144(find_all, predicate))
  return bfs11502().bfs10605(predicate)

def scroll_down(num_pixels=100):
  """EXPORT
	Scrolls down the page the given number of pixels.
	"""
  getLogger(__name__).info(bfs10144(scroll_down, num_pixels))
  bfs11502().bfs10606(num_pixels)

def scroll_up(num_pixels=100):
  """EXPORT
	Scrolls the the page up the given number of pixels.
	"""
  getLogger(__name__).info(bfs10144(scroll_up, num_pixels))
  bfs11502().bfs10610(num_pixels)

def scroll_right(num_pixels=100):
  """EXPORT
	Scrolls the page to the right the given number of pixels.
	"""
  getLogger(__name__).info(bfs10144(scroll_right, num_pixels))
  bfs11502().bfs10607(num_pixels)

def scroll_left(num_pixels=100):
  """EXPORT
	Scrolls the page to the left the given number of pixels.
	"""
  getLogger(__name__).info(bfs10144(scroll_left, num_pixels))
  bfs11502().bfs10611(num_pixels)

def hover(element):
  """EXPORT
	:param element: The element or point to hover.
	:type element: str, unicode, :py:class:`HTMLElement`, :py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Hovers the mouse cursor over the given element or point. For example::

		hover("File size")
		hover(Button("OK"))
		hover(Link("Download"))
		hover(Point(200, 300))
		hover(ComboBox("File type").top_left + (50, 0))
	"""
  getLogger(__name__).info(bfs10144(hover, element))
  bfs11502().bfs10553(element)

def rightclick(element):
  """EXPORT
	:param element: The element or point to click.
	:type element: str, unicode, :py:class:`HTMLElement`, :py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Performs a right click on the given element or point. For example::

		rightclick("Something")
		rightclick(Point(200, 300))
		rightclick(Image("captcha"))
	"""
  getLogger(__name__).info(bfs10144(rightclick))
  bfs11502().bfs10554(element)

def select(combo_box, value):
  """EXPORT
	:param combo_box: The combo box whose value should be changed.
	:type combo_box: str, unicode or :py:class:`ComboBox`
	:param value: The visible value of the combo box to be selected.

	Selects a value from a combo box. For example::

		select("Language", "English")
		select(ComboBox("Language"), "English")
	"""
  getLogger(__name__).info(bfs10144(select, combo_box, value))
  bfs11502().bfs10614(combo_box, value)

def drag_file(file_path, to):
  'EXPORT\n\tSimulates the dragging of a file from the computer over the browser window\n\tand dropping it over the given element. This allows, for example, to attach\n\tfiles to emails in Gmail::\n\n\t\tclick("COMPOSE")\n\t\twrite("example@gmail.com", into="To")\n\t\twrite("Email subject", into="Subject")\n\t\tdrag_file(r"C:\\Documents\\notes.txt", to="Drop files here")\n\t'
  getLogger(__name__).info(bfs10144(drag_file, file_path, to))
  bfs11502().bfs10623(file_path, to)

def attach_file(file_path, to=None):
  """EXPORT
	:param file_path: The path of the file to be attached.
	:param to: The file input element to which the file should be attached.

	Allows attaching a file to a file input element. For instance::

		attach_file("c:/test.txt", to="Please select a file:")

	The file input element is identified by its label. If you omit the ``to=``
	parameter, then Helium attaches the file to the first file input element it
	finds on the page.
	"""
  getLogger(__name__).info(bfs10144(attach_file, file_path, to=to))
  bfs11502().bfs10627(file_path, to=to)

def refresh():
  """EXPORT
	Refreshes the current page. If an alert dialog is open, then Helium first
	closes it.
	"""
  getLogger(__name__).info(bfs10144(refresh))
  bfs11502().bfs10632()

def wait_until(condition_fn, timeout_secs=10, interval_secs=0.5):
  """EXPORT
	:param condition_fn: A function taking no arguments that represents the 	condition to be waited for.
	:param timeout_secs: The timeout, in seconds, after which the condition is 	deemed to have failed.
	:param interval_secs: The interval, in seconds, at which the condition 	function is polled to determine whether the wait has succeeded.

	Waits until the given condition function evaluates to true. This is most
	commonly used to wait for an element to exist::

		wait_until(Text("Finished!").exists)

	More elaborate conditions are also possible using Python lambda
	expressions. For instance, to wait until a text no longer exists::

		wait_until(lambda: not Text("Uploading...").exists())

	When the optional parameter ``timeout_secs`` is given and not ``None``,
	``wait_until`` raises :py:class:`selenium.common.exceptions.TimeoutExpired`
	if the condition is not satisfied within the given number of seconds. The
	parameter ``interval_secs`` specifies the number of seconds Helium waits
	between evaluating the condition function.
	"""
  getLogger(__name__).info(bfs10144(wait_until, condition_fn, timeout_secs=timeout_secs, interval_secs=interval_secs))
  bfs11502().bfs10637(condition_fn, timeout_secs, interval_secs)

class Config(object):
  """EXPORT
	This class contains Helium's run-time configuration. To modify Helium's
	behaviour, simply assign to the properties of this class. For instance::

		Config.implicit_wait_secs = 0
	"""
  implicit_wait_secs = 10

class GUIElement(object):
  def __init__(self):
    self.bfs10677 = bfs11502().bfs10457()
    self.bfs11504 = []
    self.bfs11505 = OrderedDict()
    self.bfs11506 = None

  def exists(self):
    """EXPORT
		Evaluates to true if this GUI element exists.
		"""
    return self.bfs10531.exists()

  def bfs10602(self, bfs11510):
    bfs11507 = copy(self)
    bfs11507.bfs10531 = bfs11510
    return bfs11507

  @property
  def bfs10531(self):
    if (self.bfs11506 is None):
      bfs11511 = getattr(helium.bfs10155, (self.__class__.__name__ + 'Impl'))
      self.bfs11506 = bfs11511(self.bfs10677, *self.bfs11504, **self.bfs11505)

    return self.bfs11506

  @bfs10531.setter
  def bfs10531(self, value):
    self.bfs11506 = value

  def __repr__(self):
    return self.bfs11512(self.bfs11504, self.bfs11505)

  def bfs11512(self, args=None, bfs11514=None):
    if (args is None):
      args = []

    if (bfs11514 is None):
      bfs11514 = {}

    return ('%s(%s)' % (self.__class__.__name__, bfs10141(self.__init__, args, bfs11514, bfs10101)))

  def bfs10676(self):
    return ((self.bfs11506 is not None) and self.bfs11506.bfs10676())


class HTMLElement(GUIElement):
  def __init__(self, below=None, to_right_of=None, above=None, to_left_of=None):
    super(HTMLElement, self).__init__()
    self.bfs11505['below'] = below
    self.bfs11505['to_right_of'] = to_right_of
    self.bfs11505['above'] = above
    self.bfs11505['to_left_of'] = to_left_of

  @property
  def width(self):
    """EXPORT
		The width of this HTML element, in pixels.
		"""
    return self.bfs10531.width

  @property
  def height(self):
    """EXPORT
		The height of this HTML element, in pixels.
		"""
    return self.bfs10531.height

  @property
  def x(self):
    """EXPORT
		The x-coordinate on the page of the top-left point of this HTML element.
		"""
    return self.bfs10531.x

  @property
  def y(self):
    """EXPORT
		The y-coordinate on the page of the top-left point of this HTML element.
		"""
    return self.bfs10531.y

  @property
  def top_left(self):
    """EXPORT
		The top left corner of this element, as a :py:class:`helium.api.Point`.
		This point has exactly the coordinates given by this element's `.x` and
		`.y` properties. `top_left` is for instance useful for clicking at an
		offset of an element::

			click(Button("OK").top_left + (30, 15))
		"""
    return self.bfs10531.top_left

  @property
  def web_element(self):
    """EXPORT
		The Selenium WebElement corresponding to this element.
		"""
    return self.bfs10531.web_element

  def __repr__(self):
    if self.bfs10676():
      bfs11513 = self.web_element.get_attribute('outerHTML')
      return bfs10200(bfs11513)
    else:
      return super(HTMLElement, self).__repr__()



class S(HTMLElement):
  """EXPORT
	:param selector: The selector used to identify the HTML element(s).

	A jQuery-style selector for identifying HTML elements by ID, name, CSS
	class, CSS selector or XPath. For example: Say you have an element with
	ID "myId" on a web page, such as ``<div id="myId" .../>``.
	Then you can identify this element using ``S`` as follows::

		S("#myId")

	The parameter which you pass to ``S(...)`` is interpreted by Helium
	according to these rules:

	 * If it starts with an ``@``, then it identifies elements by HTML ``name``.
	   Eg. ``S("@btnName")`` identifies an element with ``name="btnName"``.
	 * If it starts with ``//``, then Helium interprets it as an XPath.
	 * Otherwise, Helium interprets it as a CSS selector. This in particular
	   lets you write ``S("#myId")`` to identify an element with ``id="myId"``,
	   or ``S(".myClass")`` to identify elements with ``class="myClass"``.

	``S`` also makes it possible to read plain text data from a web page. For
	example, suppose you have a table of people's email addresses. Then you
	can read the list of email addresses as follows::

		email_cells = find_all(S("table > tr > td", below="Email"))
		emails = [cell.web_element.text for cell in email_cells]

	Where ``email`` is the column header (``<th>Email</th>``). Similarly to
	``below`` and ``to_right_of``, the keyword parameters ``above`` and
	``to_left_of`` can be used to search for elements above and to the left
	of other web elements.
	"""
  def __init__(self, bfs11515, below=None, to_right_of=None, above=None, to_left_of=None):
    super(S, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(bfs11515)


class Text(HTMLElement):
  """EXPORT
	Lets you identify any text or label on a web page. This is most useful for
	checking whether a particular text exists::

		if Text("Do you want to proceed?").exists():
		    click("Yes")

	``Text`` also makes it possible to read plain text data from a web page. For
	example, suppose you have a table of people's email addresses. Then you
	can read John's email addresses as follows::

		Text(below="Email", to_right_of="John").value

	Similarly to ``below`` and ``to_right_of``, the keyword parameters ``above``
	and ``to_left_of`` can be used to search for texts above and to the left of
	other web elements.
	"""
  def __init__(self, text=None, below=None, to_right_of=None, above=None, to_left_of=None):
    super(Text, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(text)

  @property
  def value(self):
    """EXPORT
		Returns the current value of this Text object.
		"""
    return self.bfs10531.value


class Link(HTMLElement):
  """EXPORT
	Lets you identify a link on a web page. A typical usage of ``Link`` is::

		click(Link("Sign in"))

	You can also read a ``Link``'s properties. This is most typically used to
	check for a link's existence before clicking on it::

		if Link("Sign in").exists():
		    click(Link("Sign in"))

	When there are multiple occurrences of a link on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(Link("Block User", to_right_of="John Doe"))
	"""
  def __init__(self, text=None, below=None, to_right_of=None, above=None, to_left_of=None):
    super(Link, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(text)

  @property
  def href(self):
    """EXPORT
		Returns the URL of the page the link goes to.
		"""
    return self.bfs10531.href


class ListItem(HTMLElement):
  """EXPORT
	Lets you identify a list item (HTML ``<li>`` element) on a web page. This is
	often useful for interacting with elements of a navigation bar::

		click(ListItem("News Feed"))

	In other cases such as an automated test, you might want to query the
	properties of a ``ListItem``. For example, the following line checks whether
	a list item with text "List item 1" exists, and raises an error if not::

		assert ListItem("List item 1").exists()

	When there are multiple occurrences of a list item on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(ListItem("List item 1", below="My first list:"))
	"""
  def __init__(self, text=None, below=None, to_right_of=None, above=None, to_left_of=None):
    super(ListItem, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(text)


class Button(HTMLElement):
  """EXPORT
	Lets you identify a button on a web page. A typical usage of ``Button`` is::

		click(Button("Log In"))

	``Button`` also lets you read a button's properties. For example, the
	following snippet clicks button "OK" only if it exists::

		if Button("OK").exists():
		    click(Button("OK"))

	When there are multiple occurrences of a button on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(Button("Log In", below=TextField("Password")))
	"""
  def __init__(self, text=None, below=None, to_right_of=None, above=None, to_left_of=None):
    super(Button, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(text)

  def is_enabled(self):
    """EXPORT
		Returns true if this UI element can currently be interacted with.
		"""
    return self.bfs10531.is_enabled()


class Image(HTMLElement):
  """EXPORT
	Lets you identify an image (HTML ``<img>`` element) on a web page.
	Typically, this is done via the image's alt text. For instance::

		click(Image(alt="Helium Logo"))

	You can also query an image's properties. For example, the following snippet
	clicks on the image with alt text "Helium Logo" only if it exists::

		if Image("Helium Logo").exists():
		    click(Image("Helium Logo"))

	When there are multiple occurrences of an image on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(Image("Helium Logo", to_left_of=ListItem("Download")))
	"""
  def __init__(self, alt=None, below=None, to_right_of=None, above=None, to_left_of=None):
    super(Image, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(alt)


class TextField(HTMLElement):
  """EXPORT
	Lets you identify a text field on a web page. This is most typically done to
	read the value of a text field. For example::

		TextField("First name").value

	This returns the value of the "First name" text field. If it is empty, the
	empty string "" is returned.

	When there are multiple occurrences of a text field on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		TextField("Address line 1", below="Billing Address:").value
	"""
  def __init__(self, label=None, below=None, to_right_of=None, above=None, to_left_of=None):
    super(TextField, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(label)

  @property
  def value(self):
    """EXPORT
		Returns the current value of this text field. '' if there is no value.
		"""
    return self.bfs10531.value

  def is_enabled(self):
    """EXPORT
		Returns true if this UI element can currently be interacted with.

		The difference between a text field being 'enabled' and 'editable' is
		mostly visual: If a text field is not enabled, it is usually greyed out,
		whereas if it is not editable it looks normal. See also ``is_editable``.
		"""
    return self.bfs10531.is_enabled()

  def is_editable(self):
    """EXPORT
		Returns true if the value of this UI element can be modified.

		The difference between a text field being 'enabled' and 'editable' is
		mostly visual: If a text field is not enabled, it is usually greyed out,
		whereas if it is not editable it looks normal. See also ``is_enabled``.
		"""
    return self.bfs10531.is_editable()


class ComboBox(HTMLElement):
  """EXPORT
	Lets you identify a combo box on a web page. This can for instance be used
	to determine the current value of a combo box::

		ComboBox("Language").value

	A ComboBox may be *editable*, which means that it is possible to type in
	arbitrary values in addition to selecting from a predefined drop-down list
	of values. The property :py:func:`ComboBox.is_editable` can be used to
	determine whether this is the case for a particular combo box instance.

	When there are multiple occurrences of a combo box on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		select(ComboBox(to_right_of="John Doe", below="Status"), "Active")

	This sets the Status of John Doe to Active on the page.
	"""
  def __init__(self, label=None, below=None, to_right_of=None, above=None, to_left_of=None):
    super(ComboBox, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(label)

  def is_editable(self):
    """EXPORT
		Returns whether this combo box allows entering an arbitrary text in
		addition to selecting predefined values from a drop-down list.
		"""
    return self.bfs10531.is_editable()

  @property
  def value(self):
    """EXPORT
		Returns the currently selected combo box value.
		"""
    return self.bfs10531.value

  @property
  def options(self):
    """EXPORT
		Returns a list of all possible options available to choose from in the
		ComboBox.
		"""
    return self.bfs10531.options


class CheckBox(HTMLElement):
  """EXPORT
	Lets you identify a check box on a web page. To tick a currently unselected
	check box, use::

		click(CheckBox("I agree"))

	``CheckBox`` also lets you read the properties of a check box. For example,
	the method :py:func:`CheckBox.is_checked` can be used to only click a check
	box if it isn't already checked::

		if not CheckBox("I agree").is_checked():
		    click(CheckBox("I agree"))

	When there are multiple occurrences of a check box on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(CheckBox("Stay signed in", below=Button("Sign in")))
	"""
  def __init__(self, label=None, below=None, to_right_of=None, above=None, to_left_of=None):
    super(CheckBox, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(label)

  def is_enabled(self):
    """EXPORT
		Returns True if this GUI element can currently be interacted with.
		"""
    return self.bfs10531.is_enabled()

  def is_checked(self):
    """EXPORT
		Returns True if this GUI element is checked (selected).
		"""
    return self.bfs10531.is_checked()


class RadioButton(HTMLElement):
  """EXPORT
	Lets you identify a radio button on a web page. To select a currently
	unselected radio button, use::

		click(RadioButton("Windows"))

	``RadioButton`` also lets you read the properties of a radio button. For
	example, the method :py:func:`RadioButton.is_selected` can be used to only
	click a radio button if it isn't already selected::

		if not RadioButton("Windows").is_selected():
		    click(RadioButton("Windows"))

	When there are multiple occurrences of a radio button on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(RadioButton("I accept", below="License Agreement"))
	"""
  def __init__(self, label=None, below=None, to_right_of=None, above=None, to_left_of=None):
    super(RadioButton, self).__init__(below=below, to_right_of=to_right_of, above=above, to_left_of=to_left_of)
    self.bfs11504.append(label)

  def is_selected(self):
    """EXPORT
		Returns true if this radio button is selected.
		"""
    return self.bfs10531.is_selected()


class Window(GUIElement):
  """EXPORT
	Lets you identify individual windows of the currently open browser session.
	"""
  def __init__(self, title=None):
    super(Window, self).__init__()
    self.bfs11504.append(title)

  @property
  def title(self):
    """EXPORT
		Returns the title of this Window.
		"""
    return self.bfs10531.title

  @property
  def handle(self):
    """EXPORT
		Returns the Selenium driver window handle assigned to this window. Note
		that this window handle is simply an abstract identifier and bears no
		relationship to the corresponding operating system handle (HWND on
		Windows).
		"""
    return self.bfs10531.handle

  def __repr__(self):
    if self.bfs10676():
      return self.bfs11512([self.title])
    else:
      return super(Window, self).__repr__()



class Alert(GUIElement):
  """EXPORT
	Lets you identify and interact with JavaScript alert boxes.
	"""
  def __init__(self, search_text=None):
    super(Alert, self).__init__()
    self.bfs11504.append(search_text)

  @property
  def text(self):
    """EXPORT
		The text displayed in the alert box.
		"""
    return self.bfs10531.text

  def accept(self):
    """EXPORT
		Accepts this alert. This typically corresponds to clicking the "OK"
		button inside the alert. The typical way to use this method is::

			>>> Alert().accept()

		This accepts the currently open alert.
		"""
    self.bfs10531.accept()

  def dismiss(self):
    """EXPORT
		Dismisses this alert. This typically corresponds to clicking the
		"Cancel" or "Close" button of the alert. The typical way to use this
		method is::

			>>> Alert().dismiss()

		This dismisses the currently open alert.
		"""
    self.bfs10531.dismiss()

  def __repr__(self):
    if self.bfs10676():
      return self.bfs11512([self.text])
    else:
      return super(Alert, self).__repr__()



class Point(namedtuple('Point', ['x', 'y'])):
  """EXPORT
	A clickable point. To create a ``Point`` at an offset of an existing point,
	use ``+`` and ``-``::

		>>> point = Point(x=10, y=25)
		>>> point + (10, 0)
		Point(x=20, y=25)
		>>> point - (0, 10)
		Point(x=10, y=15)
	"""
  def __new__(bfs11516, x=0, y=0):
    return bfs11516.__bases__[0].__new__(bfs11516, x, y)

  def __init__(self, x=0, y=0):
    pass

  @property
  def x(self):
    """EXPORT
		The x coordinate of the point.
		"""
    return self[0]

  @property
  def y(self):
    """EXPORT
		The y coordinate of the point.
		"""
    return self[1]

  def __eq__(self, bfs11520):
    return ((self.x, self.y) == bfs11520)

  def __ne__(self, bfs11517):
    return (not (self == bfs11517))

  def __hash__(self):
    return (self.x + (7 * self.y))

  def __add__(self, bfs11521):
    (bfs11522, bfs11524) = bfs11521
    return Point((self.x + bfs11522), (self.y + bfs11524))

  def __radd__(self, bfs11523):
    return self.__add__(bfs11523)

  def __sub__(self, bfs11525):
    (bfs11526, bfs11527) = bfs11525
    return Point((self.x - bfs11526), (self.y - bfs11527))

  def __rsub__(self, bfs11530):
    (x, y) = bfs11530
    return Point((x - self.x), (y - self.y))


def switch_to(window):
  """EXPORT
	:param window: The title (string) of a browser window or a :py:class:`Window` object

	Switches to the given browser window. For example::

		switch_to("Google")

	This searches for a browser window whose title contains "Google", and
	activates it.

	If there are multiple windows with the same title, then you can use
	:py:func:`find_all` to find all open windows, pick out the one you want and
	pass that to ``switch_to``. For example, the following snippet switches to
	the first window in the list of open windows::

		switch_to(find_all(Window())[0])
	"""
  getLogger(__name__).info(bfs10144(switch_to, window))
  bfs11502().bfs10641(window)

def kill_browser():
  """EXPORT
	Closes the current browser with all associated windows and potentially open
	dialogs. Dialogs opened as a response to the browser closing (eg. "Are you
	sure you want to leave this page?") are also ignored and closed.

	This function is most commonly used to close the browser at the end of an
	automation run::

		start_chrome()
		...
		# Close Chrome:
		kill_browser()
	"""
  getLogger(__name__).info(bfs10144(kill_browser))
  bfs11502().bfs10640()

def highlight(element):
  """EXPORT
	:param element: The element to highlight.

	Highlights the given element on the webpage by drawing a red rectangle
	around it. This is useful for debugging purposes. For example::

		highlight("Helium")
		highlight(Button("Sign in"))
	"""
  getLogger(__name__).info(bfs10144(highlight, element))
  bfs11502().bfs10643(element)

def bfs11502():
  return bfs11423().APIImpl()

