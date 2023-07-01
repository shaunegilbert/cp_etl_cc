import os
import csv

from src.utils.sftp_utils import (
    load_credentials,
    establish_sftp_connection,
    fetch_files,
    download_files,
    close_connection)

# from dotenv import load_dotenv

# load_dotenv()

# def test():
#     ehps_creds = load_credentials('ehps_sftp')

#     print(ehps_creds)

def ehps_pull():
    try:
        ehps_creds = load_credentials("ehps_sftp")  # Replace with actual secret name
        ehps_sftp = establish_sftp_connection(ehps_creds)
        ehps_files = fetch_files(ehps_sftp, '/ehps_uploads/', '.txt')
        download_files(ehps_sftp, ehps_files, '/ehps_uploads/', ".", prefix="")

        # Convert EHPS .txt files to CSV
        convert_files_to_csv(ehps_files)

        close_connection(ehps_sftp)
    except Exception as e:
        print(f'Failed: {str(e)}')

def convert_files_to_csv(files):
    for file in files:
        if file.endswith('.txt'):
            txt_file_path = os.path.join("data", "raw", file)
            csv_file_path = os.path.join("data", "raw", os.path.splitext(file)[0] + ".csv")

            with open(txt_file_path, 'r') as txt_file, open(csv_file_path, 'w', newline='') as csv_file:
                txt_reader = csv.reader(txt_file, delimiter='\t')
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(txt_reader)

            os.remove(txt_file_path)

def main():
    ehps_pull()
    convert_files_to_csv()

if __name__ == "__main__":
    main()
