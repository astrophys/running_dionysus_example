# Author : Ali Snedden
# Date   : 4/12/21
# License: MIT
# Purpose: 
#   This file takes matlab_int.txt files and converts them to the Perseus file format
#   
# Notes : 
#  
#  
# Future:
#   
#
# References : 
#   1. http://people.maths.ox.ac.uk/nanda/perseus/index.html
#
import time
import numpy as np

def read_matlab_int_file(InputPath = None):
    """
    ARGS:
        InputPath   :   Input File name

    DESCRIPTION:
        Return a density array.
        Data formatted as : Dx = Dcolumns
                            Dy = Drows
                            Dz = every Ddim[1] rows
        NOTE: This is _NOT_ scaled by the 'z-axis'
        NOTE: I'm using a _different_ file format when compared to das_zdim_by_4.py!

    RETURN:
        dataM   :  unmodified raw data array from a matlab_int.txt file

    DEBUG:
        1. a) Output scaled [0, 255] value density_array (not scaling by z-axis!)
              from JD01_B_comE_16hr.lsm-Ch2-C1matlab_int.txt
           b) Output of Ray's JD01_B_comE_16hr.lsm-Ch2-C1float.vtk
           c) The output's were _identical_ (compared with diff)
           ---> I am correctly scaling the input data _and_ getting the x-y-z
                format correct!

        2. a) Output unscaled value density_array (not scaling by z-axis!)
              from JD01_B_comE_16hr.lsm-Ch2-C1matlab_int.txt
           b) Compared output to original file. Were IDENTICAL.
           ---> I am correctly reading in the original data file.

        CONCLUSION : output_array_as_matlab_int(),scale_array()
                     and read_matlab_int_file() must all be working
                     correctly, otherwise I would not have been able to
                     get the correct output.

    FUTURE:
    """
    print("Reading matlab txt file....")
    print("     Start : %s"%(time.strftime("%D:%H:%M:%S")))
    fname = InputPath if InputPath is not None else exit_with_error("ERROR in InputPath!\n")
    fin = open(fname, "r")
    (i,j,k) = (0,0,0)       # x index for density_array
    lidx = 0                # Line index
    ##### Input data #####
    # Read-in file as y on rows, x on cols, z every 512 rows.
    for line in fin:
        # Read Metadata - first 2 lines
        if(lidx==0):
            name = line
            lidx += 1
        elif(lidx==1):
            lidx += 1
            # dimensions
            dim  = line.split()
            for d in range(0,len(dim)):     # Convert to list of 3 ints
                dim[d] = int(dim[d])
            if(len(dim) != 3):
                exit_with_error("ERROR! dim is NOT 3-dimensional. Inspect 2nd line of data file")
            else :
                dataM = np.zeros([dim[0],dim[1],dim[2]], dtype=np.int64)
        else :
            line = line.split()
            # Read data
            for val in line:
                dataM[i,j,k]   = int(val)
                i += 1
                # Reset
                if(i == dim[0]):
                    i = 0
            j += 1
            # Reset j
            if(j == dim[1]):
                j = 0
                k += 1
    if(k != dim[2]):
        exit_with_error("ERROR!! k = %i, dim[2] = %i.  Should be equal\n"%(k,dim[2]))
    fin.close()
    print("     End : %s"%(time.strftime("%D:%H:%M:%S")))
    return dataM
