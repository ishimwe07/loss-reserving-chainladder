import pandas as pd

COMPANY = 'State Farm Mut Grp'
VALUATION_YEAR = 2007
DATA_PATH = "data/ppauto.csv"

def initial_triangle():
    claims_data = pd.read_csv(DATA_PATH)

    # Restrict to one company, as at the 2007 valuation date
    non_square_claims_data = claims_data[
        (claims_data['GRNAME'] == COMPANY) &
        (claims_data['DevelopmentYear'] <= VALUATION_YEAR)
        ]

    triangle = non_square_claims_data.pivot_table(
        index='AccidentYear',
        columns='DevelopmentLag',
        values='CumPaidLoss',
        aggfunc='sum')

    return triangle
