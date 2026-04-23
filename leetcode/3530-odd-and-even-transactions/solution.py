import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["odd_num"]=transactions["amount"].where(transactions["amount"]%2 !=0,0)
    transactions["even_num"]=transactions["amount"].where(transactions["amount"]%2==0,0)
    transactions=transactions.groupby("transaction_date").agg(
        odd_sum=("odd_num","sum"),
        even_sum=("even_num","sum"),
    ).reset_index().sort_values("transaction_date")
    return transactions
