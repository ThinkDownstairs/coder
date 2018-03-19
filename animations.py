
import enum
from enum import auto
import os

import pygame

import animation

DIRECTORY = '~/Bilder/coder/export'

_surfaces = {}
class SurfaceType(enum.Enum):
    VIM = auto()
    ATOM = auto()
    EMACS = auto()
    INTELLIJ = auto()
    NANO = auto()
    VSCODE = auto()

    BUG_RED_1 = auto()
    BUG_RED_2 = auto()
    BUG_GREEN_1 = auto()
    BUG_GREEN_2 = auto()
    BUG_YELLOW_1 = auto()
    BUG_YELLOW_2 = auto()
    BUG_GRAY_1 = auto()
    BUG_GRAY_2 = auto()

    TRY_EXCEPT = auto()
    CATCH_EXCEPTION = auto()

    FOR_LOOP = auto()

    FLOATINGPOINTERROR = auto()
    INDEXERROR = auto()
    KEYERROR = auto()
    MEMORYERROR = auto()
    NOTIMPLEMENTEDERROR = auto()
    OVERFLOWERROR = auto()
    RECURSIONERROR = auto()
    RUNTIMEERROR = auto()
    TYPEERROR = auto()

    def get_filename(self):
        if self == Surfaces.VIM: fn = 'vim.png'
        elif self == Surfaces.ATOM: fn = 'atom.png'
        elif self == Surfaces.EMACS: fn = 'emacs.png'
        elif self == Surfaces.INTELLIJ: fn = 'intellij.png'
        elif self == Surfaces.NANO: fn = 'nano.png'
        elif self == Surfaces.VSCODE: fn = 'vscode.png'
        elif self == Surfaces.BUG_RED_1: fn = 'bug-red-1.png'
        elif self == Surfaces.BUG_RED_2: fn = 'bug-red-2.png'
        elif self == Surfaces.BUG_GREEN_1: fn = 'bug-green-1.png'
        elif self == Surfaces.BUG_GREEN_2: fn = 'bug-green-2.png'
        elif self == Surfaces.BUG_YELLOW_1: fn = 'bug-yellow-1.png'
        elif self == Surfaces.BUG_YELLOW_2: fn = 'bug-yellow-2.png'
        elif self == Surfaces.BUG_GRAY_1: fn = 'bug-gray-1.png'
        elif self == Surfaces.BUG_GRAY_2: fn = 'bug-gray-2.png'
        elif self == Surfaces.TRY_EXCEPT: fn = 'try-except.png'
        elif self == Surfaces.CATCH_EXCEPTION: fn = 'catch-exception.png'
        elif self == Surfaces.FOR_LOOP: fn = 'for-loop.png'
        elif self == Surfaces.FLOATINGPOINTERROR: fn = 'floatingpointerror.png'
        elif self == Surfaces.INDEXERROR: fn = 'indexerror.png'
        elif self == Surfaces.KEYERROR: fn = 'keyerror.png'
        elif self == Surfaces.MEMORYERROR: fn = 'memoryerror.png'
        elif self == Surfaces.NOTIMPLEMENTEDERROR: fn = 'notimplementederror.png'
        elif self == Surfaces.OVERFLOWERROR: fn = 'overflowerror.png'
        elif self == Surfaces.RECURSIONERROR: fn = 'recursionerror.png'
        elif self == Surfaces.RUNTIMEERROR: fn = 'runtimeerror.png'
        elif self == Surfaces.TYPEERROR: fn = 'typeerror.png'
        else raise Exception('Unknown Surface Type: {}'.format(str(self)))
        return os.path.join(DIRECTORY, fn)

    def get_surface(self):
        if self in _surfaces:
            return _surfaces[self]
        surface = pygame.image.load(self.get_filename()).convert_alpha()
        _surfaces[self] = surface
        return surface


class Player(animation.Animation):
    def __init__(self, player_type: SurfaceType):
        super().__init__(player_type.get_surface(), 1, 1, False)

class Bug(animation.Animation):
    def __init__(self, bug_type: SurfaceType):
        super().__init__(bug_type.get_surface(), 3, 12, False)

class TryExcept(animation.Animation):
    def __init__(self):
        super().__init__(SurfaceType.TRY_EXCEPT.get_surface(), 1, 1, False)

class CatchException(animation.Animation):
    def __init__(self, x: int, y: int):
        super().__init__(SurfaceType.CATCH_EXCEPTION.get_surface(), 8, 20, True)
        self._x = x
        self._y = y

    def render(self, target, *args):
        super().render(target, self._x, self._y)

class Snippet(animation.Animation):
    def __init__(self, snippet_type: SurfaceType):
        super().__init__(snippet_type.get_surface(), 1, 1, False)

class Error(animation.Animation):
    def __init__(self, error_type: SurfaceType):
        super().__init__(error_type.get_surface(), 1, 1, False)


