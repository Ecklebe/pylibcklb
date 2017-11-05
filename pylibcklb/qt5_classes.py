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
# @copyright    Unknown at this stage of implemantation.
#
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .ClassLibrary import cDebug 

Debug = cDebug(cDebug.LEVEL_ZERO)

