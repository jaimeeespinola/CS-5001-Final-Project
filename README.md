# Final Project Report

* Student Name: Jaime Espinola
* Github Username: jaimeeespinola
* Semester: Fall 2023
* Course: CS 5001



## Description 
This project is a simple version of a drug library used in infusion pumps. I selected this project because I work on infusion pumps (the mechanical side) and the software component of pumps inspired me to begin studying computer science. Infusion pumps are used to give patients fluids and medications. In one method of pumping, the clinician provides information to the pump (medication name and patient weight) and the pump looks up the drug in the library and calculates the amount of medication that the clinician needs to give. The clinician then puts this amount of medication in an IV bag, and the pump infuses the medication.

## Key Features
The project allows for an automized infusion or a manually added infusion. It also allows the user to add drugs to the existing drub library file. In an automized infusion, the drug is already in the drug library - the user only needs to enter the patient weight and the program will calculate the dose. In a manually added infusion, the user directly enters the dose rate and patient weight, and the program calculates the dose. The project also includes appropriate warnings and confirmations to ensure that the user is ready to start infusion. The drug library includes warnings for each drug - the warnings can be displayed prior to starting infusion.

## Guide
To run the project, simply run the **drug_library.py** file and follow the in-file instructions. The program provides warnings and input specifications where possible, but general guidelines for formatting for inputs include:

* drug name - the name of the drug (not case sensitive)
* warnings to be added - can include spaces and punctuation, and is not case sensitive
* dose rate - must be a rate between 0.1 and 9.9 ml/lb
* patient weight - patient's weight in lbs
* filename - the name of the drug library - must be a txt file

To access a drug that is already in the library, try dopamine or moprphine (the more well known).

## Installation Instructions
To run this project locally, download all files, **drug_library.py**, **app_user_inferface.py**, and **drug_library.txt**. Ensure that all files are saved in the directory in which you are working. The program will encounter an error if the drug_library file is not saved to the working directory. 

## Code Review
The two files with code in this project are:
* **app_user_input.py** - https://github.com/jaimeeespinola/CS-5001-Final-Project/blob/main/app_user_interaction.py
* **drug_library** - https://github.com/jaimeeespinola/CS-5001-Final-Project/blob/main/drug_library.py

Txt files that are required for this project are:
* **drug_library_txt** - https://github.com/jaimeeespinola/CS-5001-Final-Project/blob/main/drug_library.txt

**app_user_interaction** contains the functions that interact with the user. Print statements that display information such as:
```python
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
    else:
        print_welcome()
```
This code snippet provides an example of one of the many print statements that is included in the file. It is written recurselively so that if the user does not enter one of the two program options (add drug or start infusion), it continues to prompt the user until they select one of these options.


There are also several print statements that do not require any user input. For example:
```python
def print_shut_down_message() -> None:
    """ Prints the shut down message"""
    print('Infusion Complete. \n Shutting down')
```
This code snippet simply prints the shut down message.


There are also numerous functions that ask for user input but do not print anything to the user, instead returns a value for the drug_library functions to use. For example:
```python
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
```
This code snippet asks the user to input the name of the file for the drug library. It is also written recursively so that is the user inputs a file that is not a txt file, it will continue to prompt the user until they do so.


**drug_library.py** contains the main driver for the application. There are three functions and the main() which drive the program.

The first is access_drug_library:
```python
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
```
The function prompts the user to enter the drug name by calling the get_drug_name() function. It then prompts the user and calls a function to get the filename. It then seaches the filename to see if the drug name is in the file. If it is, it stores both the rate and the warnings for that drug. If it is not found in the file, it calls the get_dose_rate() function (another function within app_user_interaction) , which prompts the user to manually enter the dose rate.


The second function is add_drug():
```python
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
```
This function calls the functions needed to add a drug to the drug library. It first gets the information to be added by called get_drug_info() - this function prompts the user for the drug name, dose rate, and warnings associated with the drug. Then the function prompts the user for the the filename, appends the new drug information to this file, and closes the file.


