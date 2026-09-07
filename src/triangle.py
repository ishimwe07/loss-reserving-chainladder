import pandas as pd

COMPANY = "State Farm Mut Grp"
VALUATION_YEAR = 2007
DATA_PATH = "data/ppauto.csv"


def load_data():
    claims_data = pd.read_csv(DATA_PATH)

    # Restrict to one company, as at the 2007 valuation year
    company_claims = claims_data[
        (claims_data['GRNAME'] == COMPANY) &
        (claims_data['DevelopmentYear'] <= VALUATION_YEAR)]

    return company_claims


def initial_triangle():
    claims_data = pd.read_csv(DATA_PATH)

    company_claims = load_data()

    triangle = company_claims.pivot_table(
        index='AccidentYear',
        columns='DevelopmentLag',
        values='CumPaidLoss',
        aggfunc='sum')

    return triangle
