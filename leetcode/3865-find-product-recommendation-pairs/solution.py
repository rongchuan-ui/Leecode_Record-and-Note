import pandas as pd
from itertools import combinations

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    # Find the conbination of products
    product_combo =product_purchases.groupby("user_id").agg({
        "product_id":lambda x: tuple(sorted(set(x)))
    }).reset_index()
    # combine pairs with product1_id < product2_id
    product_combo["product_id"]=product_combo["product_id"].apply(lambda x: list(combinations(x,2)))
    product_combo=product_combo.explode("product_id")
    #calculate and filter the customer number
    customer_number=product_combo.groupby("product_id").agg({
        "user_id":"count"
    }).rename(columns={"user_id":"customer_count"}).reset_index()
    customer_number_gt3=customer_number[
        customer_number["customer_count"]>=3]
    # seperate each pair
    customer_number_gt3[["product1_id","product2_id"]]=pd.DataFrame(customer_number_gt3["product_id"].tolist(), index=customer_number_gt3.index)
    customer_number_gt3=customer_number_gt3.drop(columns="product_id")
    # merge two table
    customer_number_gt3_1=customer_number_gt3.merge(product_info[["product_id","category"]], left_on="product1_id",right_on="product_id",how="inner").rename(columns={"category": "product1_category"})
    customer_number_gt3_2=customer_number_gt3_1.merge(product_info[["product_id","category"]], left_on="product2_id",right_on="product_id",how="inner").rename(columns={"category": "product2_category"})
    customer_number_gt3_2=customer_number_gt3_2.drop(columns=["product_id_x","product_id_y"])
    # adjust format
    col="customer_count"
    customer_number_gt3_2=customer_number_gt3_2[[c for c in customer_number_gt3_2.columns if c != col]+[col]]
    customer_number_gt3_2 = customer_number_gt3_2.sort_values(
    by=["customer_count", "product1_id", "product2_id"],
    ascending=[False, True, True]
)
    return customer_number_gt3_2


    # df = product_purchases.merge(product_purchases, on="user_id")
    # df = df[df["product_id_x"] < df["product_id_y"]]
    # df = df.rename(columns={
    #     "product_id_x": "product1_id",
    #     "product_id_y": "product2_id"
    # })
    # df = df.sort_values(
    #     by=["user_id", "product1_id", "product2_id"]
    # ).reset_index(drop=True)
    # df = df.groupby(["product1_id", "product2_id"]).agg(
    #         customer_count=("user_id", "nunique")
    #     ).reset_index()
    # df = df[df["customer_count"] >= 3]
    # df = df.merge(
    #     product_info.rename(columns={
    #         "product_id": "product1_id",
    #         "category": "product1_category"
    #     }),
    #     on="product1_id",
    #     how="left"
    # )
    # df = df.merge(
    #     product_info.rename(columns={
    #         "product_id": "product2_id",
    #         "category": "product2_category"
    #     }),
    #     on="product2_id",
    #     how="left"
    # )
    # df = df.sort_values(
    #     by=["customer_count", "product1_id", "product2_id"],
    #     ascending=[False, True, True]
    # ).reset_index(drop=True)

    # return df[[
    #     "product1_id",
    #     "product2_id",
    #     "product1_category",
    #     "product2_category",
    #     "customer_count"
    # ]]


