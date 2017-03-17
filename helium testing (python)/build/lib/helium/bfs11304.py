from ConfigParser import RawConfigParser
bfs11303 = 'Helium.ini'
class bfs11305(object):
  def __init__(self, bfs11306):
    self.bfs11310 = RawConfigParser()
    self.bfs11310.read(bfs11306)
    self.bfs11307 = self.bfs11310.get('build', 'version')
    self.bfs11311 = self.bfs11310.get('build', 'checksum')
    self.bfs11313 = self.bfs11310.get('server', 'host')
    self.bfs11312 = self.bfs11310.getint('server', 'port')
    self.bfs11314 = self.bfs11310.get('server', 'path')


