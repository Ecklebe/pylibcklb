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
import os  
import sys
from PyQt5 import QtWidgets
from pylibcklb.ClassLibrary import cDebug 

Debug = cDebug(cDebug.LEVEL_ZERO)

## Documentation for a method to let the user search the correct directory.
#  @param self The object pointer of the the window class
#  @param windowname The name of the pop up window that describe what directory the user has to search
def BrowseFolder(self, windowname):        
    # execute getExistingDirectory dialog and set the directory variable to be equal to the user selected directory and return that
    return QtWidgets.QFileDialog.getExistingDirectory(self, windowname)      

## Documentation for a method to let the user search the correct directory to save a file
#   @code 
#   windowname = 'Search the folder to save to'
#   StringOfFiletypes = 'XML File (*.xml)'
#   dir = QT5FL.SaveFolder(self, windowname, StringOfFiletypes)
#   @endcode
#   @param self The object pointer of the the window class
#   @param windowname The name of the pop up window that describe what directory the user has to search
#   @param StringOfFiletypes Filter the files list for a specific type
def SaveFolder(self, windowname,StringOfFiletypes):
    return QtWidgets.QFileDialog.getSaveFileName(self, windowname,os.getcwd(), filter=StringOfFiletypes)[0]      

## Documentation for a method to let the user search the correct directory to load a file
#   @code 
#   windowname = 'Search the folder to load from'
#   StringOfFiletypes = 'XML File (*.xml)'
#   dir = QT5FL.SaveFolder(self, windowname, StringOfFiletypes)
#   @endcode
#   @param self The object pointer of the the window class
#   @param windowname The name of the pop up window that describe what directory the user has to search
#   @param StringOfFiletypes Filter the files list for a specific type
def LoadFolder(self, windowname,StringOfFiletypes):
    return QtWidgets.QFileDialog.getOpenFileName(self, windowname,os.getcwd(), filter=StringOfFiletypes)[0]    

## Documentation for a method to create a message box 
#   @note Is the MESSAGE_TYPE not none and from the MESSAGE_TYPE_LIST an ICON and WINDOW_TITLE is not necessary
#   @param SELF The object pointer of the the window class
#   @param MESSAGE Message to display at first in the box
#   @param INFORMATIVE_MESSAGE Message with more informations
#   @param DETAILED_MESSAGE Message with very detailed informations can be selected by drop down
#   @param WINDOW_TITLE The title of the window to set, only needed if MESSAGE_TYPE is not from MESSAGE_TYPE_LIST
#   @param MESSAGE_TYPE An type from the MESSAGE_TYPE_LIST
#   @param ICON The icon of the window to set, only needed if MESSAGE_TYPE is not from MESSAGE_TYPE_LIST
#   @return Value is True or if MESSAGE_TYPE == 'QUESTION' the answer of the question as true/false
def CreateMessageBox(SELF, MESSAGE = None, INFORMATIVE_MESSAGE = None, DETAILED_MESSAGE = None, WINDOW_TITLE = None, MESSAGE_TYPE = None, ICON = None):
    MESSAGE_TYPE_LIST = ['ERROR', 'WARNING', 'INFORMATION', 'QUESTION']
    msg = QtWidgets.QMessageBox(SELF)

    if MESSAGE_TYPE in MESSAGE_TYPE_LIST:
        if MESSAGE_TYPE == 'ERROR': 
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle('Error')
        elif MESSAGE_TYPE == 'WARNING': 
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle('Warning')        
        elif MESSAGE_TYPE == 'INFORMATION': 
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle('Information')
        elif MESSAGE_TYPE == 'QUESTION': 
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setWindowTitle('Question')
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    else:
        if WINDOW_TITLE is not None:
            msg.setWindowTitle(WINDOW_TITLE)
        else:
            msg.setWindowTitle('Informations')
        if ICON is not None:
            msg.setIcon(ICON)
        else:
            msg.setIcon(QtWidgets.QMessageBox.Information)

    if MESSAGE is not None:
        msg.setText(str(MESSAGE))
    else:
        msg.setText('No message to display')

    if INFORMATIVE_MESSAGE is not None:
        msg.setInformativeText(str(INFORMATIVE_MESSAGE))

    if DETAILED_MESSAGE is not None:
        msg.setDetailedText(str(DETAILED_MESSAGE))
    ret = msg.exec_() 

    if MESSAGE_TYPE == 'QUESTION': 
        if ret == QtWidgets.QMessageBox.Yes:
            return True
        else:
            return False
    else: 
        return True

