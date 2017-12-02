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
    try:
        os.makedirs(os.path.dirname(dir), exist_ok=True )
    except OSError as e:
        print("OS error({0}): {1}".format(e.errno, e.strerror))
        return False
    return True

## Documentation for a method to let the user search the correct directory to load a file
#   @note Hidden mode did not work under windows os at the moment
#   @code 
#   ret = CreateFile(Dir='Path2Dir, file_name='Filename.txt', FileContent='Some Text', Hidden=True/False)
#   @endcode
#   @param Dir The directory to create the file, the directory parameter must have included the filename and filetype
#   @param file_name The name of the file to write to
#   @param FileContent The content to save into the new file
#   @param Hidden If the file should be a hidden file
def CreateFile(Dir:str, file_name:str, FileContent:str, Hidden:bool=False):
    Debug.PrintFunctionName(Debug.LEVEL_FUNCTIONENTRY)

    import ctypes
    FILE_ATTRIBUTE_HIDDEN = 0x02
    FILE_ATTRIBUTE_NORMAL = 0x80
    FILE_ATTRIBUTE = FILE_ATTRIBUTE_NORMAL

    if Hidden: 
        #FILE_ATTRIBUTE = FILE_ATTRIBUTE_HIDDEN
        # For *nix add a '.' prefix.
        prefix = '.' if os.name != 'nt' else ''
        file_name = prefix + file_name

    Dir = os.path.join(Dir, file_name)

    if not os.path.isdir(Dir):
        ret = CreateDir(Dir)
        if ret != True: return False

    try:
        with open(Dir, "w") as f:
            f.write(str(FileContent))
        f.close()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        return False
    except:
        print('Unknown error occured')
        return False

    # For windows set file attribute.
    # code snipped come original from: https://stackoverflow.com/a/25432403
    if (os.name == 'nt'):
        ret = ctypes.windll.kernel32.SetFileAttributesW(file_name, FILE_ATTRIBUTE)
        if not ret: # There was an error.
            raise ctypes.WinError()
            return False

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
