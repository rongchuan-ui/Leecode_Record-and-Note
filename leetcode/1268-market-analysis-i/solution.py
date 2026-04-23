import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    #users["join_date"]=pd.to_datetime(users["join_date"])
    orders["order_date"]=pd.to_datetime(orders["order_date"])
    orders["year"]=orders["order_date"].dt.year
    orders=orders[orders["year"]==2019]
    orders=orders.groupby("buyer_id").agg(
        orders_in_2019=("order_id","count")
    ).reset_index()

    order_user=users.merge(orders, left_on="user_id", right_on="buyer_id", how="left")
    order_user["orders_in_2019"]=order_user["orders_in_2019"].fillna(0)
    return order_user[["user_id", "join_date", "orders_in_2019"]].rename(columns={"user_id": "buyer_id"})
    

    # # 1. 准备订单数据：转换日期并只看 2019 年
    # orders["order_date"] = pd.to_datetime(orders["order_date"])
    # orders_2019 = orders[orders["order_date"].dt.year == 2019]
    
    # # 2. 统计每个买家的订单数
    # # reset_index(name="...") 直接给统计结果列起好名字
    # counts = orders_2019.groupby("buyer_id").size().reset_index(name="orders_in_2019")
    
    # # 3. 核心修正：使用 LEFT Join 合并 users 表
    # # 确保没有买过东西的用户（3和4）也能留下来
    # res = users.merge(counts, left_on="user_id", right_on="buyer_id", how="left")
    
    # # 4. 把那些没有订单的 NaN 变成 0
    # res["orders_in_2019"] = res["orders_in_2019"].fillna(0)
    
    # # 5. 按照题目要求的列名返回
    # return res[["user_id", "join_date", "orders_in_2019"]].rename(columns={"user_id": "buyer_id"})
    
