import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    # trips["trip_date"]=pd.to_datetime(trips["trip_date"],errors="coerce")
    # trips["fuel_efficiency"]=trips["distance_km"]/trips["fuel_consumed"]

    # trips_first_half=trips[trips["trip_date"].dt.month <=6]
    # trips_first_half = trips_first_half.groupby("driver_id").agg(
    # first_half_avg_0=("fuel_efficiency", "mean"))
    # trips_first_half["first_half_avg"] = trips_first_half["first_half_avg_0"].round(2)

    # trips_second_half=trips[trips["trip_date"].dt.month >6]
    # trips_second_half = trips_second_half.groupby("driver_id").agg(
    #     second_half_avg_0=("fuel_efficiency","mean"))
    # trips_second_half["second_half_avg"] = trips_second_half["second_half_avg_0"].round(2)

    # result=trips_first_half.merge(trips_second_half,on="driver_id",how="inner").merge(drivers,on="driver_id",how="inner")
    # result["efficiency_improvement"]=round(result["second_half_avg_0"]-result["first_half_avg_0"],2)
    # result=result[result["efficiency_improvement"]>=0].sort_values(
    #     by=["efficiency_improvement","driver_name"],
    #     ascending=[False,True]
    # )
    # return result[["driver_id","driver_name","first_half_avg","second_half_avg","efficiency_improvement"]]

    # 1. Calculate individual trip efficiency and classify half-years
    trips["trip_date"] = pd.to_datetime(trips["trip_date"])
    trips["fuel_efficiency"] = trips["distance_km"] / trips["fuel_consumed"]
    
    # Map months: Jan-Jun -> H1, Jul-Dec -> H2
    trips["half"] = trips["trip_date"].dt.month.map(lambda x: "H1" if x <= 6 else "H2")
    
    # 2. Pivot to calculate means (Keep raw precision for now)
    pivot_df = trips.pivot_table(
        index="driver_id", 
        columns="half", 
        values="fuel_efficiency", 
        aggfunc="mean"
    ).dropna()
    
    # Rename columns for clarity
    pivot_df.columns = ["h1_raw", "h2_raw"]
    pivot_df = pivot_df.reset_index()
    
    # 3. CRITICAL: Calculate improvement using RAW values, then round
    # This prevents the "2.09 vs 2.1" error seen in your screenshot
    pivot_df["efficiency_improvement"] = (pivot_df["h2_raw"] - pivot_df["h1_raw"]).round(2)
    
    # 4. Round the display columns to 2 decimal places
    pivot_df["first_half_avg"] = pivot_df["h1_raw"].round(2)
    pivot_df["second_half_avg"] = pivot_df["h2_raw"].round(2)
    
    # 5. Filter for improvement > 0 and merge with driver names
    result = pivot_df[pivot_df["efficiency_improvement"] > 0].merge(drivers, on="driver_id")
    
    # 6. Final sorting: improvement (DESC), name (ASC)
    return result.sort_values(
        by=["efficiency_improvement", "driver_name"], 
        ascending=[False, True]
    )[["driver_id", "driver_name", "first_half_avg", "second_half_avg", "efficiency_improvement"]]
