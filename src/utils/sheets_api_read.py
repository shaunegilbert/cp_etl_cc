from googleapiclient.discovery import build
from google.oauth2 import service_account
import tempfile
import os
from dotenv import load_dotenv


from .get_secret import get_secret

load_dotenv()

gs_api_secret = os.getenv('sheets_api_secret_name')

service_account_secret = get_secret(gs_api_secret)

# Write the secret to a temporary file
with tempfile.NamedTemporaryFile(suffix='.json', delete=False, mode='w') as f:
    f.write(service_account_secret)
    SERVICE_ACCOUNT_FILE = f.name  # This is now a path to a JSON file

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)