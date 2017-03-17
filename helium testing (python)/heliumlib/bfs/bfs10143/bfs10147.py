class LicensingError(Exception):
  pass

class InvalidLicenseFile(LicensingError):
  pass

class LicenseInvalid(LicensingError):
  def __init__(self, message):
    super(LicenseInvalid, self).__init__(message)
    self.message = message


