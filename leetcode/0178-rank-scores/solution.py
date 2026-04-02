import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    j=1
    scores=scores.sort_values("score",ascending=False).reset_index(drop=True)
    scores["rank"] = 0  
    for i in range(0,len(scores["score"])):
        if i+1 <len(scores["score"]):
            if scores.loc[i,"score"] == scores.loc[i+1,"score"]:
                scores.loc[i:i+1,"rank"]=j
            else:
                scores.loc[i,"rank"]=j
                j+=1
        else:
            scores.loc[i,"rank"]=j
        i+=1
    return pd.DataFrame({
        "score":scores["score"],
        "rank":scores["rank"]
    })

# def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
#     scores = scores.sort_values("score", ascending=False).copy()
#     scores["rank"] = scores["score"].rank(method="dense", ascending=False).astype(int)
#     return scores[["score", "rank"]]
    
