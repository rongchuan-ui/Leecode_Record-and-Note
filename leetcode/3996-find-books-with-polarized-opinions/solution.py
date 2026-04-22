import pandas as pd

def find_polarized_books(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
    # A book has polarized opinions if it has at least one rating ≥ 4 and at least one rating ≤ 2
    reading_sessions_0=reading_sessions[reading_sessions["session_rating"]>=4]
    reading_sessions=reading_sessions[reading_sessions["book_id"].isin(reading_sessions_0["book_id"])]
    reading_sessions_1=reading_sessions[reading_sessions["session_rating"]<=2]
    reading_sessions=reading_sessions[reading_sessions["book_id"].isin(reading_sessions_1["book_id"])]

    # Only consider books that have at least 5 reading sessions
    reading_sessions=reading_sessions[reading_sessions.groupby("book_id")["session_id"].transform("size")>=5]

    # Calculate the rating spread as (highest_rating - lowest_rating)
    reading_sessions["rating_spread"]=(reading_sessions.groupby("book_id")["session_rating"].transform("max") - reading_sessions.groupby("book_id")["session_rating"].transform("min"))

    # Calculate the polarization score as the number of extreme ratings (ratings ≤ 2 or ≥ 4) divided by total sessions and Only include books where polarization score ≥ 0.6 (at least 60% extreme ratings)
    reading_sessions["is_extreme"]=((reading_sessions["session_rating"]<=2) | (reading_sessions["session_rating"]>=4)).astype(int)
    reading_sessions["polarization_score"]=(reading_sessions.groupby("book_id")["is_extreme"].transform("sum")/reading_sessions.groupby("book_id")["session_rating"].transform("count"))
    reading_sessions=reading_sessions[reading_sessions["polarization_score"]>=0.6]
    reading_sessions["polarization_score"] =(reading_sessions["polarization_score"]+1e-9).round(2)

    result=reading_sessions.merge(books,on="book_id")[["book_id","title","author","genre","pages","rating_spread","polarization_score"]].drop_duplicates().sort_values(
        by=["polarization_score","title"],
        ascending=[False,False]
    )

    return result
