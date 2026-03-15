import flask
from flask import Flask, request, session, redirect, url_for, jsonify, render_template
from flask_login import login_user, logout_user, UserMixin
from supabase import create_client, Client
import os



SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class LoginManagerAuth:
        def authenticate(self, username, password):
              response = (supabase.table("Employee_details").select("*").eq("Email", username).eq("Password", password).execute())
              if response.data:
                  return True
              else:
                    return False


