## Setup file for the pylibcklb package
#
# @file		    setup.py
# @author	    Tobias Ecklebe tobias.ecklebe@outlook.de
# @date		    02.11.2017
# @version	    0.1.0
# @bug          No bugs at the moment.
# @copyright    Unknown at this stage of implemantation.
#
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

exec(open('pylibcklb/version.py').read())

setup(name='pylibcklb',
      version=__version__,
      description='The libary for all functions and classes implemented in python from Tobias Ecklebe',
      long_description=readme(),
      author='Tobias Ecklebe',
      author_email='tobias.ecklebe@outlook.de',
      license='MIT',
      packages=['pylibcklb'],
      install_requires=[
            'os',
            'sys',
            'traceback',
            'abc',
            'lxml',
            'pyqt5>=5.8.2',
            'markdown2',
            'numpy',
      ],
      include_package_data=True,
      zip_safe=False)