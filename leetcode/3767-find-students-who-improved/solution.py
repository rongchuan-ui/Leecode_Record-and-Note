import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    # scores["exam_date"]=pd.to_datetime(scores["exam_date"])
    # scores=scores[scores.groupby(["student_id","subject"])["exam_date"].transform("size")>=2]
    # scores=scores.sort_values(by=["student_id","subject","exam_date"])
    # scores_first=scores.groupby(["student_id","subject"]).head(1).reset_index().rename(columns={"score":"first_score"})
    # scores_last=scores.groupby(["student_id","subject"]).tail(1).reset_index().rename(columns={"score":"latest_score"})
    # scores=(scores_first.merge(scores_last,on=["student_id","subject"]))[["student_id","subject","first_score","latest_score"]].sort_values(
    #     by=["student_id","subject"],
    #     ascending=[True,True]
    # )
    # scores=scores[scores["first_score"]<scores["latest_score"]]
    # return scores

    scores = scores.sort_values(['student_id', 'subject', 'exam_date'])

    first = scores.drop_duplicates(['student_id', 'subject'], keep='first')
    latest = scores.drop_duplicates(['student_id', 'subject'], keep='last')
    
    res = pd.merge(
        first, latest, 
        on=['student_id', 'subject'], 
        suffixes=('_first', '_latest')
    )
   
    mask = (res['exam_date_first'] != res['exam_date_latest']) & \
           (res['score_latest'] > res['score_first'])
    
    ans = res[mask].rename(columns={
        'score_first': 'first_score',
        'score_latest': 'latest_score'
    })
    
    return ans[['student_id', 'subject', 'first_score', 'latest_score']].sort_values(['student_id', 'subject'])
