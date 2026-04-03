import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer_new = customer.groupby("customer_id").agg(
        product_num = ("product_key","nunique")
    ).reset_index()
    customer_new=customer_new[customer_new["product_num"] == len(product["product_key"])]
    return customer_new[["customer_id"]]
    
