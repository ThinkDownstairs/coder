
import enum
from enum import auto
import os

import pygame
import random

import animation
import locations


_surfaces = {}
class Surfaces(enum.Enum):
    VIM = auto()
    ATOM = auto()
    EMACS = auto()
    INTELLIJ = auto()
    NANO = auto()
    VSCODE = auto()
    RANDOM = auto()

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

    FLOATINGPOINTERROR = auto()
    INDEXERROR = auto()
    KEYERROR = auto()
    MEMORYERROR = auto()
    NOTIMPLEMENTEDERROR = auto()
    OVERFLOWERROR = auto()
    RECURSIONERROR = auto()
    RUNTIMEERROR = auto()
    TYPEERROR = auto()

    FIBONACCI = auto()
    FOR_I_IN_RANGE = auto()
    FOR_ITEM_IN_ITEMS = auto()
    IMPORT_PYGAME = auto()
    PRINT_HELLO_WORLD = auto()
    REVERSE = auto()
    SQR_LAMBDA = auto()
    STR_JOIN = auto()
    XY_POINT = auto()

    COFFEE = auto()
    COFFEE_BROKEN = auto()

    EXPLOSION = auto()
    EFFECT = auto()


    def get_filename(self):
        if self == Surfaces.VIM: fn = 'vim.png'
        elif self == Surfaces.ATOM: fn = 'atom.png'
        elif self == Surfaces.EMACS: fn = 'emacs.png'
        elif self == Surfaces.INTELLIJ: fn = 'intellij.png'
        elif self == Surfaces.NANO: fn = 'nano.png'
        elif self == Surfaces.VSCODE: fn = 'vscode.png'
        elif self == Surfaces.RANDOM: fn = 'random-editor.png'
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
        elif self == Surfaces.FLOATINGPOINTERROR: fn = 'floatingpointerror.png'
        elif self == Surfaces.INDEXERROR: fn = 'indexerror.png'
        elif self == Surfaces.KEYERROR: fn = 'keyerror.png'
        elif self == Surfaces.MEMORYERROR: fn = 'memoryerror.png'
        elif self == Surfaces.NOTIMPLEMENTEDERROR: fn = 'notimplementederror.png'
        elif self == Surfaces.OVERFLOWERROR: fn = 'overflowerror.png'
        elif self == Surfaces.RECURSIONERROR: fn = 'recursionerror.png'
        elif self == Surfaces.RUNTIMEERROR: fn = 'runtimeerror.png'
        elif self == Surfaces.TYPEERROR: fn = 'typeerror.png'
        elif self == Surfaces.FIBONACCI: fn = 'fibonacci.png'
        elif self == Surfaces.FOR_I_IN_RANGE: fn = 'for-i-in-range.png'
        elif self == Surfaces.FOR_ITEM_IN_ITEMS: fn = 'for-item-in-items.png'
        elif self == Surfaces.IMPORT_PYGAME: fn = 'import-pygame.png'
        elif self == Surfaces.PRINT_HELLO_WORLD: fn = 'print-hello-world.png'
        elif self == Surfaces.REVERSE: fn = 'reverse.png'
        elif self == Surfaces.SQR_LAMBDA: fn = 'sqr-lambda.png'
        elif self == Surfaces.STR_JOIN: fn = 'str-join.png'
        elif self == Surfaces.XY_POINT: fn = 'xy-point.png'
        elif self == Surfaces.COFFEE: fn = 'coffee.png'
        elif self == Surfaces.COFFEE_BROKEN: fn = 'coffee-broken.png'
        elif self == Surfaces.EXPLOSION: fn = 'bug-explode.png'
        elif self == Surfaces.EFFECT: fn = 'effect.png'
        else: raise Exception('Unknown Surface Type: {}'.format(str(self)))
        return locations.image(fn)

    def get_surface(self):
        global _surfaces
        if self in _surfaces:
            return _surfaces[self]
        surface = pygame.image.load(self.get_filename()).convert_alpha()
        _surfaces[self] = surface
        return surface


class Player(animation.Animation):
    def __init__(self, player_type: Surfaces):
        super().__init__(player_type.get_surface(), 1, 1, True)

class RandomEditor(animation.Animation):
    def __init__(self):
        super().__init__(Surfaces.RANDOM.get_surface(), 6, 6, False)



class Bug(animation.Animation):
    def __init__(self, bug_type: Surfaces):
        super().__init__(bug_type.get_surface(), 3, 8, False)

class TryExcept(animation.Animation):
    def __init__(self):
        super().__init__(Surfaces.TRY_EXCEPT.get_surface(), 1, 1, True)

class CatchException(animation.Animation):
    def __init__(self):
        super().__init__(Surfaces.CATCH_EXCEPTION.get_surface(), 8, 8, True)

class Snippet(animation.Animation):
    def __init__(self, snippet_type: Surfaces):
        super().__init__(snippet_type.get_surface(), 1, 1, True)

class Error(animation.Animation):
    def __init__(self, error_type: Surfaces):
        super().__init__(error_type.get_surface(), 1, 1, True)

class Coffee(animation.Animation):
    def __init__(self):
        super().__init__(Surfaces.COFFEE.get_surface(), 5, 6, False)

class CoffeeBroken(animation.Animation):
    def __init__(self):
        super().__init__(Surfaces.COFFEE_BROKEN.get_surface(), 1, 1, True)

class Explosion(animation.Animation):
    def __init__(self):
        super().__init__(Surfaces.EXPLOSION.get_surface(), 5, 8, True)


class Effect(animation.Animation):
    def __init__(self):
        super().__init__(Surfaces.EFFECT.get_surface(), 5, 6, False)


