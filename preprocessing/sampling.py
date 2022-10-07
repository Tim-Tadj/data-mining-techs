import numpy as np
import pandas as pd

def linear_resample_interp(df, period = '1min'):
    return df.resample(period).mean().interpolate('linear', limit_direction='both')

def lstm_split_sequence(sequence, n_steps_in, n_steps_out):
    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps_in
        # check if we are beyond the sequence
        if end_ix+n_steps_out > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x= sequence[i:end_ix]
        seq_y = sequence[end_ix:end_ix+n_steps_out]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)