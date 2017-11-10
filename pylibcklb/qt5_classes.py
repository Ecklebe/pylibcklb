## qt class libary file for all classes related to pyqt5
#
# @file		    qt5_classes.py
# @author	    Tobias Ecklebe tobias.ecklebe@outlook.de
# @date		    01.11.2017
# @version	    0.1.0
# @note		    This file includes functions as libary that i think are great for different projects.\n\n
#               To use this file:  from pylibcklb import qt5_classes as QT5CL\n
#               To use a function: QT5CL.SomeFuction()\n\n        
#               
# @pre          The library was developed with python 3.6 and pyqt5 
#
# @bug          No bugs at the moment.
#
# @warning      No warnings at the moment.
#
# @copyright    Filtergenerator for ADTF
#               Copyright (C) 2017  Tobias Ecklebe
#
#               This program is free software: you can redistribute it and/or modify
#               it under the terms of the GNU Lesser General Public License as published by
#               the Free Software Foundation, either version 3 of the License, or
#               (at your option) any later version.
#
#               This program is distributed in the hope that it will be useful,
#               but WITHOUT ANY WARRANTY; without even the implied warranty of
#               MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#               GNU Lesser General Public License for more details.
#
#               You should have received a copy of the GNU Lesser General Public License
#               along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .ClassLibrary import cDebug 

Debug = cDebug(cDebug.LEVEL_ZERO)

