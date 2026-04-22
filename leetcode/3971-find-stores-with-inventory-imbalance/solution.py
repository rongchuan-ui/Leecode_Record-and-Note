import pandas as pd

def find_inventory_imbalance(stores: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    # # Only include stores that have at least 3 different products
    # store_more_3=inventory.groupby("store_id").agg(
    #     inventory_num=("inventory_id","nunique")
    # ).reset_index()
    # store_more_3=store_more_3[store_more_3["inventory_num"]>=3]
    # inventory=inventory[inventory["store_id"].isin(store_more_3["store_id"])]

    # #identify the most expensive product and cheapest product 
    # inventory=inventory.sort_values(by=["store_id","price"])
    # inventory_cheap= inventory.groupby("store_id").head(1).reset_index().rename(columns={
    #     'product_name': 'cheapest_product', 
    #     'quantity': 'cheap_qty'
    # })
    # inventory_expensive= inventory.groupby("store_id").tail(1).reset_index().rename(columns={
    #     'product_name': 'most_exp_product', 
    #     'quantity': 'expensive_qty'
    # })
    # inventory=inventory_expensive.merge(inventory_cheap, on="store_id",how="inner")

    # # inventory imbalance and imbalance ratio
    # inventory_imbalance=inventory[inventory["expensive_qty"]<inventory["cheap_qty"]]
    # inventory_imbalance["imbalance_ratio"]=round(inventory["cheap_qty"]/inventory["expensive_qty"],2)
    # result=inventory_imbalance.merge(stores, on="store_id",how="inner")[["store_id","store_name","location","most_exp_product","cheapest_product","imbalance_ratio"]].sort_values(
    #     by=["imbalance_ratio","store_name"],
    #     ascending=[False,True]
    # )
    # return result


    # 1. Filter: Keep only stores with at least 3 unique products
    # Using transform is generally faster than groupby.filter for large datasets
    inventory['product_count'] = inventory.groupby('store_id')['inventory_id'].transform('nunique')
    inventory = inventory[inventory['product_count'] >= 3]
    
    # 2. Sort once by price to easily pick min and max
    inventory = inventory.sort_values(['store_id', 'price'])
    
    # 3. Get cheapest (first row of each group)
    cheapest = inventory.drop_duplicates('store_id', keep='first').rename(
        columns={'product_name': 'cheapest_product', 'quantity': 'cheap_qty'}
    )
    
    # 4. Get most expensive (last row of each group)
    expensive = inventory.drop_duplicates('store_id', keep='last').rename(
        columns={'product_name': 'most_exp_product', 'quantity': 'expensive_qty'}
    )
    
    # 5. Merge the min/max data
    combined = pd.merge(cheapest, expensive, on='store_id')
    
    # 6. Apply condition: expensive quantity < cheap quantity
    combined = combined[combined['expensive_qty'] < combined['cheap_qty']].copy()
    
    # 7. Calculate ratio
    combined['imbalance_ratio'] = (combined['cheap_qty'] / combined['expensive_qty']).round(2)
    
    # 8. Final merge with stores table and sort
    result = combined.merge(stores, on='store_id')
    
    return result[[
        'store_id', 'store_name', 'location', 
        'most_exp_product', 'cheapest_product', 'imbalance_ratio'
    ]].sort_values(['imbalance_ratio', 'store_name'], ascending=[False, True])
