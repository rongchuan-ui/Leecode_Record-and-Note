import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    # first select user who paid 
    df1 = user_activity.groupby("user_id").agg({
        "activity_type":list})
    df1=df1[
        df1["activity_type"].apply(lambda x: "free_trial" in x and "paid" in x)
    ]

    # second filter user in original table
    user_activity = user_activity[
        user_activity["user_id"].isin(df1.index)]
    
    # calculate and form table
    user_activity_free= user_activity[
        user_activity["activity_type"] == "free_trial"
    ]
    user_activity_free = user_activity_free.groupby("user_id").agg({
        "activity_duration":"mean"}).round(2).rename(columns={"activity_duration":"trial_avg_duration"}).reset_index()
    # user_activity_free["trial_avg_duration"] = (np.trunc(user_activity_free["trial_avg_duration"] * 100) / 100)
    
    user_activity_paid= user_activity[
        user_activity["activity_type"] == "paid"
    ]
    user_activity_paid = user_activity_paid.groupby("user_id").agg({
        "activity_duration":"mean"}).round(2).rename(columns={"activity_duration":"paid_avg_duration"}).reset_index()
    #user_activity_paid["paid_avg_duration"] = ( np.trunc(user_activity_paid["paid_avg_duration"] * 100) / 100)
    
    df=user_activity_free.merge(user_activity_paid,on="user_id",how="inner")
    return df    

# other way
import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    df = (
        user_activity.groupby(["user_id", "activity_type"])["activity_duration"]
        .mean()
        .unstack()
        .reset_index()
    )

    df = df[
        df["free_trial"].notna() & df["paid"].notna()
    ]

    df = df.rename(columns={
        "free_trial": "trial_avg_duration",
        "paid": "paid_avg_duration"
    })

    return df[["user_id", "trial_avg_duration", "paid_avg_duration"]]
