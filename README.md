# data-mining-techs

## Preprocessing
Stores techniques for preprocessing data

### Filtering
Preset custom filters

#### quantile_derivative_autothresh
Takes nth order gradient of the quantiles of input array and automatically determines abnormal quantiles. Good for filtering saturated recordings from sensors.

Quantiles may have variable len sampling

#### quantile_minmax_autothresh
Uses quantile_derivative_autothresh and finds the min and max threshold based on abnormal quantiles