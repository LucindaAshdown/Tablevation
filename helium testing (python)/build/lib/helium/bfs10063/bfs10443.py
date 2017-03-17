from os import chmod, stat
from stat import S_IEXEC
def bfs10444(file_path):
  chmod(file_path, (stat(file_path).st_mode | S_IEXEC))

