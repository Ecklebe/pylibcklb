## Function library file for my functions 
#
# @file		    FunctionLibrary.py
# @author	    Tobias Ecklebe tobias.ecklebe@outlook.de
# @date		    05.11.2017
# @version	    0.3.0
# @note		    This file includes functions as libary that i think are great for different projects.\n\n
#               To use this file:  from pylibcklb import FunctionLibrary as FL\n
#               To use a function: FL.SomeFuction()\n\n        
#               Some ideas:
#               - Create an executable for user without installed python 
#                   - https://mborgerson.com/creating-an-executable-from-a-python-script    
#                   - Install of pyinstaller:  python -m pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip --upgrade

# @pre          The library was developed with python 3.6 
#
# @bug          No bugs at the moment.
#
# @warning      No warnings at the moment
#
# @copyright    pylibcklb package
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
from pylibcklb.ClassLibrary import cDebug 
import fileinput
from pylibcklb.metadata import PackageVariables
Debug = cDebug(PackageVariables.DebugLevel)

## Documentation for a method to get an bool from the xml string
# @param value Value from xml string
# @return Boolean extract from string
def str2bool(value):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)
    return value.lower() in ("True", "true")

## Documentation of a method to load a file from a pyinstaller bundled exe
# @note https://stackoverflow.com/questions/19669640/bundling-data-files-with-pyinstaller-2-1-and-meipass-error-onefile
# @param relative_path The realtive path to the file
def resource_path(relative_path):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        #simulate the top path, because in the project the main file is not in the root folder
        base_path = os.path.abspath("..")

    return os.path.join(base_path, relative_path)

## Documentation of a method to remove an defined prefix from an text
# @param text The string from which the prefix should be removed
# @param prefix The prefix that should be removed
# @return String without postfix if the text and prefix are from type string, else text without changes
def remove_prefix(text, prefix):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)
    if ((type(text) is str) and (type(prefix) is str)):
        if not text.startswith(prefix):
            return text
        return text[text.startswith(prefix) and len(prefix):]
    else: 
        print("Warning one of the variabels is no string")
        return text

## Documentation of a method to remove an defined postfix from an text
# @param text The string from which the postfix should be removed
# @param postfix The prefix that should be removed
# @return String without postfix if the text and prefix are from type string, else text without changes
def remove_postfix(text, postfix):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)
    if ((type(text) is str) and (type(postfix) is str)):
        if not text.endswith(postfix):
            return text
        return text[:len(text)-len(postfix)]
    else: 
        print("Warning one of the variabels is no string")
        return text

## Documentation of a method that checks the string if there is a known prefix
# @param text The text that should 
# @param ListOfPrefixes List of the prefixes to search in
# @return String with prefix if the there is a known prefix and None if no prefix
def IsThereAKnownPrefix(text, ListOfPrefixes):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)
    if type(text) is str:
        retValue = None
        Debug.Print(Debug.LEVEL_FUNCTIONENTRY, ('Input text is: ' + text))
        for i in range(len(ListOfPrefixes)):
            if text.startswith(ListOfPrefixes[i]): 
                retValue = ListOfPrefixes[i]     
        return retValue
    else:                 
        return None

## Documentation for a method to create an directory
#   @param dir The directory to create
#   @return The returned value is true to signalize that the directory is created
def CreateDir(dir):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)
    if not os.path.exists(dir):
        os.makedirs(dir)
    return True

## Documentation for a method to let the user search the correct directory to load a file
#   @code 
#   ret = CreateFile('Some Text', 'Path2Dir\Filename.txt')
#   @endcode
#   @param FileContent The content to save into the new file
#   @param Dir The directory to create the file, the directory parameter must have included the filename and filetype
def CreateFile(FileContent, Dir):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)
    os.makedirs(os.path.dirname(Dir), exist_ok=True)
    with open(Dir, "w") as f:
        f.write(str(FileContent))
    return True

## Documentation for a method to save the changes of an dict back to the file for remembering on next application start
#   @param FileDir The directory of the file
#   @param FileName The name of the file where the dict is placed
#   @param DictName Name of the dict as string the method should search for
#   @param Dict The dict that should be saved back
def SaveChangesOfDictBack2File(FileDir:str, FileName:str, DictName:str, Dict:dict):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)
    dir = os.path.join(FileDir, FileName)
    # Safely read the input filename using 'with'
    with open(dir) as f:
        s = f.read()
        if DictName not in s:
            Debug.Print(Debug.LEVEL_All, '"{DictName}" not found in {FileName}.'.format(**locals()))
            return False

    ParameterValue = None
    for line in s.splitlines():
        if DictName in line:
            ParameterName, ParameterValue = line.split('=')

    if ParameterValue is not None:
        old_string = ParameterValue
        new_string = str(Dict)
        # Safely write the changed content, if found in the file
        with open(dir, 'w') as f:
            Debug.Print(Debug.LEVEL_All,'Changing "{old_string}" to "{new_string}" in {dir}'.format(**locals()))
            s = s.replace(old_string, new_string)
            f.write(s)
        return True
    else:
        return False
