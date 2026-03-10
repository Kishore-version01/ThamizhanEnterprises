from supabase import create_client, Client
import string
import os



SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class Delayentry:
    def route_dropdown(self, train_no):
        response = supabase.table("Route_data").select("stop_seq,distance_frm,station,sched_arr,sched_dep").eq("train_no",train_no).order("stop_seq").execute()
        for row in response.data:
            print(row["station"], row["stop_seq"])
        return response.data

    def delay_train(self, train_no, date, stations, arr_timings, dep_timings, holiday_flags, weathers):
        trip_id=str(train_no)+str(date)
        route_data = self.route_dropdown(train_no)

        rows=[]
        
        for i in range(len(stations)):
            rows.append({
                "trip_id" : trip_id,
                "date":date,
                "train_no":train_no,
                "stop_seq":route_data["stop_seq"],
                "station":stations[i],
                "distance_frm_src":route_data["distance_frm"],
                "sched_arr":route_data["sched_arr"],
                "sched_dep":route_data["sched_dep"],
                "actual_arr":arr_timings[i],
                "actual_dep":dep_timings[i],
                "holiday_flag": holiday_flags[i],
                "weather":weathers[i]
                })
        supabase.table("Delay_format").insert(rows).execute()