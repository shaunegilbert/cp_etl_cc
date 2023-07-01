from src.utils.sftp_utils import (
    load_credentials,
    establish_sftp_connection,
    fetch_files,
    download_files,
    close_connection
)

# from dotenv import load_dotenv

# load_dotenv()

def test():
    ehps_creds = load_credentials('ehps_sftp')

    print(ehps_creds)
