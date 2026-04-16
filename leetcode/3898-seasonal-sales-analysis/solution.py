import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales["Month"]=sales["sale_date"].dt.month_name()
    sales["Revenue"]=sales["quantity"]*sales["price"]
    df=sales.groupby(["Month","product_id"]).agg(
        total_quantity=("quantity","sum"),
        total_revenue=("Revenue","sum")
    ).reset_index()
    season_map={
        "December":"Winter",
        "January":"Winter",
        "February":"Winter",
        "March":"Spring",
        "April":"Spring",
        "May":"Spring",
        "June":"Summer",
        "July":"Summer",
        "August":"Summer",
        "September":"Fall",
        "October":"Fall",
        "November":"Fall"
    }
    df["season"]=df["Month"].map(season_map)
    df1=df.merge(products,on="product_id",how="left")
    df1=df1.groupby(["season","category"]).agg({
        "total_quantity":"sum",
        "total_revenue":"sum"
    }).sort_values(
        by=["total_quantity","total_revenue"],
        ascending=[False,False]
    ).reset_index()
    df1=df1.groupby("season").head(1).sort_values("season")
    return df1

    # # 1. Merge tables first and calculate total revenue per sale
    # df = sales.merge(products, on='product_id')
    # df['total_revenue'] = df['quantity'] * df['price']
    
    # # 2. Vectorized Season Mapping (Fastest method)
    # # Using month numbers (1-12) is much faster than using month names (strings)
    # month = pd.to_datetime(df['sale_date']).dt.month
    
    # season_map = {
    #     12: 'Winter', 1: 'Winter', 2: 'Winter',
    #     3: 'Spring', 4: 'Spring', 5: 'Spring',
    #     6: 'Summer', 7: 'Summer', 8: 'Summer',
    #     9: 'Fall', 10: 'Fall', 11: 'Fall'
    # }
    # df['season'] = month.map(season_map)
    
    # # 3. Perform a single aggregation by Season and Category
    # # as_index=False keeps the dataframe flat and avoids extra .reset_index() calls
    # stats = df.groupby(['season', 'category'], as_index=False).agg(
    #     total_quantity=('quantity', 'sum'),
    #     total_revenue=('total_revenue', 'sum')
    # )
    
    # # 4. Sorting logic based on problem requirements:
    # # Priority: 1. Season (ASC), 2. Quantity (DESC), 3. Revenue (DESC), 4. Category (ASC)
    # stats = stats.sort_values(
    #     by=['season', 'total_quantity', 'total_revenue', 'category'],
    #     ascending=[True, False, False, True]
    # )
    
    # # 5. Select the top (most popular) category for each season
    # # head(1) after sorting is highly efficient for "Top 1 per group" problems
    # return stats.groupby('season').head(1).sort_values('season')
