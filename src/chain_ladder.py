import pandas as pd

NO_TAIL_FACTOR = 1.0


def chain_ladder(triangle, cdfs):
    result = []
    for year, row in triangle.iterrows():
        latest_lag = row.last_valid_index()
        latest = row[latest_lag]

        cdf = cdfs.get(latest_lag, NO_TAIL_FACTOR)

        ultimate = latest * cdf
        reserve = ultimate - latest

        result.append({
            "Year": year,
            "Latest": latest,
            "CDF": cdf,
            "Ultimate": ultimate,
            "Reserve": reserve
        })

    final_estimates_per_year = pd.DataFrame(result).set_index("Year")
    total_reserve = final_estimates_per_year["Reserve"].sum()

    return final_estimates_per_year, total_reserve
