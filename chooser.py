
import state_manager
import pygame
import os
import animations
import quit_
import menu
import consts


LEFT = 25
TOP = 5
STEP = 20
WIDTH = 90
HEIGHT = 90

ATOM_TEXT = """
Atom is a free and open-source text and source code editor for macOS, Linux,
and Microsoft Windows with support for plug-ins written in Node.js, and
embedded Git Control, developed by GitHub. Atom is a desktop application built
using web technologies. Most of the extending packages have free software
licenses and are community-built and maintained. Atom is based on Electron
(formerly known as Atom Shell), a framework that enables cross-platform
desktop applications using Chromium and Node.js. It is written in CoffeeScript
and Less. It can also be used as an integrated development environment (IDE).
Atom was released from beta, as version 1.0, on 25 June 2015. Its developers
call it a "hackable text editor for the 21st Century".
"""
EMACS_TEXT = """
GNU Emacs is the most popular and most ported Emacs text editor. It was
created by GNU Project founder Richard Stallman. In common with other
varieties of Emacs, GNU Emacs is extensible using a Turing complete
programming language. GNU Emacs has been called "the most powerful text editor
available today." With proper support from the underlying system, GNU Emacs is
able to display files in multiple character sets, and has been able to
simultaneously display most human languages since at least 1999. Throughout
its history, GNU Emacs has been a central component of the GNU project, and a
flagship of the free software movement. GNU Emacs is sometimes abbreviated as
GNUMACS, especially to differentiate it from other EMACS variants. The tag
line for GNU Emacs is "the extensible self-documenting text editor".
"""
INTELLIJ_TEXT = """
IntelliJ IDEA is a Java integrated development environment (IDE) for
developing computer software. It is developed by JetBrains (formerly known as
IntelliJ), and is available as an Apache 2 Licensed community edition, and in
a proprietary commercial edition. Both can be used for commercial development.

The first version of IntelliJ IDEA was released in January 2001, and was one
of the first available Java IDEs with advanced code navigation and code
refactoring capabilities integrated.
"""
NANO_TEXT = """
GNU nano is a text editor for Unix-like computing systems or operating
environments using a command line interface. It emulates the Pico text editor,
part of the Pine email client, and also provides additional functionality.
Unlike Pico, nano is licensed under the GNU General Public License (GPL).
Released as free software by Chris Allegretta in 1999, nano became part of the
GNU Project in 2001.

GNU nano implements some features that Pico lacks, including colored text,
regular expression search and replace, smooth scrolling, multiple buffers,
rebindable key support, and undoing and redoing of edit changes.
"""
VIM_TEXT = """
Vim (a contraction of Vi IMproved) is a clone of Bill Joy's vi text editor
program for Unix. It was written by Bram Moolenaar based on source for a port
of the Stevie editor to the Amiga and first released publicly in 1991. Vim is
designed for use both from a command-line interface and as a standalone
application in a graphical user interface. Vim is free and open source
software and is released under a license that includes some charityware
clauses, encouraging users who enjoy the software to consider donating to
children in Uganda. The license is compatible with the GNU General Public
License through a special clause allowing distribution of modified copies
"under the GNU GPL version 2 or any later version".
Although it was originally released for the Amiga, Vim has since been
developed to be cross-platform, supporting many other platforms. In 2006, it
was voted the most popular editor amongst Linux Journal readers; in 2015 the
Stack Overflow developer survey found it to be the third most popular text
editor; and in 2016 the Stack Overflow developer survey found it to be the
fourth most popular development environment.
"""
VSCODE_TEXT = """
Visual Studio Code is a source code editor developed by Microsoft for Windows,
Linux and macOS. It includes support for debugging, embedded Git control,
syntax highlighting, intelligent code completion, snippets, and code
refactoring. It is also customizable, so users can change the editor's theme,
keyboard shortcuts, and preferences. It is free and open-source, although the
official download is under a proprietary license.
Visual Studio Code is based on Electron, a framework which is used to deploy
Node.js applications for the desktop running on the Blink layout engine.
Although it uses the Electron framework, the software does not use Atom and
instead employs the same editor component (codenamed "Monaco") used in Visual
Studio Team Services (formerly called Visual Studio Online).
In the Stack Overflow 2018 Developer Survey, Visual Studio code was ranked the
most popular developer environment tool, with 34.9% of 75398 respondents
claiming to use it.
"""
RANDOM_TEXT = """
A pseudorandom number generator (PRNG), also known as a deterministic random
bit generator (DRBG), is an algorithm for generating a sequence of numbers
whose properties approximate the properties of sequences of random numbers.
The PRNG-generated sequence is not truly random, because it is completely
determined by an initial value, called the PRNG's seed (which may include
truly random values). Although sequences that are closer to truly random can
be generated using hardware random number generators, pseudorandom number
generators are important in practice for their speed in number generation and
their reproducibility.
PRNGs are central in applications such as simulations (e.g. for the Monte
Carlo method), electronic games (e.g. for procedural generation), and
cryptography. Cryptographic applications require the output not to be
predictable from earlier outputs, and more elaborate algorithms, which do not
inherit the linearity of simpler PRNGs, are needed.
"""


