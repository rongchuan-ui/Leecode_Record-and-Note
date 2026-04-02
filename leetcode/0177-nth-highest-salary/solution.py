import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary=employee["salary"].drop_duplicates().sort_values(ascending=False)
    if N>0 and len(salary)>=N:
        NthHighestSalary=salary.iloc[N-1]
    else:
        NthHighestSalary=None
    
    return  pd.DataFrame({f"getNthHighestSalary({N})": [NthHighestSalary]})
