import pandas as pd

COMPANY = "State Farm Mut Grp"
VALUATION_YEAR = 2007
DATA_PATH = "data/ppauto.csv"


def load_data(valuation_year=VALUATION_YEAR):
    claims_data = pd.read_csv(DATA_PATH, dtype={"CumPaidLoss": float})
    company_claims = claims_data[claims_data['GRNAME'] == COMPANY]

    if valuation_year is not None:
        company_claims = company_claims[
            company_claims['DevelopmentYear'] <= valuation_year]

    return company_claims


def initial_triangle():
    company_claims = load_data()

    triangle = company_claims.pivot_table(
        index='AccidentYear',
        columns='DevelopmentLag',
        values='CumPaidLoss',
        aggfunc='sum')

    return triangle
