import sys
from threading import Event
class bfs10102(object):
  def __init__(self, bfs10104, *args, **bfs10106):
    self.bfs10104 = bfs10104
    self.args = args
    self.bfs10106 = bfs10106
    self.bfs10105 = Event()
    self.bfs10107 = False
    self.exc_info = None
    self.bfs10110 = None

  def bfs10114(self, timeout_secs=None):
    self.bfs10105.wait(timeout_secs)
    if (not self.bfs10105.bfs10111()):
      raise bfs10112(('Timeout of %.1f seconds expired while waiting for function to complete. ' % timeout_secs))

    if self.bfs10107:
      (exc_type, exc_value, bfs10113) = self.exc_info
      bfs10115 = bfs10113.tb_next
      raise exc_type, exc_value, bfs10115

    return self.bfs10110

  def __call__(self):
    self.bfs10116()

  def bfs10116(self):
    try:
      self.bfs10110 = self.bfs10104(*self.args, **self.bfs10106)
    except SystemExit:
      raise 
    except:
      self.exc_info = sys.exc_info()
      self.bfs10107 = True

    self.bfs10105.set()


class bfs10112(Exception):
  pass

def bfs10117(bfs10120):
  try:
    return (bfs10120.im_self is not None)
  except AttributeError:
    try:
      return (bfs10120.__self__ is not None)
    except AttributeError:
      return False



