# Author : Ali Snedden
# Date   : 4/12/21
# License: MIT
# Purpose: 
#   This file takes matlab_int.txt files and converts them to the Perseus file format
#   
# Notes : 
#  
#  
# Future : 
#   
#
# References : 
#   1. http://people.maths.ox.ac.uk/nanda/perseus/index.html
#
import time
import numpy as np
import sys
import re
from error import exit_with_error
from functions import read_matlab_int_file
from datetime import datetime


def print_help(ExitCode):
    """
    ARGS:
        ExitCode : int, code to exit with
    RETURN:
    DESCRIPTION:
    DEBUG:
    FUTURE:
    """
    sys.stderr.write("python3 ./src/matlabint2perseus.py input_matlab_int.txt\n"
                     "      input_matlab_int.txt : input data file\n"
                     "   \n")
    sys.exit(ExitCode)



def tmp(ExitCode):
    """
    ARGS:
    RETURN:
    DESCRIPTION:
    DEBUG:
    FUTURE:
    """


def main():
    """
    ARGS:
    RETURN:
    DESCRIPTION:
    DEBUG:
    FUTURE:
    """
    # Check Python version
    nArg = len(sys.argv)
    ## Get options 
    if(nArg != 2):
        print_help(1)
    elif(nArg == 2 and "-h" in sys.argv[1]):
        print_help(0)
    inFile = sys.argv[1]

    startTime = time.time()
    print("{} \n".format(sys.argv),flush=True)
    print("   Start Time : {}".format(time.strftime("%a, %d %b %Y %H:%M:%S ",
                                       time.localtime())),flush=True)
    # Error check
    if(re.search("matlab_int.txt$", inFile) == None):
        exit_with_error("ERROR!! {} is not a matlab_int.txt file\n".format(inFile))
    else:
        dataM = read_matlab_int_file(InputPath = inFile)
    
    


    print("\n\nEnded : %s"%(time.strftime("%D:%H:%M:%S")))
    print("Run Time : {:.4f} h".format((time.time() - startTime)/3600.0))
    sys.exit(0)


if __name__ == "__main__":
    main()
