## Function library file for my math functions
#
# @file		    math_functions.py
# @author	    Tobias Ecklebe tobias.ecklebe@outlook.de
# @date		    05.11.2017
# @version	    0.1.0
# @note		    This file includes functions as libary that i think are great for different projects.\n\n
#               To use this file:  from pylibcklb import math_functions as MFL\n
#               To use a function: MFL.SomeFuction()\n\n        
#
# @pre          The library was developed with python 3.6 
#
# @bug          No bugs at the moment.
#
# @warning      No warnings at the moment
#
# @copyright    Unknown at this stage of implemantation.
#
import numpy as np

## Documentation for a method to get an normal random number
# @note https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.normal.html
# @param loc  Mean (“centre”) of the distribution.
# @param scale Standard deviation (spread or “width”) of the distribution.
# @param size   Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn. If size is None (default), a single value is returned if loc and 
#               scale are both scalars. Otherwise, np.broadcast(loc, scale).size samples are drawn.
# @return Drawn samples from the parameterized normal distribution.
def GetNormalRandomNumber(loc=0.0, scale=1.0, size=None):
    return np.random.normal(loc, scale, size)

