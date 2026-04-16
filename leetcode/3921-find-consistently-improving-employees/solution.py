import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
#     #first: filter out employees with less than 3 review
#     df_mask=performance_reviews.groupby('employee_id').agg({
#         "review_date":"nunique"}
#     )
#     df_mask=df_mask[df_mask["review_date"]>=3]
#     performance_reviews=performance_reviews[performance_reviews['employee_id'].isin(df_mask.index)]
    
#     performance_reviews=performance_reviews.sort_values(
#     by=["employee_id","review_date"],
#     ascending=[True,False]
#     )
#     performance_reviews=performance_reviews.groupby("employee_id").head(3)
#     performance_reviews = performance_reviews.rename(columns={"rating":"rating_lag_0"})
#     for i in range(1,3):
#         performance_reviews[f"rating_lag_{i}"]=performance_reviews.groupby("employee_id")[f"rating_lag_{i-1}"].shift(-1).fillna(0)
#         performance_reviews[f"rating_lag_difference{i}"]=performance_reviews[f"rating_lag_{i-1}"]-performance_reviews[f"rating_lag_{i}"]
#     performance_reviews=performance_reviews.groupby("employee_id").head(1)
#     performance_reviews["improvement_score"]=performance_reviews["rating_lag_0"]-performance_reviews["rating_lag_2"]
#     performance_reviews=performance_reviews[(performance_reviews["rating_lag_difference2"]>0) & (performance_reviews["rating_lag_difference1"]>0)]
#     df1= performance_reviews.merge(employees,on="employee_id", how="left")
#     result=df1.sort_values(
#         by=["improvement_score","name"],
#         ascending=[False,True])
#     return result[["employee_id","name","improvement_score"]]
   

    # 1. Sort by date ASCENDING so the logic "Newer - Older" is intuitive
    df = performance_reviews.sort_values(['employee_id', 'review_date'])
    
    # 2. Keep only the last 3 reviews for each employee to save memory
    df['review_count'] = df.groupby('employee_id')['review_id'].transform('size')
    last_3 = df[df['review_count'] >= 3].groupby('employee_id').tail(3).copy()
    
    # 3. Vectorized logic: Calculate the difference between consecutive ratings
    # Positive diff means the rating improved compared to the previous one
    last_3['score_diff'] = last_3.groupby('employee_id')['rating'].diff()
    
    # 4. Identify employees who do NOT have strictly increasing ratings
    # (i.e., any difference in the last 3 reviews is <= 0)
    # We skip the first of the 3 reviews because its diff is NaN
    invalid_ids = last_3[last_3['score_diff'] <= 0]['employee_id'].unique()
    valid_df = last_3[~last_3['employee_id'].isin(invalid_ids)]
    
    # 5. Calculate the improvement score: Latest Rating - Earliest Rating
    result = valid_df.groupby('employee_id').agg(
        improvement_score=('rating', lambda x: x.iloc[-1] - x.iloc[0])
    ).reset_index()
    
    # 6. Merge with names and sort by score (DESC) then name (ASC)
    return (
        result.merge(employees, on='employee_id')
        [['employee_id', 'name', 'improvement_score']]
        .sort_values(['improvement_score', 'name'],
        ascending=[False, True])
    )
