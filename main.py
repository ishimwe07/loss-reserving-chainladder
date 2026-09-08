import pandas as pd
from src.triangle import initial_triangle
from src.vol_weighted_factors import vol_weighted_factors
from src.cumulative_dev_factors import cumulative_dev_factors
from src.chain_ladder import chain_ladder
from src.backtest import backtest
from src.plots import plot_development_factors

pd.set_option("display.float_format", "{:,.2f}".format)


def main():
    triangle = initial_triangle()
    ldfs = vol_weighted_factors(triangle)
    cdfs = cumulative_dev_factors(ldfs)

    table, total = chain_ladder(triangle, cdfs)
    print(table)
    print(f"\nTotal reserve: {total:,.0f}")

    actual_and_estimates, differences_over_whole_period, error_over_whole_period = backtest(table)

    print(f"\nThis table compare estimates and actual amounts paid\n", actual_and_estimates)
    print(f"\nThis is the Differences over whole period", differences_over_whole_period)
    print(f"\nThis is the Error over whole period", error_over_whole_period)

    plot_development_factors(ldfs, "outputs/development_factors.png")

    return table, total


if __name__ == "__main__":
    main()