The third and final function is calculate_dose():
```python
def calculate_dose() -> tuple:
    '''Calcuates the dose in mL of the drug to be infused. The dose is calculated
    based on the dose rate (is either pulled from the library or entered manually if
    the drug is not found in the library) and the patient weight in lbs

    Inputs - None
    Returns = Tuple of dose, warnings
    '''
    drug_warnings = access_drug_library()
    dose_rate = drug_warnings[0]
    warnings = drug_warnings[1]
    patient_weight = get_patient_weight()
    dose = round(float(dose_rate) * float(patient_weight), 2)
    return dose, warnings
```
This function calculates the dose of the drug to be infused. It first calls the function to access the drug library to get the warnings and the rates for the drug, and it calls the function to get patient weight. It then calculates the dose my multiplying the dose rate by the patient wait.


The drug_library.txt file contains a list of drugs, their dose rate, and their warnings. For example:
* amiodarone 5.0 Class III antiarrthythmic
* bretylium 5.0 Should not be used in place of more rapidly acting agents.
* cisatricurium 0.2 Non-depolarizing neuromuscular blocking agent

### Major Challenges
Some aspects that I struggled on were organizing all of my functions and figuring out how to test everything. The organization was difficult because there was a lot of information to get from the user, and I had to determine how to do it in an organized way. Testing was difficult for this project because it is all based on user input, so you cannot easily use doctest or build a test program. Instead, I needed to think of all the possible paths the program can go in based on different inputs, and also think of all the things the user could enter that they are not supposed to enter.


## Example Runs
There are three example videos that show execution of the 3 major functions of the project. They are zipped into a file here:
* https://github.com/jaimeeespinola/CS-5001-Final-Project/blob/main/Example%20Runs.zip

* Add a drug - Shows adding a drug to the drug library.
* Start a drug that is in the drug library - shows running a drug that is in the drug library. This video also shows what happens if the user does not enter a txt filename and shows the warnings when the user indicates they would like to read them before infusing.
* Start a drug that is not in the drug library - shows running a drug that is not in the library and how the user can manually enter the dose rate.

The example videos show the correct function of the program.

## Testing
Since the project was based entirely on user input, the way to test it was to practice all the possible inputs and see if it was possible to break the programs. I also tested each function individually before implementing the main(). In the repository there are the text outputs for testing completed:

* Add a drug - https://github.com/jaimeeespinola/CS-5001-Final-Project/blob/main/add%20drug.rtf 
* Start a drug that is in the drug library - https://github.com/jaimeeespinola/CS-5001-Final-Project/blob/main/start%20drug%20in%20library.rtf
* Start a drug that is not in the drug library - https://github.com/jaimeeespinola/CS-5001-Final-Project/blob/main/Start%20drug%20not%20in%20library.rtf


## Missing Features / What's Next
A few features that I would have liked to include are creating the drug as a class and using some of the fucntionality of classes. I also would have liked to add an error loop for when the file does not exist in the directory. I cused this error quite a few times when testing my program and would have to start over each time. I tried for some time to implement the error loop but was not able to do so in the time that I had. Finally, I would like to include more types of infusions. I simplified the infusion options by only including infusion by volume. In reality, there are much more complicated infusions. For example infusions that infuse at one rate for a period of time to start, and after a certime time (or volume), change to a slower rate of infusion. In the future, that functionality could be added to this project.

## Final Reflection
Overall I had a good experience in this course - I found it to be a good mix of frustrating and rewarding. I find that personally, if I am not getting frustrated, I am not learning. This couse was able to get me to that frustrated point, but also had enough time/support so that being able to successfully complete the assignments. By completing the assignments correctly, I was able to prove to myself that I was capable of understanding the content. I did learn a lot of programming concepts such as functions, classes, lists, and recursiveness. However, I also learned how to work for shorter periods of time and take breaks. I know we were told at the beginning, but it did take me a bit to learn that often the best way to solve something is to actually stop trying for a bit (and then return later). I feel that from a programming perspective, I need a bit more practice in classes and opening/writing files. I chose to include writing and reading files in my final project to get a little more practice, but I struggled with the concept and still feel a bit more uncomfortable in this area than in others. Finally, I need to continue working on taking breaks and not getting frustrated and wanting to solve everything immedietly. I enjoyed this course and and looking foward to what is to come in the next courses.

