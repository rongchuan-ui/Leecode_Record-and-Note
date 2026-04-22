import pandas as pd

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    customer_transactions["transaction_date"]=pd.to_datetime(customer_transactions["transaction_date"])
    customer_transactions["refund"]=(customer_transactions["transaction_type"]=="refund").astype(int)
    customer_transactions=customer_transactions.groupby("customer_id").agg(
        purchase_num=("transaction_id","count"),
        active_day_frt=("transaction_date","min"),
        active_day_lst=("transaction_date","max"),
        refund_num=("refund","sum")
    ).reset_index()
    customer_transactions["active_period"]=(customer_transactions["active_day_lst"]-customer_transactions["active_day_frt"]).dt.days
    customer_transactions["refund_rate"]=customer_transactions["refund_num"]/customer_transactions["purchase_num"]
    customer_transactions=customer_transactions[
        (customer_transactions["purchase_num"]>=3) &
        (customer_transactions["active_period"]>=30) &
        (customer_transactions["refund_rate"]<0.2)
        ][["customer_id"]].sort_values("customer_id")
    return customer_transactions
