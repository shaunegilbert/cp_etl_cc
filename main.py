import logging
from src.data import sftp_read
from src.data import sheets_read

def main():
    try:
        sftp_read.main()
        sheets_read.main()
    except Exception as e:
        print(f'Failed: {str(e)}')

if __name__ == "__main__":
    main()


