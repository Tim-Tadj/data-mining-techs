import numpy as np
import pandas as pd

def linear_resample_interp(df, period = '1min'):
    return df.resample(period).mean().interpolate('linear', limit_direction='both')