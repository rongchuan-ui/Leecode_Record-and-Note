import pandas as pd

def find_overbooked_employees(employees: pd.DataFrame, meetings: pd.DataFrame) -> pd.DataFrame:
    meetings["meeting_date"]=pd.to_datetime(meetings["meeting_date"])
    meetings["week"]=meetings["meeting_date"].dt.isocalendar().week
    meetings["year"]=meetings["meeting_date"].dt.year
    meetings=meetings.groupby(["employee_id","year","week"]).agg(
        total_meeting_h=("duration_hours","sum")
    )
    meetings["meeting_ratio"]=meetings["total_meeting_h"]/40
    meetings["meeting_heavy"]=meetings["meeting_ratio"].map(lambda x: 1 if x> 0.5 else 0)
    meetings=meetings.groupby(["employee_id"]).agg(
        meeting_heavy_weeks=("meeting_heavy","sum")
    )
    meetings=meetings[meetings["meeting_heavy_weeks"]>=2]
    result=employees.merge(meetings, on="employee_id", how="inner").sort_values(
        by=["meeting_heavy_weeks","employee_name"],
        ascending=[False,True]
    )
    return result
