import pandas as pd

from src.triangle import load_data


def backtest(estimates):
    company_claims_data = load_data(None)

    data_at_developed_year = company_claims_data[(company_claims_data['DevelopmentLag'] == 10)].set_index(
        "AccidentYear")
    actual_cum_paid_loss = data_at_developed_year['CumPaidLoss']

    actual_and_estimates = pd.DataFrame({
        "Actual": actual_cum_paid_loss,
        "Estimated": estimates["Ultimate"],
    })

    actual_and_estimates["Difference"] = actual_and_estimates["Actual"] - actual_and_estimates["Estimated"]
    actual_and_estimates["ErrorPercentage"] = (actual_and_estimates["Difference"] / actual_and_estimates[
        "Actual"]) * 100

    differences_over_whole_period = actual_and_estimates["Difference"].sum()
    error_over_whole_period = (differences_over_whole_period / actual_and_estimates["Actual"].sum()) * 100

    return actual_and_estimates, differences_over_whole_period, error_over_whole_period