## Documentation for a method to create a error message box 
#   @param SELF The object pointer of the the window class
#   @param ERROR_MESSAGE Message to display at first in the box
#   @param ERROR_INFORMATIVE_MESSAGE Message with more informations
#   @param ERROR_DETAILED_MESSAGE Message with very detailed informations can be selected by drop down
#   @return Value is True 
def CreateErrorMessage(SELF, ERROR_MESSAGE, ERROR_INFORMATIVE_MESSAGE, ERROR_DETAILED_MESSAGE = None):
    return CreateMessageBox(SELF, ERROR_MESSAGE, ERROR_INFORMATIVE_MESSAGE, ERROR_DETAILED_MESSAGE, MESSAGE_TYPE = 'ERROR')

## Documentation for a method to create a error message box 
#   @param SELF The object pointer of the the window class
#   @param WARNING_MESSAGE Message to display at first in the box
#   @param WARNING_INFORMATIVE_MESSAGE Message with more informations
#   @param WARNING_DETAILED_MESSAGE Message with very detailed informations can be selected by drop down
#   @return Value is True 
def CreateWarningMessage(SELF, WARNING_MESSAGE, WARNING_INFORMATIVE_MESSAGE, WARNING_DETAILED_MESSAGE = None):
    return CreateMessageBox(SELF, WARNING_MESSAGE, WARNING_INFORMATIVE_MESSAGE, WARNING_DETAILED_MESSAGE, MESSAGE_TYPE = 'WARNING')

## Documentation for a method to create a error message box 
#   @param SELF The object pointer of the the window class
#   @param INFORMATION_MESSAGE Message to display at first in the box
#   @param INFORMATION_INFORMATIVE_MESSAGE Message with more informations
#   @param INFORMATION_DETAILED_MESSAGE Message with very detailed informations can be selected by drop down
#   @return Value is True 
def CreateInformationMessage(SELF, INFORMATION_MESSAGE, INFORMATION_INFORMATIVE_MESSAGE, INFORMATION_DETAILED_MESSAGE = None):
    return CreateMessageBox(SELF, INFORMATION_MESSAGE, INFORMATION_INFORMATIVE_MESSAGE, INFORMATION_DETAILED_MESSAGE, MESSAGE_TYPE = 'INFORMATION')

## Documentation for a method to create a error message box 
#   @param SELF The object pointer of the the window class
#   @param QUESTION_MESSAGE Message to display at first in the box
#   @param QUESTION_INFORMATIVE_MESSAGE Message with more informations
#   @param QUESTION_DETAILED_MESSAGE Message with very detailed informations can be selected by drop down
#   @return The answer of the question as true/false
def CreateQuestionMessage(SELF, QUESTION_MESSAGE, QUESTION_INFORMATIVE_MESSAGE, QUESTION_DETAILED_MESSAGE = None):
    return CreateMessageBox(SELF, QUESTION_MESSAGE, QUESTION_INFORMATIVE_MESSAGE, QUESTION_DETAILED_MESSAGE, MESSAGE_TYPE = 'QUESTION')

## Documenation of a method to set the drag and drop mode of a qtreeview
# @param self The object pointer
# @param treeview a view with the type qtreeview
# @param expr The Mode as string that should be set: 'DragOnly',
# 'DropOnly', 'DropAndDrop'
def SetDragDropMode(self, treeview, expr='NoDragDrop'):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)
    if expr == 'DragOnly':
        treeview.setDragDropMode(QAbstractItemView.DragOnly)
    elif expr == 'DropOnly':
        treeview.setDragDropMode(QAbstractItemView.DropOnly)
    elif expr == 'DropAndDrop':
        treeview.setDragDropMode(QAbstractItemView.DragDrop)
    else:
        treeview.setDragDropMode(QAbstractItemView.NoDragDrop)
    return