chosen_editor = None

class Chooser(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._idx = 0
        self._mouse = (consts.SCREEN_W + 1, consts.SCREEN_H + 1)
        self._font = pygame.font.Font('DejaVuSansMono.ttf', 16)
        self._texts = [
            self._text(ATOM_TEXT),
            self._text(EMACS_TEXT),
            self._text(INTELLIJ_TEXT),
            self._text(NANO_TEXT),
            self._text(VIM_TEXT),
            self._text(VSCODE_TEXT),
            self._text(RANDOM_TEXT)]
        self._animations = [
            animations.Player(animations.Surfaces.ATOM),
            animations.Player(animations.Surfaces.EMACS),
            animations.Player(animations.Surfaces.INTELLIJ),
            animations.Player(animations.Surfaces.NANO),
            animations.Player(animations.Surfaces.VIM),
            animations.Player(animations.Surfaces.VSCODE),
            animations.RandomEditor()]

    def _text(self, text: str) -> pygame.Surface:
        lines = [self._font.render(txt, True, (255, 255, 255), None) for txt in text.split('\n')]
        if len(lines) > 0:
            line_height = int(self._font.get_height() * 1.5)
            surface = pygame.Surface((consts.SCREEN_W - 10, line_height * len(lines)), pygame.SRCALPHA, None)
            offset = 0
            for line in lines:
                surface.blit(line, (0, offset))
                offset += line_height
        return surface

    def _select(self, clicked: bool):
        global chosen_editor
        x, y = self._mouse
        if TOP < y < (HEIGHT + TOP):
            for i in range(len(self._animations)):
                if (LEFT + i * (WIDTH + STEP)) < x < ((LEFT + i * (WIDTH + STEP)) + WIDTH):
                    self._idx = i
                    if clicked:
                        if isinstance(self._animations[self._idx], animations.Player):
                            chosen_editor = self._animations[self._idx]
                        else:
                            chosen_editor = None
                        self.state_manager.change_state(menu.Menu)
                    break


    def render(self) -> None:
        left = LEFT
        top = TOP
        step = STEP
        self.screen.fill((0, 0, 0))
        for i in range(len(self._animations)):
            s = self._animations[i].surface
            w, h = s.get_size()
            self.screen.blit(s, (left + (WIDTH // 2 - w // 2), top + (HEIGHT // 2 - h // 2)))
            if i == self._idx:
                pygame.draw.rect(self.screen, (255, 255, 255), (left - 2, top - 2, WIDTH + 4, HEIGHT + 4), 3)
            left += (w + step)
        self.screen.blit(self._texts[self._idx], (5, TOP + HEIGHT + STEP))
        pygame.draw.line(self.screen, (255, 255, 255), (self._mouse[0], self._mouse[1] - 10), (self._mouse[0], self._mouse[1] + 10), 2)
        pygame.draw.line(self.screen, (255, 255, 255), (self._mouse[0] - 10, self._mouse[1]), (self._mouse[0] + 10, self._mouse[1]), 2)
        pygame.display.flip()

    def input(self) -> None:
        global chosen_editor
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_manager.change_state(quit_.Quit)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._idx -= 1
                    if self._idx < 0:
                        self._idx = len(self._animations) - 1
                elif event.key == pygame.K_RIGHT:
                    self._idx += 1
                    if self._idx >= len(self._animations):
                        self._idx = 0
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if isinstance(self._animations[self._idx], animations.Player):
                        chosen_editor = self._animations[self._idx]
                    else:
                        chosen_editor = None
                    self.state_manager.change_state(menu.Menu)
                elif event.key == pygame.K_ESCAPE:
                    self.state_manager.change_state(menu.Menu)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                l, m, r = pygame.mouse.get_pressed()
                if l == 1:
                    self._select(True)
            elif event.type == pygame.MOUSEMOTION:
                self._mouse = event.pos
                self._select(False)


    def update(self, delta: int, fps: float) -> None:
        for animation in self._animations:
            animation.update(delta)

    def leave(self, next_: state_manager.StateType) -> None:
        pass

    def enter(self, prev_: state_manager.StateType) -> None:
        global chosen_editor
        if chosen_editor is None:
            self._idx = len(self._animations) - 1
        else:
            for i in range(len(self._animations)):
                if self._animations[i] == chosen_editor:
                    self._idx = i
                    break
