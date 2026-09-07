import pandas as pd


def chain_ladder(triangle, cdfs):
    result = []
    for year, row in triangle.iterrows():
        ultimate_lag = row.last_valid_index()
        latest = row[ultimate_lag]

        cdf = cdfs.get(ultimate_lag, 1.0)

        ultimate = latest * cdf
        reserve = ultimate - row[ultimate_lag]

        result.append({
            "Year": year,
            "CDF": cdf,
            "Latest": latest,
            "Ultimate": ultimate,
            "Reserve": reserve
        })

    final_estimates_per_year = pd.DataFrame(result).set_index("Year")
    total_reserve = final_estimates_per_year["Reserve"].sum()

    return final_estimates_per_year, total_reserve
