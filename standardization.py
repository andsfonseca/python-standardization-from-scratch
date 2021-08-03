import numpy as np

def Standardization(data, n_features,axis = 0):
    """
    Performs a data standardization 
    
    Parameters:
    data (np.array): Dataset
    n_features (int): Number of features.
    axis (int): Direction
  
    Returns:
    np.array: Standardized data
    """
    X = data.copy()
    
    #Mean subtraction 
    mean = np.mean(X, axis = axis)
    for i in range(n_features):
        X[:,i] -= mean[i]
        
    # Normalize the Variance
    std = np.std(X, axis =axis)
    for i in range(n_features):
        X[:,i] /= std[i]
    
    return X