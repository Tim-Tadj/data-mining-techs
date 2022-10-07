import numpy as np

def quantile_derivative_autothresh(array:np.ndarray, ord:int, n_points=100):

    if len(array.shape) != 1:
        print("ERR: array must be 1d")
        return
    if ord < 0:
        print("ERR: ord gradient must  be >= 0")
        return
    if n_points < 2:
        print("ERR must have at least 2 quantiles")

    spikes =[]
    quantiles = np.arange(0, 1, 1/n_points)
    quant = np.quantile(data, quantiles)
    quant_grad = quant

    for i in range(0, ord):
        quant_grad = np.gradient(quant_grad)
    
    thresh = quant_grad.std()
    
    for i in range(len(quant_grad)):
        if abs(quant_grad[i]) > thresh:
            spikes.append(i)

    return np.array(spikes)

def quantile_minmax_autothresh(array:np.ndarray, ord:int, n_points=100):
    spikes = quantile_derivative_autothresh(array, ord, n_points=n_points)
    min_thresh = spikes[spikes < n_points/2].max()
    max_thresh = spikes[spikes > n_points/2].min()

    return min_thresh, max_thresh
    

