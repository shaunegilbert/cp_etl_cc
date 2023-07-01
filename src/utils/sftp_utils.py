import paramiko
import os
import json
from src.utils.get_secret import get_secret

def load_credentials(secret_name):
    try:
        secret = get_secret(secret_name)
        ehps_creds = json.loads(secret)
        return ehps_creds
    except Exception as e:
        raise Exception(f"Failed to load credentials: {str(e)}")


def establish_sftp_connection(creds):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(creds['hostname'], creds['port'], creds['username'], creds['password'])
    sftp = ssh.open_sftp()
    return sftp

def fetch_files(sftp, directory, file_extension):
    files = sftp.listdir(directory)
    return [file for file in files if file.endswith(file_extension)]

def download_files(sftp, files, remote_directory, local_directory, prefix=""):
    project_root = os.getcwd()
    data_directory = os.path.join(project_root, "data")
    raw_data_path = os.path.join(data_directory, "raw")
    
    # Ensure the data/raw directory exists
    if not os.path.exists(raw_data_path):
        os.makedirs(raw_data_path)
    
    for file in files:
        new_file_name = prefix + file
        local_file_path = os.path.join(raw_data_path, new_file_name)
        sftp.get(remote_directory + "/" + file, local_file_path)



def close_connection(sftp):
    sftp.close()