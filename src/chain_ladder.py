import pandas as pd

def chain_ladder(triangle, cdfs):
    reserve = {}

    for year, row in triangle.iterrows():

        ultimate_lag = row.last_valid_index()

        if ultimate_lag == len(row):
            ultimate = row[ultimate_lag]
            reserve[year] = ultimate - row[ultimate_lag]
            continue

        ultimate = row[ultimate_lag] * cdfs[ultimate_lag]
        reserve[year] = ultimate - row[ultimate_lag]

    print(pd.Series(reserve))
    return reserve
