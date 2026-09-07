def cumulative_dev_factor(factors):
    cdfs = factors.iloc[::-1].cumprod().iloc[::-1]
    return cdfs