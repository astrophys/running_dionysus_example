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
from gaussian_kde import kernel_density_estimator
from error import exit_with_error
from functions import read_matlab_int_file
from functions import output_array_as_matlab_int
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



def main():
    """
    ARGS:
    RETURN:
    DESCRIPTION:
    DEBUG:
        1. Compared my computation of smoothM to that given by R's TDA::kde(). Running in
           ~/Code/R/das_rtda/src/biofilm_tda_analysis.R:415, I print out the same sized
           smoothed array... 

            From R:
                Browse[2]> xseq = seq(1,3); yseq=seq(1,5); zseq=seq(1,4);
                Browse[2]> grid2 = expand.grid(xseq,yseq,zseq)
                Browse[2]> colnames(grid2) <- c("x","y","z")
                Browse[2]> grid2$val = kde(dataM, grid2, h)
                Browse[2]> grid2
            
            Comparing it to the debug section below, the outputs are IDENTICAL.  I can
            safely conclude that my computation of the smoothed data is correct.
            Also that my gaussian_kde.py (copied from das_rtda) is also correct.

           
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
    #print("{} \n".format(sys.argv),flush=True)
    print("Start Time : {}\n".format(time.strftime("%a, %d %b %Y %H:%M:%S ",
                                       time.localtime())),flush=True)
    # Error check
    if(re.search("matlab_int.txt$", inFile) == None):
        exit_with_error("ERROR!! {} is not a matlab_int.txt file\n".format(inFile))
    else:
        dataM = read_matlab_int_file(InputPath = inFile)  # It isn't a matrix, but still
    ## Put all the elements into a list
    dim = dataM.shape
    smoothM = np.zeros(dim)
    thresh = 1          # Do otsu thresholding here
    dataL = []          # a list of points where voxel is > thresh

    # Get list of points to pass to kernel_density_estimator
    for i in range(dim[0]):
        for j in range(dim[1]):
            for k in range(dim[2]):
                if(dataM[i,j,k] >= thresh):
                    dataL.append([i,j,k])
    # Now compute smoothed data
    h = 1
    for i in range(dim[0]):
        for j in range(dim[1]):
            for k in range(dim[2]):
                smoothM[i,j,k] = kernel_density_estimator(DataL=dataL, X=i, Y=j, Z=k, H=h)
    
    # Debug - compare to kde() from TDA package, recall R is 1 indexed 
    for k in range(dim[2]):
        for j in range(dim[1]):
            for i in range(dim[0]):
                print("{} {} {} {:0.10f}".format(i+1,j+1,k+1,smoothM[i,j,k]))

    smoothOutName = "smooth_{}".format(inFile.split("/")[-1])
    output_array_as_matlab_int(Array=smoothM, OutName=smoothOutName)
    print("\n\nEnded : %s"%(time.strftime("%D:%H:%M:%S")))
    print("Run Time : {:.4f} h".format((time.time() - startTime)/3600.0))
    sys.exit(0)


if __name__ == "__main__":
    main()
