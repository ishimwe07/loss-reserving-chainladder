def cumulative_dev_factor(factors):
    cdfs = factors.iloc[::-1].cumprod().isloc[::-1]
    return cdfs