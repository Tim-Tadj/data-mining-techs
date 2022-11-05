import numpy as np

def even_fit_y(y, deg=1):
    x = np.arange(len(df), dtype=float)
    consts = np.polyfit(x=x, y=y, deg=deg)
    ynew = np.zeros_like(x, dtype=float)
    for i, c in enumerate(consts):
        a =len(consts)-(i+1)
        ynew += c * x**a
    return ynew