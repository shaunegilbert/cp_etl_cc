import pandas as pd
import numpy as np
import os 
from dotenv import load_dotenv
from src.utils.standardize_phone import standardize_phone

def pull_csv_files(directory):
    app_files = [
        'app_bhs.csv',
        'app_bps.csv',
        'app_ehps.csv',
        'app_gp.csv',
        'app_hphs.csv',
        'app_nb.csv',
        'app_pa.csv',
        'app_whs.csv'
    ]

    data_frames = []

    for file in app_files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path)
            data_frames.append(df)
        else:
            print(f"{file} does not exist in the specified directory.")

    return data_frames

def main():
    directory = 'data/raw/'
    data_frames = pull_csv_files(directory)

    app_final = pd.concat(data_frames, ignore_index=True)

    # Standardize phone numbers
    phone_columns = ['Student Phone Number', 'Parent/Guardian Phone Number', 'Parent/Guardian Phone Number(2)']
    for col in phone_columns:
        app_final[col] = app_final[col].apply(standardize_phone)
        
    app_final.to_csv('data/processed/app_final.csv', index=False)

if __name__ == "__main__":
    main()




