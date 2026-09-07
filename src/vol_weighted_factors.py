import pandas as pd

def vol_weighted_factors(triangle):
    factors = {}
    lags = triangle.columns

    for earlier, later in zip(lags[:-1], lags[1:]):
        rows_with_values = triangle[triangle[[earlier, later]].notna().all(axis=1)]

        columns_sum = rows_with_values[[earlier, later]].sum()
        new_factor = columns_sum[later] / columns_sum[earlier]
        factors[earlier] = new_factor

    return pd.Series(factors)
