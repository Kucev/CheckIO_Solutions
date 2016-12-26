import numpy as np
def checkio(a):
    return np.array_equal(-np.array(a),np.array(a).transpose())
