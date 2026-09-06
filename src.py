import pandas as pd

claimsData = pd.read_csv("data/ppauto.csv")

nonSquareClaimsData = claimsData[
    (claimsData['GRNAME'] == 'State Farm Mut Grp') &
    (claimsData['DevelopmentYear'] <= 2007)
]

# print(nonSquareClaimsData)
triangle = nonSquareClaimsData.pivot_table(
    index='AccidentYear',
    columns='DevelopmentLag',
    values='CumPaidLoss',
    aggfunc='sum')

print(triangle.to_string())