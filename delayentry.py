from supabase import create_client, Client
import string 
import os



SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class Delayentry:
    def delay_train(self, train_no, date, stations, arr_timings, dep_timings, holiday_flags, weathers):
        trip_id=str(train_no)+str(date)
        
        row=[]
        for i in range(len(stations)):
            row.append({
                "trip_id":trip_id
                "train_no":train_no,
                "station":stations[i]
                "actual_arr":arr_timings[i]
                "actual_dep":dep_timings[i]
                "holiday_flag": holiday_flags[i]
                "weather":weathers[i]
                })