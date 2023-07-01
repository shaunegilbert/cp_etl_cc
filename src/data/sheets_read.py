from src.utils.sheets_api_read import service
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

def sheets_data_pull():
    # pull staggered data entry personal info (JAWS) from google sheets
    sde_personal_info_query = os.getenv('sde_personal_info_query')
    sheet = service.spreadsheets()
    results_sde_personal_info = sheet.values().get(spreadsheetId = sde_personal_info_query,
                                range="Data!A1:Z").execute()
    sde_personal_info = results_sde_personal_info.get('values', [])
    sde_personal_info = pd.DataFrame(sde_personal_info[1:], columns=sde_personal_info[0]).fillna(np.nan)
    sde_personal_info.to_csv('data/raw/sde_personal_info.csv', index=False)

    # pull workshop attendance (JAWS) from google sheets
    s50_workshop_attendance_query = os.getenv('s50_workshop_attendance_query')
    sheet = service.spreadsheets()
    results_workshop_attendance = sheet.values().get(spreadsheetId = s50_workshop_attendance_query,
                                range="Data!A1:Z").execute()
    workshop_attendance = results_workshop_attendance.get('values', [])
    workshop_attendance = pd.DataFrame(workshop_attendance[1:], columns=workshop_attendance[0]).fillna(np.nan)
    workshop_attendance.to_csv('data/raw/workshop_attendance.csv', index=False)


