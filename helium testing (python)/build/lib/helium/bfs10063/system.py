from os import popen
import os
import sys
def bfs10445():
  return (sys.platform in ('win32', 'cygwin'))

def bfs10447():
  return (sys.platform == 'darwin')

def bfs10446():
  return sys.platform.startswith('linux')

def bfs10450():
  if bfs10445():
    return 'win'
  elif bfs10447():
    return 'macosx'
  elif bfs10446():
    return 'linux'


def bfs10451():
  if bfs10445():
    return ('PROGRAMFILES(X86)' not in os.environ)

  assert (bfs10446() or bfs10447())
  return (bfs10452() in ('i386', 'i686'))

def bfs10452():
  return popen('uname -m').read().strip()

def bfs10453():
  if bfs10445():
    return ('PROGRAMFILES(X86)' in os.environ)

  assert (bfs10446() or bfs10447())
  return (bfs10452() in ('x86_64', 'ia64', 'amd64'))

