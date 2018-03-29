
import os
import sys

_root = None
def get_root():
    global _root
    if _root is None:
        if getattr(sys, 'frozen', False):
            _root = sys._MEIPASS
        else:
            _root = os.path.dirname(os.path.abspath(__file__))
    return _root

def sound(filename: str):
    return os.path.join(get_root(), 'res', 'sounds', filename)

def image(filename: str):
    # todo: change to 'image'
    return os.path.join(get_root(), 'res', 'export', filename)

def user(filename: str):
    directory = os.path.join(os.path.expanduser('~'), '.thinkdownstairs', 'coder')
    if not os.path.exists(directory):
        os.makedirs(directory)
    return os.path.join(directory, filename)

