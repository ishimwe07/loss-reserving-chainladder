import chainladder as cl

from src.chain_ladder import chain_ladder
from src.cumulative_dev_factors import cumulative_dev_factors
from src.triangle import initial_triangle, load_data
from src.vol_weighted_factors import vol_weighted_factors

COMPANY = "State Farm Mut Grp"
VALUATION_YEAR = 2007
DATA_PATH = "data/ppauto.csv"


def test_matches_library():
    data = load_data()
    triangle = initial_triangle()
    ldfs = vol_weighted_factors(triangle)
    cdfs = cumulative_dev_factors(ldfs)

    mine, my_predicted_total_reserve = chain_ladder(triangle, cdfs)

    cl_triangle = cl.Triangle(
        data,
        origin='AccidentYear',
        development='DevelopmentYear',
        columns=['CumPaidLoss'],
        cumulative=True
    )

    model = cl.Development().fit_transform(cl_triangle)
    ultimates_from_actual_cl_library = cl.Chainladder().fit(model).ultimate_
    their_values = ultimates_from_actual_cl_library.values.flatten()

    assert abs(mine["Ultimate"].values - their_values).max() == 0
