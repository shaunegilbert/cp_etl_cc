import pandas as pd
import numpy as np
import os 
from dotenv import load_dotenv
from src.utils.standardize_phone import standardize_phone


def agreement_wrangle ():
    cp_agreements = pd.read_csv('data/raw/cp_agreements.csv')
    #rename agreement columns
    agreement_final = cp_agreements.rename(columns={
        'First Name': 'first_name',
        'Last Name': 'last_name',
        'Student ID number': 'id_number',
        'School': 'school',
        'District': 'district',
        'Agreement Completed': 'agreement_completed',
        'Emergency Contact Name': 'ec_name',
        'Emergency Contact Relation': 'ec_relation',
        'Emergency Contact Phone Number': 'ec_phone',
        'Emergency Contact Name (2)': 'ec2_name',
        'Emergency Contact (2) Relation': 'ec2_relation',
        'Emergency Contact (2) Phone Number': 'ec2_phone',
        'Does your child have any allergies?': 'allergies_yn',
        'If you answered yes that your child has allergies, please describe those allergies below': 'allergies_desc',
        'Do your child have any medical, physical, or mental health conditions that will require special attention/care?': 'other_med_yn',
        'If you answered "yes" that your child has any medical, physical, or mental health conditions, please provide details below.': 'other_med_desc',
        'Are there any other considerations we should know before we match your child with an internship?': 'other_consid_desc',
        'Student Signature': 'student_sig',
        'Date': 'sig_date',
        'Parent Signature': 'parent_sig',
        'Date 2':'sig2_Date', 
        'gt-id': 'gt_id',
        'Submission ID':'submission_id'
    })

    # drop columns
    agreement_final = agreement_final.drop(columns=['sig_date',
                                                'sig2_Date',
                                                'student_sig',
                                                'parent_sig',
                                                'submission_id'
                                                ])
    
    # change gf agreement timestamp to datetime
    agreement_final["Timestamp"] = pd.to_datetime(agreement_final["Timestamp"], format='%m/%d/%Y %H:%M:%S')

    # sort intent forms with most recent dates being first
    agreement_final = agreement_final.sort_values(by='Timestamp', ascending= False)

    # remove duplicate gt_id numbers and only keep the first
    agreement_final = agreement_final.drop_duplicates(subset='gt_id', keep="first")

    agreement_final['ec_phone'] = agreement_final['ec_phone'].apply(standardize_phone)
    agreement_final['ec2_phone'] = agreement_final['ec2_phone'].apply(standardize_phone)
    
    agreement_final.to_csv('data/processed/agreement_final.csv', index=False)
    
agreement_wrangle()

def main():
    agreement_wrangle()


if __name__ == "__main__":
    main()