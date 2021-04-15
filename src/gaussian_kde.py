from error import exit_with_error
import numpy as np
def kernel_density_estimator(DataL=None, X=None, Y=None, Z=None, H=None):
    """
    ARGS:
        DataL = List of data, assume unit value
        X,Y,Z = X,Y,Z position to compute pdf from DataL. Z is optional
        H     = the 'width' of the kernel
    DESCRIPTION:
    RETURN:
    DEBUG:
    FUTURE:
    """
    prob = 0
    n = len(DataL)
    h = H

    # Sum exponential part
    for i in range(n):
        muL= DataL[i]       # List of position of gaussian center
        if(Z == None):
            posL = [X,Y]        # Point of interest
        else:
            posL = [X,Y,Z]
        p = gaussian_pdf(PosL=posL, MuL=muL, Sigma=H)

        # d2= (Data[i,1] - X)**2 + (Data[i,2] - Y)**2 + (Data[i,3] - Z)**2
        # p = gaussian_pdf(D=d2**0.5, NDim=ndim, Sigma=H)
        # p = exp(-d2 / (2*h**2))

        prob = prob + p

    # Divide by number of samples, see 1/n factor above
    prob = prob / n
    return(prob)


def gaussian_pdf(PosL, MuL, Sigma):
    """
    ARGS:
        PosL = List, [float, float], X and Y positions
        MuL  = List, [float, float]
        Sigma= Standard deviation of gaussian function
    DESCRIPTION:
        Computes Gaussian pdf
    RETURN:
    DEBUG:
        1. Compared to wolfram alpha
            PDF(NormalDistribution[0,0.4472136], 0.5) = 0.4774864
           --> IDENTICAL
    FUTURE:
        1. Use numpy's np.random.normal
    """
    xDim  = len(PosL)
    muDim = len(MuL)
    if(xDim != muDim):
        exit_with_error("ERROR!!! xDim ({}) != muDim ({})\n".format(xDim, muDim))
    else:
        nDim = xDim

    d = 0
    for i in range(nDim):
        d = d + (PosL[i] - MuL[i])**2

    prob = np.exp(-d / (2*Sigma**2)) / (np.sqrt(2*np.pi*Sigma**2)**nDim)
    #print("{}    PosL : {},  MuL : {}, Sigma : {}".format(prob, PosL, MuL, Sigma))
    return(prob)

def main():
    """
    ARGS:
        None.
    DESCRIPTION:
    RETURN:
    DEBUG:
    FUTURE:
        1. Check that bcFile is actually a barcode file
        2. Vectorize operations
    """
    print(gaussian_pdf([0.5],[0],0.4472136))
    dataL = [[1,1],[2,2],[3,3],[5,10]]
    print(kernel_density_estimator(DataL=dataL, X=0, Y=1, H=1))
    
    print("hello")

if __name__ == "__main__":
    main()
