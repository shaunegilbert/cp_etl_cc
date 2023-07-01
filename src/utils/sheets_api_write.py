# libraries for google sheets push
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import tempfile

from .get_secret import get_secret

service_account_secret = get_secret('sheets_api_6_23')

# Write the secret to a temporary file
with tempfile.NamedTemporaryFile(suffix='.json', delete=False, mode='w') as f:
    f.write(service_account_secret)
    SERVICE_ACCOUNT_FILE = f.name  # This is now a path to a JSON file

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)

gc = gspread.authorize(credentials)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

