'''
Final Project: Drug Library
===========================
Course:   CS 5001

This file contains the main driver for the application.
'''
from drug_class import Drug
from app_user_input import *

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
                rate = line[0:4]
                return rate
            else:
                manual_rate = get_dose_rate()
                return manual_rate


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

'''def menu_options(drug) -> None:
    Returns the appropriate information based on what the user selects during the infusion
    Inputs - None
    Returns - None

    print(drug)
#  aspirin = Drug("aspirin", "10")  
#  menu_options(aspirin) stopped here'''
def main():
    if print_welcome() == "start":
        drug = access_drug_library()
        patient_weight = get_patient_weight()
        dose_rate = round(float(drug) * float(patient_weight), 2)
        print(f"Infusion amount is {dose_rate} mL")
        if confirm_infusion_message() == "begin":
            print_infusion_message()
        else:
            print_welcome()

    elif print_welcome() == "add":
        add_drug()
    else: 
        print_shut_down_message()


    
main()
