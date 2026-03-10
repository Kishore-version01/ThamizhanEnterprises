from flask import Flask, request
from supabase import create_client, Client

import os


SUPABASE_URL = os.getenv("SUPA_URL")
SUPABASE_KEY = os.getenv("SUPA_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class RouteEntry:
    def route_entry():
        train_name = request.form.get("train_name")
        train_no = request.form.get("train_no")
        station_codes = request.form.getlist("station_code[]")
        stop_seq = request.form.getlist("stop_seq[]")
        sched_arr = request.form.getlist("sched_arr[]")
        sched_dep = request.form.getlist("sched_dep[]")
        distances = request.form.getlist("distance[]")
        
        rows = []
        for i in range(len(station_codes)):
            row = {
                "train_name": train_name,
                "train_no": train_no,
                "stop_seq": stop_seq[i],
                "sched_arr": sched_arr[i],
                "sched_dep": sched_dep[i],
                "station_code": station_codes[i],
                "distance_frm_source": distances[i]
                }
            rows.append(row)
        supabase.table("Route_data").insert(rows).execute()