## Library of classes with installers  
#
# @file		    InstallerScriptLibrary.py
# @author	    Tobias Ecklebe tobias.ecklebe@outlook.de
# @date		    14.11.2017
# @version	    0.1.0
# @note		    This file includes classes as libary that i think are great for different projects.\n\n
#               To use this file:  from pylibcklb import InstallerScriptLibrary as ISL\n
#               To use a function: ISL.SomeClass()\n\n        
#
# @pre          The library was developed with python 3.6
#
# @bug          No bugs at the moment.
#
# @warning      No warning at the moment.
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
from subprocess import Popen

class PyInstaller:
    
    def BuildOnWindows(build_path, project_name, version_number):
        main_py = os.path.join(project_name, "main.py")
        icon_file = os.path.join(project_name, "resources", "logo", "logo.ico")

        Popen(["pyinstaller",
               main_py,
               "--onefile",
               "--windowed",
               "--icon=" + icon_file]).wait()

        file_name = project_name + "-windows-" + version_number + ".exe"
        file_origin = os.path.join("dist", "main.exe")
        file_destination = os.path.join(build_path, file_name)

        os.rename(file_origin, file_destination)


    def BuildOnLinux(build_path, project_name, version_number):
        Popen(["pyinstaller", os.path.join(project_name, "main.py"), "--onefile"]).wait()

        file_name = project_name + "-linux-" + version_number
        file_origin = os.path.join("dist", "main")
        file_destination = os.path.join(build_path, file_name)

        os.rename(file_origin, file_destination)

    def CreateSpec():
       print('Create the installer spec')



