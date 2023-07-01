import paramiko
import os
from utils.get_secret import get_secret

def load_credentials(secret_name):
    return get_secret(secret_name)

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
    cwd = os.getcwd()
    for file in files:
        new_file_name = prefix + file
        sftp.get(remote_directory + "/" + file, cwd + "/" + local_directory + "/" + new_file_name)

def close_connection(sftp):
    sftp.close()