import boto3
import json
from botocore.exceptions import ClientError


# Function to fetch secrets from AWS Secrets Manager
def get_secret(secret_name, key_name=None):
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        # Get the secret
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # Handle exceptions
        raise e

    # Decrypts secret using the associated KMS key
    secret = get_secret_value_response['SecretString']

    # If a specific key of the secret is requested
    if key_name:
        secret_dict = json.loads(secret)
        secret = secret_dict.get(key_name)
        if secret is None:
            raise Exception(f"The key '{key_name}' does not exist in the secret '{secret_name}'.")

    return secret