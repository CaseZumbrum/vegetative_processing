import numpy as np

def GNDVI(nir: np.ndarray, green: np.ndarray) -> np.ndarray:
    if(nir + green == 0):
        return 0
    return ((nir - green) / (nir + green))