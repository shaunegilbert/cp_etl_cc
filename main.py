import logging
from src.data import sftp_read

def main():
    try:
        sftp_read.test()
    except Exception as e:
        print(f'Failed: {str(e)}')

if __name__ == "__main__":
    main()


