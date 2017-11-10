## Metadata file for the ADTF-Filtergenerator
#
# @file		    metadata.py
# @author	    Tobias Ecklebe
# @date		    09.11.2017
# @version	    0.1.0
# @note		    The metadata is stored here. It can be used by any other module in this project this way
# 
# @pre          The programm was developed with python 3.5 64Bit and pyqt5 an installation is possible over the installtaion batch script.
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

"""
The metadata is stored here. It can be used by any other module in this project this way
"""
from .version import __version__

class GitRepository:
    """
    Class that stores information about the git repository sites used by this project
    """

    repository_name = "pylibcklb"
    """
    The name of the repository
    """

    gitlab_owner = "open-source/python"
    """
    The project's owner's username on Gitlab
    """

    gitlab_site_url = "https://gitlab.ecklebe.de/"
    """
    The address of the Gitlab instance
    """

    gitlab_url = gitlab_site_url + gitlab_owner + "/" + repository_name
    """
    The Gitlab Project URL
    """


class General:
    """
    Class that stores general information about a project
    """

    project_description = 'The pylibcklb is a library of functions and classes created from Tobias Ecklebe and were used in different other projects.'
    """
    A short description of the project
    """

    version_number = __version__
    """
    The current version of the program.
    """

    author_names = "Tobias Ecklebe"
    """
    The name(s) of the project author(s)
    """

    author_emails = "tobias.ecklebe@outlook.de"
    """
    The email address(es) of the project author(s)
    """

    license_type = "GNU LGPLv3"
    """
    The project's license type
    """

    project_name = GitRepository.repository_name
    """
    The name of the project
    """

    download_master_zip = GitRepository.gitlab_url + "/repository/archive.zip?ref=master"
    """
    A URL linking to the current source zip file of the master branch.
    """


class Variables:
    """
    Variables used for distributing with setuptools to the python package index
    """

    classifiers = [

        "Natural Language :: English",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"

    ]
    """
    The list trove classifiers applicable to this project
    """

    install_requires = ["lxml", "pyqt5>=5.8.2", "markdown2", "numpy"]
    """
    Python Packaging Index dependencies
    """

    extras_require = {"gui": ["PyQt5"]}
    """
    Optional dependencies for Pypi
    """

    name = General.project_name
    """
    The name of the project on Pypi
    """

    version = General.version_number
    """
    The version of the project on pypi
    """

    description = General.project_description
    """
    The short description of the project on pypi
    """

    url = GitRepository.gitlab_url
    """
    A URL linking to the home page of the project, in this case a
    self-hosted Gitlab page
    """

    download_url = General.download_master_zip
    """
    A link to the current source zip of the project
    """

    author = General.author_names
    """
    The author(s) of this project
    """

    author_email = General.author_emails
    """
    The email adress(es) of the author(s)
    """

    license = General.license_type
    """
    The License used in this project
    """