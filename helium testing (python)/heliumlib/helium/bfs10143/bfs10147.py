from bfs.bfs10143.bfs10147 import LicensingError
class NoLicenseKeyFound(LicensingError):
  def __init__(self, message):
    super(NoLicenseKeyFound, self).__init__(message)
    self.message = message


class bfs10163(LicensingError):
  pass

