import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    # build a new dataframe to store swapped data
    seat_swap = seat.copy()
    # using loop to swap every two consecutive pair
    i=1
    while i<len(seat["id"]):
        seat_swap.iloc[i-1,1] = seat.iloc[i,1]
        seat_swap.iloc[i,1] = seat.iloc[i-1,1]
        i+=2
    return seat_swap



