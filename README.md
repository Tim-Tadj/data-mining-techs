# data-mining-techs

## Preprocessing
Stores techniques for preprocessing data

### Filtering
Preset custom filters
```python
def quantile_derivative_autothresh(array:np.ndarray, ord:int, n_points=100)
```
Takes nth order gradient of the quantiles of input array and automatically determines abnormal quantiles. Good for filtering saturated recordings from sensors.

Quantiles may have variable len sampling

```python
def quantile_minmax_autothresh(array:np.ndarray, ord:int, n_points=100)
```
Uses quantile_derivative_autothresh and finds the min and max threshold based on abnormal quantiles
