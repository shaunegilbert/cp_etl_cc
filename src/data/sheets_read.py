from src.utils.sheets_api_read import service
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

def agreement_pull():
    # pull staggered data entry personal info (JAWS) from google sheets
    cp_agreements_query = os.getenv('cp_agreements_query')
    sheet = service.spreadsheets()
    results_cp_agreements = sheet.values().get(spreadsheetId = cp_agreements_query,
                                range="agreement_query!A1:Z").execute()
    cp_agreements = results_cp_agreements.get('values', [])
    cp_agreements = pd.DataFrame(cp_agreements[1:], columns=cp_agreements[0]).fillna(np.nan)
    cp_agreements.to_csv('data/raw/cp_agreements.csv', index=False)


def app_pull(service, form_names: List[str], root_dir='data/raw'):
    sheet = service.spreadsheets()
    for form_name in form_names:
        google_form_id = os.getenv(f'{form_name}_google_form') # Get the Google form ID from environment variables
        if google_form_id is None:
            print(f"Couldn't find environment variable for {form_name}_google_form")
            continue
        # Get the data
        form_name_without_app = form_name.replace("_app", "")
        results = sheet.values().get(spreadsheetId=google_form_id, range="{}_application!A1:AH".format(form_name_without_app)).execute()
        data = results.get('values', [])
        df = pd.DataFrame(data[1:], columns=data[0]).fillna(np.nan)
        # Save to CSV
        output_filename = os.path.join(root_dir, f'app_{form_name_without_app}.csv') # Changed the output file name
        df.to_csv(output_filename, index=False)

# Define the form names
form_names = ['bhs_app', 'bps_app', 'ehps_app', 'gp_app', 'hphs_app', 'nb_app', 'pa_app', 'whs_app']

# Call the function
app_pull(service, form_names)

# # pull _cp_etl_sftp_comparison (JAWS)
# def students_pull():
#     # pull staggered data entry personal info (JAWS) from google sheets
#     students_compare_query = os.getenv('students_compare_query')
#     sheet = service.spreadsheets()
#     results_students_compare = sheet.values().get(spreadsheetId = students_compare_query,
#                                 range="data!A1:Z").execute()
#     students_compare = results_students_compare.get('values', [])
#     students_compare = pd.DataFrame(students_compare[1:], columns=students_compare[0]).fillna(np.nan)
#     students_compare.to_csv('data/raw/students_compare.csv', index=False)

def main():
    agreement_pull()
    form_names = ['bhs_app', 'bps_app', 'ehps_app', 'gp_app', 'hphs_app', 'nb_app', 'pa_app', 'whs_app']
    app_pull(service, form_names)
    # students_pull()


if __name__ == "__main__":
    main()

