from hashlib import md5
from uuid import getnode
from platform import node as bfs11260, machine, system as bfs11262
from getpass import getuser
from _socket import gethostname
from ctypes import c_ulonglong, byref
import os, platform, ctypes, sys
if hasattr(os, 'statvfs'):
  def bfs11265(path):
    bfs11263 = os.statvfs(path)
    return (bfs11263.f_blocks * bfs11263.f_frsize)

elif (os.name == 'nt'):
  def bfs11265(path):
    (bfs11264, bfs11266, bfs11267) = (c_ulonglong(), c_ulonglong(), c_ulonglong())
    if ((sys.version_info >= (3,)) or isinstance(path, str)):
      bfs11270 = ctypes.windll.kernel32.GetDiskFreeSpaceExW
    else:
      bfs11270 = ctypes.windll.kernel32.GetDiskFreeSpaceExA

    bfs11271 = bfs11270(path, byref(bfs11264), byref(bfs11266), byref(bfs11267))
    if (bfs11271 == 0):
      raise ctypes.WinError()

    return bfs11266.value


class bfs11273(object):
  def __init__(self):
    self.bfs11272 = None

  def bfs10213(self):
    if (self.bfs11272 is None):
      self.bfs11272 = self.bfs11274()

    return self.bfs11272

  def bfs11275(self):
    return (bfs11260() or gethostname() or 'unknown')

  def bfs11274(self):
    bfs11277 = (str(getnode()) + bfs11260())
    return md5(bfs11277.encode('ASCII')).hexdigest()

  def bfs11276(self):
    return self.bfs10213()

  def bfs11300(self):
    return self.bfs10213()

  def bfs11301(self):
    return self.bfs10213()

  def bfs10216(self):
    os = bfs11262().lower()
    if (('darwin' in os) or ('mac' in os)):
      return 'OSX'

    if ('nux' in os):
      return 'Linux'

    if (('win' in os) or ('cygwin' in os)):
      return 'Windows'

    return 'Unknown'

  def bfs10220(self):
    if (self.bfs10216() == 'OSX'):
      return platform.mac_ver()[0]

    return platform.release()

  def bfs10217(self):
    bfs11302 = ('C:\\' if (os.name == 'nt') else '/')
    return bfs11265(bfs11302)

  def bfs10221(self):
    return str('{0:x}'.format(getnode()))

  def bfs10222(self):
    return bfs11260()

  def bfs10223(self):
    return machine()

  def bfs10225(self):
    return getuser()


