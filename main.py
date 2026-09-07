import pandas as pd
from src.triangle import initial_triangle
from src.vol_weighted_factors import vol_weighted_factors
from src.cumulative_dev_factors import cumulative_dev_factors
from src.chain_ladder import chain_ladder

pd.set_option("display.float_format", "{:,.2f}".format)


def main():
    triangle = initial_triangle()
    ldfs = vol_weighted_factors(triangle)
    cdfs = cumulative_dev_factors(ldfs)

    table, total = chain_ladder(triangle, cdfs)
    print(table)
    print(f"\nTotal reserve: {total:,.0f}")

    return table, total


if __name__ == "__main__":
    main()
