def cumulative_dev_factors(factors):
    cdfs = factors.iloc[::-1].cumprod().iloc[::-1]
    return cdfs