## qt functions libary file for all functions related to pyqt5
#
# @file		    qt5_functions.py
# @author	    Tobias Ecklebe efos@ecklebe.de
# @date		    25.08.2017
# @version	    0.1.0
# @note		    This file includes functions as libary that i think are great for different projects.\n\n
#               To use this file:  from pylibcklb import qt5_functions as QT5FL\n
#               To use a function: QT5FL.SomeFuction()\n\n        
#               
# @pre          The programm was developed with python 3.5 and pyqt5 and the following modules and installation possiblites:
#               - nothing at the moment
#
# @bug          No bugs at the moment.
#
# @warning      The functions need a self pointer of the qt application! 
#
# @copyright    Unknown at this stage of implemantation.
#
import os  
import sys
from PyQt5 import QtWidgets
from .ClassLibrary import cDebug 

Debug = cDebug(cDebug.LEVEL_ZERO)

## Documentation for a method to let the user search the correct directory.
#  @param self The object pointer of the the window class
#  @param windowname The name of the pop up window that describe what directory the user has to search
def BrowseFolder(self, windowname):        
    # execute getExistingDirectory dialog and set the directory variable to be equal to the user selected directory and return that
    return QtWidgets.QFileDialog.getExistingDirectory(self, windowname)      

## Documentation for a method to let the user search the correct directory to save a file
#  @param self The object pointer of the the window class
#  @param windowname The name of the pop up window that describe what directory the user has to search
#  @param StringOfFiletypes Filter the files list for a specific type
def SaveFolder(self, windowname,StringOfFiletypes):
    return QtWidgets.QFileDialog.getSaveFileName(self, windowname,os.getcwd(), filter=StringOfFiletypes)[0]      

## Documentation for a method to let the user search the correct directory to load a file
#  @param self The object pointer of the the window class
#  @param windowname The name of the pop up window that describe what directory the user has to search
#  @param StringOfFiletypes Filter the files list for a specific type
def LoadFolder(self, windowname,StringOfFiletypes):
    return QtWidgets.QFileDialog.getOpenFileName(self, windowname,os.getcwd(), filter=StringOfFiletypes)[0]    
