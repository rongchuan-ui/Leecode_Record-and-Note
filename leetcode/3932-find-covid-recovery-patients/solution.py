import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
    covid_tests=covid_tests.sort_values(
        by=["patient_id","test_date"],
        ascending=[True,True]
    )
    df_postive=covid_tests[covid_tests["result"]=="Positive"].groupby("patient_id").head(1).rename(columns={
        "test_date":"First_positive_date",
        "result":"Postive_result"
    })
    df=covid_tests.merge(df_postive,on="patient_id",how="left")
    df=df[(df["result"]== "Negative") & (df["test_date"]>df["First_positive_date"])]
    df=df.groupby("patient_id").head(1)
    df["test_date"] = pd.to_datetime(df["test_date"])
    df["First_positive_date"] = pd.to_datetime(df["First_positive_date"])
    df["recovery_time"]=(df["test_date"]-df["First_positive_date"]).dt.days
    result=df.merge(patients,on="patient_id",how="left")[["patient_id","patient_name","age","recovery_time"]].sort_values(
        by=["recovery_time","patient_name"],
        ascending=[True,True]
    )
    return result


    




