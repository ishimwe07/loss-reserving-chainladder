from src.triangle import initial_triangle
from src.vol_weighted_factor import volume_weighted_factors
from src.cumulative_dev_factors import cumulative_dev_factor
from src.chain_ladder import chain_ladder
import pandas as pd

pd.set_option("display.float_format", "{:,.2f}".format)


def main():
    triangle = initial_triangle()
    ldfs = volume_weighted_factors(triangle)
    cdfs = cumulative_dev_factor(ldfs)

    table, total = chain_ladder(triangle, cdfs)
    print(table)
    print(f"\nTotal reserve: {total:,.0f}")

    return table, total


if __name__ == "__main__":
    main()
