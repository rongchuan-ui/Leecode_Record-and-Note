import pandas as pd
# data = [[1, 100], [2, 200], [3, 300]]
# employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
# row驱动的写法

# 等价的列驱动写法：
# employee=(
#     pd.DataFrame({
#        "id": [1,2,3],
#        "salary": [100,200,300]
# }).astype({
#     "id": "int64",
#     "salary": "int64"
# }))

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # S=employee["salary"].drop_duplicates()
    # S=S.sort_values(ascending=False)
    # if len(S)>=2:
    #   second=S.iloc[1]
    # else:
    #   second=None
    # return pd.DataFrame({"SecondHighestSalary": [second]})
    
    max1 = employee["salary"].max()
    below = employee.loc[employee["salary"]<max1,"salary"]
    if not below.empty:
        second=below.max()
    else:
        second=None
    return pd.DataFrame({"SecondHighestSalary": [second]})


# DataFrame 选单列 → Series
# Series .to_numpy() / .values → ndarray
# 双中括号永远是 DataFrame

    
