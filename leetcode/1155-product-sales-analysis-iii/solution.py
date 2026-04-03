import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    sales_year=sales.groupby("product_id").agg(
        {"year":"min"},
    ).reset_index()
    # sales_quantity=sales.groupby(["product_id","year"]).agg(
    #     quantity=("quantity","sum"),
    # ).reset_index()
    # sales_1 = sales_year.merge(sales_quantity,on=["product_id","year"],how="inner")
    # sales_2 = sales_1.merge(sales[["product_id","price","year"]].drop_duplicates(),on=["product_id","year"],how="inner")
    # sales_2= sales_2.rename(columns={"year": "first_year"})
    # return sales_2

    sales_2 = sales_year.merge(
        sales[["product_id", "year", "quantity", "price"]].drop_duplicates(),
        on=["product_id", "year"],
        how="inner"
    )
    sales_2 = sales_2.rename(columns={"year": "first_year"})
    return sales_2
