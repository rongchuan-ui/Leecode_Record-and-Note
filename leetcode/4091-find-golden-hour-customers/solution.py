import pandas as pd

def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:
    restaurant_orders["order_timestamp"] = pd.to_datetime(restaurant_orders["order_timestamp"])
    restaurant_orders["hours"]=restaurant_orders["order_timestamp"].dt.hour
    restaurant_orders["peak_hours"]=((restaurant_orders["hours"].between(11,13)) | (restaurant_orders["hours"].between(18,20))).astype(int)
    #restaurant_orders["order_rating"]=restaurant_orders["order_rating"].fillna(0)
    restaurant_orders=restaurant_orders.groupby("customer_id").agg(
        total_orders=("order_id","count"),
        peak_hours_num=("peak_hours","sum"),
        rate_sum=("order_rating","sum"),
        rate_num=("order_rating","count")
    ).reset_index()
    restaurant_orders["peak_hour_percentage"]=round(restaurant_orders["peak_hours_num"]/restaurant_orders["total_orders"]*100,0)
    restaurant_orders["average_rating"]=round(restaurant_orders["rate_sum"]/restaurant_orders["rate_num"],2)
    restaurant_orders["rated_ratio"]=restaurant_orders["rate_num"]/restaurant_orders["total_orders"]
    restaurant_orders=restaurant_orders[
        (restaurant_orders["total_orders"]>=3) &
        (restaurant_orders["peak_hour_percentage"]>=60) &
        (restaurant_orders["average_rating"]>=4.0) &
        (restaurant_orders["rated_ratio"]>0.5)
    ][["customer_id","total_orders","peak_hour_percentage","average_rating"]].sort_values(
        by=["average_rating","customer_id"],
        ascending=[False,False]
    )
    return restaurant_orders


