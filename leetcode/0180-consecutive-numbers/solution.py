import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # num_more_3times=[]
    # for i in range(0,len(logs["id"])-2):
    #     if logs.loc[i,"num"]==logs.loc[i+1,"num"] and logs.loc[i+1,"num"]==logs.loc[i+2,"num"]:
    #         num_more_3times.append(logs.loc[i,"num"])
    #         i=i+3
    #     else:
    #         i=i+1
    # return pd.DataFrame(
    #     {
    #         "ConsecutiveNums":num_more_3times
    #     }
    # )
    num_more_3times=[]
    i=0
    while i+2<len(logs["num"]):
        if logs.iloc[i,1]==logs.iloc[i+1,1] == logs.iloc[i+2,1]:
            num_more_3times.append(logs.iloc[i,1])
        i+=1
    ConsecutiveNums=pd.DataFrame({
        "ConsecutiveNums": list(set(num_more_3times))
    })
    return ConsecutiveNums
    


