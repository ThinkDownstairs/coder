#
# Makefile for CODER
# a game for the #MetaGameJam
#
# Author: Lukas Singer
#
# Created: 2018-03-25
#


#################
#               #
# CONFIGURATION #
#               #
#################


# the name of the game
NAME=coder

# the directory for the virtual enviroment
# HINT: dont change this, this is also a targets name!
VIRTUALENV=venv

# the "compiler" for the game (the executable)
PY-CC=python -OO $(VIRTUALENV)/bin/pyinstaller

# the "compiler" for the build info
BUILD-INFO-CC=python generate_build_info.py

BIN-DIR=bin

# the temp dir (f.e. for creating the docs or creating the executable)
TMP-DIR=tmp

IMAGES-SRC=images/*.png
IMAGES-DEST=images

SOUNDS-SRC=sounds/*.ogg
SOUNDS-DEST=sounds

FONTS-SRC=fonts/*.ttf
FONTS-DEST=fonts

# the build info file
BUILD-INFO-FILE=build_info.py

# the main source file
SRC-FILE=coder.py

# the requirements file
REQ-FILE=requirements.txt

# activation and deactivation commands for the virtual enviroment
ACTIVATE-VIRTUALENV=. $(VIRTUALENV)/bin/activate
DEACTIVATE-VIRTUALENV=deactivate

# flags for the "compiler" for the game
PY-CC-FLAGS=--clean --onefile --strip --log-level=WARN
PY-CC-ADD-DATA=--add-data '$(IMAGES-SRC):$(IMAGES-DEST)' --add-data '$(SOUNDS-SRC):$(SOUNDS-DEST)' --add-data '$(FONTS-SRC):$(FONTS-DEST)'


###########
#         #
# TARGETS #
#         #
###########


# build the game when invoked with:
#   $ make
default:
	( \
	  $(ACTIVATE-VIRTUALENV) ; \
	  $(BUILD-INFO-CC) --output=$(BUILD-INFO-FILE) ; \
	  $(PY-CC) $(PY-CC-FLAGS) $(PY-CC-ADD-DATA) --distpath=$(BIN-DIR) --name $(NAME) $(SRC-FILE) ; \
	  $(DEACTIVATE-VIRTUALENV) ; \
	)


# create the virtual enviroment and install requirements when invoked with:
#   $ make venv
.PHONY: $(VIRTUALENV)
$(VIRTUALENV):
	( \
	  python3 -m venv $(VIRTUALENV) ; \
	  $(ACTIVATE-VIRTUALENV) ; \
	  pip install -r $(REQ-FILE) ; \
	  $(DEACTIVATE-VIRTUALENV) ; \
	)

# remove the virtual enviroment when invoked with:
#   $ make clean-venv
clean-venv:
	rm -r $(VIRTUALENV)


# remove everything created with this Makefile (except the virtual enviroment) when invoked with:
#   $ make clean
.PHONY: clean
clean:
	rm -r $(BIN-DIR)
	rm -r $(TMP-DIR)
	rm $(BUILD-INFO-FILE)

