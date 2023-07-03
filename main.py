import logging
import traceback
from src.data import sftp_read
from src.data import sheets_read
from src.wrangle import agreement_wrangle
from src.wrangle import app_wrangle
from src.wrangle import students_wrangle

def main():
    try:
        sftp_read.main()
        sheets_read.main()
        agreement_wrangle.main()
        app_wrangle.main()
        students_wrangle.main()
        print("All scripts ran successfully.")
    except Exception as e:
        print("Error occurred:")
        traceback.print_exc()

if __name__ == "__main__":
    main()