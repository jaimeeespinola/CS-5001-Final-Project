"""
Final Project: Drug Library
===========================
Course:   CS 5001

This file contains the code related to client interaction. At a later time, this file could be changed to use 
a GUI instead of the console. This program displays information to the client and gets information from the client.
"""
from drug_class import Drug

def print_welcome() -> str:
    """ Prints a welcome message and returns what the user wishes to do. If it is start infusion, it returns start.
     If it is add a drug, it returns add
     Inputs - None
     Returns - User selection for how to proceed
    """
    print('Welcome to the SMART IV PUMP')
    selection = input('To start an infusion, type "start" \n To add a drug to the library, type "add"\n')
    if selection == "start":
        return "start"
    if selection == "add":
        return "add"


def print_infusion_message() -> None:
    """ Print the end message """
    print('testicles...\n ... \n .... \n')


def print_shut_down_message() -> None:
    """ Prints the shut down message"""
    print('Shutting down')


def confirm_infusion_message() -> str:
    """ Confirm that the user wants to start infusion.
   

    Returns:
        str: user selection for whether to start the infusion or return to the welcome message
    """
    begin_infusion = input('To begin infusion, type "begin" \n').strip()
    return begin_infusion


def get_filename() -> str:
    """ Get the filename of the drug library
    Returns:
        str: filename
    """
    filename = input('Enter the filename for the drug library: ').strip()
    if filename.endswith('.txt'):
        return filename
    else:
        print('Filename must end with .txt')
        return get_filename()


def get_patient_weight() -> int:
    """ Get the patient weight from the user. 

    The weight must be a int, if it is not, the user will be prompted to enter an int
    Returns:
        int: patient weight
    """
    patient_weight = int(input('Enter the patient weight in lbs: ').strip())
    if type(patient_weight) != int:
        print('Weight must be a whole number')
        return get_patient_weight()
    else:
        return patient_weight
    
def get_drug_name() -> str:
    """ Get the name of the drug to be infused. 

    Returns:
        str: the name of the drug to be infused
    """
    drug_name = input('Enter the drug to be infused: ').strip()
    return drug_name

def get_dose_rate() -> float:
    """ Get the manual dose rate for a drug that is not included in the library
    
    The dose rate must be a float, if it is not, the user will be prompted to enter a float
    Returns:
        float: dose rate in mL/lb of body weight
    """
    proceed = input('Drug not found in library. WARNING: Not recommended to run pump in manual mode. To proceed in manual mode, enter "yes"\n').strip()
    if proceed == "yes":
        dose_rate = input('Enter the dose rate in mL/lb (example 0.2 or 1.5): ').strip()
        return dose_rate
    else:
        print_welcome()


def get_drug_info() -> str:
    """ Get the name, dose rate, and warnings of the drug to be infused

    Returns:
        tuple: the name, dose rate, and warnings of the drug
    """
    drug_name = input('Enter the name of the drug to be added: ').strip()
    warnings = input('Enter any warnings for the drug to be added: ').strip()
    dose_rate = input('Enter the dose rate of the drug to be added as a decimal (example 0.3 or 1.5): ').strip()
    drug = Drug(drug_name, dose_rate, warnings)
    return "\n" + drug.name + " " + drug.rate + " " + drug.warnings


    '''drug_name = input('Enter the drug to be added: ').strip()
    warnings = input('Enter any warnings for the drug to be added: ').strip()
    dose_rate = input('Enter the dose rate of the drug to be added as a decimal (example 0.3 or 1.5): ').strip()
    drug_info = "\n" + drug_name + " " + dose_rate + " " + warnings
    return drug_info'''
