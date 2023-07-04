import pandas as pd
import numpy as np

# so this is really only going to work to identify students from schools with sftp. I did not import intent forms and this will not work for great path, bristol, or new britain
students=pd.read_csv('data/processed/sftp_students.csv')
agreement=pd.read_csv('data/processed/agreement_final.csv')
app=pd.read_csv('data/processed/app_final.csv')

def app_agreement():
    # Filter dataframes by district
    sftp_districts = ['hps', 'ehps']
    sftp_agreement_filtered = agreement[agreement['district'].isin(sftp_districts)]
    sftp_app_filtered = app[app['district'].isin(sftp_districts)]
    # sftp_intent_filtered = intent[intent['district'].isin(sftp_districts)]

    # Create dataframes for values that match
    sftp_prod_agreement = pd.merge(students[['gt_id']], sftp_agreement_filtered, on='gt_id', how='inner')
    sftp_prod_app = pd.merge(students[['gt_id']], sftp_app_filtered, on='gt_id', how='inner')
    # sftp_prod_intent = pd.merge(students[['gt_id']], sftp_intent_filtered, on='gt_id', how='inner')

    # Create error tables for values that don't match
    sftp_agreement_error = pd.merge(sftp_agreement_filtered, students[['gt_id']], on='gt_id', how='outer', indicator=True).query("_merge == 'left_only'")
    sftp_app_error = pd.merge(sftp_app_filtered, students[['gt_id']], on='gt_id', how='outer', indicator=True).query("_merge == 'left_only'")
    # sftp_intent_error = pd.merge(sftp_intent_filtered, students[['gt_id']], on='gt_id', how='outer', indicator=True).query("_merge == 'left_only'")

    # Keep only the columns in agreement, app, and intent
    sftp_agreement_error.drop(columns=['_merge'], inplace=True)
    sftp_app_error.drop(columns=['_merge'], inplace=True)
    # sftp_intent_error.drop(columns=['_merge'], inplace=True)
    
    print(sftp_prod_agreement)
    print(sftp_prod_app)
    print(sftp_agreement_error.shape)
    print(sftp_app_error.shape)

app_agreement()

