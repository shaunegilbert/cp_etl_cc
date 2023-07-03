import pandas as pd
import numpy as np

def ehps_wrangle():
    ehhs_students=pd.read_csv('data/raw/ReadyCT_EHHS_export.csv')
    synergy_students = pd.read_csv('data/raw/ReadyCT_Synergy_export.csv')
    
    # adding school columns
    ehhs_students['school'] = "East Hartford High School"
    synergy_students['school'] = "Synergy High School"

    #concat synergy and ehps student dataframes
    ehps_students = pd.concat([ehhs_students, synergy_students], axis= 0)

    #add district code
    ehps_students['district_code']= 'ehps'

    # rename coluns
    ehps_new_column_names = {
        'STUDENTS.Student_Number': 'id_number',
        'STUDENTS.State_StudentNumber': 'state_id_number',
        'STUDENTS.Last_Name': 'last_name',
        'STUDENTS.First_Name': 'first_name',
        'STUDENTS.ClassOf': 'cohort_year',
        'STUDENTS.Grade_Level': 'grade',
        'STUDENTS.Home_Room': 'home_room',
        'STUDENTS.ExitDate': 'exit_date',
        'S_CT_STU_X.facilitycode1': 'ehps_facility',
        'school':'school',
        'district_code':'district_code'
    }
    ehps_students = ehps_students.rename(columns=ehps_new_column_names)

    #drop rows without id number
    ehps_students = ehps_students.dropna(subset=['id_number'])

    # drop the state ID number
    ehps_students = ehps_students.drop('state_id_number', axis=1)
    
    ehps_students.to_csv('data/interim/ehps_students.csv', index=False)
    
    return ehps_students

def hps_wrangle():
    hps_students=pd.read_csv('data/raw/hps_students.csv')
    
    #add district code to hps_students
    hps_students['district_code']='hps'

    hps_new_column_names = {
        'STUDENT_NUMBER': 'id_number',
        'LAST_NAME': 'last_name',
        'FIRST_NAME': 'first_name',
        'COHORTYR': 'cohort_year',
        'GRADE_LEVEL': 'grade',
        'HOME_ROOM': 'home_room',
        'HOUSE': 'house',
        'ADA_INDICATOR': 'ada_indicator',
        'CUMULATIVE_GPA': 'cumulative_gpa',
        'BEHAVIOR_INDICATOR': 'behavior_indicator',
        'ENROLLMENT_SCHOOLID': 'school_id',
        'SCHOOL_NAME': 'school',
        'EXITDATE': 'exit_date',
        'CREDITS_ATTEMPTED': 'credits_attempted',
        'CREDITS_EARNED': 'credits_earned',
        'district_code': 'district_code'
    }
    hps_students = hps_students.rename(columns=hps_new_column_names)

    # drop rows without id number
    hps_students = hps_students.dropna(subset=['id_number'])

    # calculate completion rate
    hps_students['completion_rate'] = hps_students['credits_earned'] / hps_students['credits_attempted']
    
    hps_students.to_csv('data/interim/hps_students.csv', index=False)
    
    return hps_students

def merge_students(ehps_students, hps_students):
    merged_students = pd.concat([ehps_students, hps_students], axis=0, ignore_index=True)
    merged_students.to_csv('data/processed/sftp_students.csv', index=False)
    return merged_students

def main():
    ehps_students = ehps_wrangle()
    hps_students = hps_wrangle()
    merge_students(ehps_students, hps_students)
    
if __name__ == "__main__":
    main()
        
