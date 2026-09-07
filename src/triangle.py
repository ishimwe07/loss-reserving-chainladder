import pandas as pd

claimsData = pd.read_csv("data/ppauto.csv")


def initial_triangle():
    non_square_claims_data = claimsData[
        (claimsData['GRNAME'] == 'State Farm Mut Grp') &
        (claimsData['DevelopmentYear'] <= 2007)
        ]

    # Keep only the upper triangle(nonSquareClaimsData)
    triangle = non_square_claims_data.pivot_table(
        index='AccidentYear',
        columns='DevelopmentLag',
        values='CumPaidLoss',
        aggfunc='sum')

    return triangle