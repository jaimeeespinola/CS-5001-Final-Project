'''
Final Project: Drug Library
===========================
Course:   CS 5001

This file contains the main driver for the application.
'''
from app_user_interaction import *

def access_drug_library() -> int:
    '''Opens the file where the drug library is located
    Searches the drug library for the drug that the user entered
    If the drug is found in the library, it returns the dose rate associated with drug
    If it is not found, it runs the function to add the dose rate manually
    
    Inputs - none
    Returns - dose rate
    '''
    drug_name = get_drug_name()
    filename = get_filename()
    with open(filename, "r") as file:
        for line in file:
            if drug_name in line:
                rate_warnings = line[(len(drug_name) + 1):]
                rate = rate_warnings[0:4]
                warnings = rate_warnings[4:]
                return (rate, warnings)    
        get_dose_rate()


def add_drug() -> None:
    '''Takes the filename that the user enters, and adds a new drug to that file
    
    Inputs - None 
    Returns - None
    '''
    to_add = get_drug_info()
    filename = get_filename()
    file_to_write = open(filename, "a")
    file_to_write.write(to_add)
    file_to_write.close()

def calculate_dose_rate() -> str:
    drug_warnings = access_drug_library()
    drug = drug_warnings[0]
    warnings = drug_warnings[1]
    patient_weight = get_patient_weight()
    dose_rate = round(float(drug) * float(patient_weight), 2)
    return dose_rate, warnings


def main():
    if print_welcome() == "start":
        '''drug_warnings = access_drug_library()
        drug = drug_warnings[0]
        warnings = drug_warnings[1]
        patient_weight = get_patient_weight()
        dose_rate = round(float(drug) * float(patient_weight), 2)'''
        dose_warnings = calculate_dose_rate()
        dose_rate = dose_warnings[0]
        print(f"Infusion amount is {dose_rate} mL")
        if confirm_infusion_message() == "begin":
            if print_get_warning() == "yes":
                warnings = dose_warnings[1]
                print(warnings)
                if confirm_infusion_message() == "begin":
                    print_infusion_message()
                    print_shut_down_message()
                else:
                    print_welcome()
            elif print_get_warning() == "infuse":
                print_infusion_message()
                print_shut_down_message()
        else:
            print_welcome()
    elif print_welcome() == "add":
        add_drug()
    else: 
        print_welcome()


main()
