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

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pylibcklb.ClassLibrary import cDebug 
from abc import ABCMeta, abstractmethod

Debug = cDebug(cDebug.LEVEL_ZERO)

## Documentation for a class that handles as thread the reading from a directory.
# The reason for a thread is that while the programm searches in a great dir
# the gui will be frozen.
# The following code explaines the example usage:
# @code
## Creates an thread to fix the problem with an frozen gui while searching in the directory
#self.Thread_XMLFilesFromDir = QT5CL.GetThread_XMLFilesFromDir(CatalogsPath, FileType)
#            
## Next we need to connect the events from that thread to functions we want
## to be run when those signals get fired       
#self.Thread_XMLFilesFromDir.get_dir.connect(self.AddDir2ListWidget)
#self.Thread_XMLFilesFromDir.finished.connect(self.done)
#
## We have all the events we need connected we can start the thread
#self.Thread_XMLFilesFromDir.start()
## At this point we want to allow user to stop/terminate the thread so we enable that button
#self.ButtonLoadCatalogs_Stop.setEnabled(True)
## And we connect the click of that button to the built in terminate method that all QThread instances have
#self.ButtonLoadCatalogs_Stop.clicked.connect(self.Thread_XMLFilesFromDir.terminate)
## We don't want to enable user to start another thread while this one is running so we disable the start button.
#self.ButtonLoadCatalogs_Start.setEnabled(False)
# @endcode
#  @param QThread Inherit from QThread
class GetThread_XMLFilesFromDir(QThread):

    ## Documentation of the signals to throw away to listening functions
    get_dir = pyqtSignal('QString')

    ## Documentation of the constructor
    #  @param self The object pointer.
    #  @param directory The directory to search in
    #  @param filetype The filetype to search for as string. Example filetype='.xml'
    def __init__(self, directory, filetype):
        QThread.__init__(self)
        self.CatalogsDir = directory  
        self.FileType = filetype     
        return  

    ## Documentation of the destructor
    #  @param self The object pointer.
    def __del__(self): 
        self.wait()
        return

    ## Documentation of the thread run part.
    # Function search in the given directory in all folders and subfolders for
    # files with the xml ending
    # and gives them back over the signal to the listening function.  After
    # that the thread sleeps to give the other function
    # some time to work with the data.
    #  @param self The object pointer.
    def run(self):     
        for path, subdirs, files in os.walk(self.CatalogsDir):
            for filename in files:
                if not filename.endswith(self.FileType): continue
                fullname = os.path.join(path, filename)
                self.get_dir.emit(fullname)
                self.msleep(100)     
        return

class cToolbar(QToolBar):

    ## Documentation of the constructor
    #  @param self The object pointer.
    def __init__(self, parent, visibility=False):
        QToolBar.__init__(self, parent)

        self.parent = parent
        self.setFloatable(False)
        self.setMovable(False)
        self.parent.addToolBar(Qt.TopToolBarArea, self)
        self.SetVisibility(visibility)

    def SetVisibility(self, visibility:bool):
        if visibility == True:
            self.show()
        else: 
            self.hide()

class cUndoToolbar(cToolbar):

    ## Documentation of the constructor
    #  @param self The object pointer.
    def __init__(self, parent, visibility=False):
        super(self.__class__, self).__init__(parent) 

        self.undoStack = QUndoStack(self)       
        self.UndoAction = self.undoStack.createUndoAction(self, self.tr("&Undo"))
        self.UndoAction.setShortcuts(QKeySequence.Undo)
        self.RedoAction = self.undoStack.createRedoAction(self, self.tr("&Redo"))
        self.RedoAction.setShortcuts(QKeySequence.Redo)

        self.addAction(self.UndoAction)
        self.addAction(self.RedoAction)

        self.SetVisibility(visibility)

    def GetUndoStack(self):
        return self.undostack

    def AddCommand2UndoStack(self, Command:QUndoCommand):
        self.undoStack.push(Command)

    def AddElement2UndoStack(self, Element):
        if type(Element) is QLineEdit:
            self.undoStack.push(Command2Store_QLineEdit(Element))
            return True
        else:
            return False

class cUndoCommand(QUndoCommand):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        QUndoCommand.__init__(self) 

    def undo(self):
        pass
    
    def redo(self):
        pass

class cCommand2Store_QLineEdit(cUndoCommand):

    def __init__(self, LineEdit : QLineEdit):
        super(self.__class__, self).__init__() 
        
        # Record the field that has changed.
        self.LineEdit = field
         
        # Record the text at the time the command was created.
        self.text = LineEdit.text()

    def undo(self):
    
        # Remove the text from the file and set it in the field.
        # ...
        self.LineEdit.setText(self.text)
    
    def redo(self):
    
        # Store the text in the file and set it in the field.
        # ...
        self.LineEdit.setText(self.text)