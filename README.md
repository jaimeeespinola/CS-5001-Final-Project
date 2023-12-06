# Final Project Report

* Student Name: Jaime Espinola
* Github Username: jaimeeespinola
* Semester: Fall 2023
* Course: CS 5001



## Description 
This project is a simple version of a drug library used in infusion pumps. I selected this project because I work on infusion pumps (the mechanical side) and the software component of it inspired me to begin studying computer science. Infusion pumps are used to give patients fluids and medications. In one method of pumping, the clinician provides information to the pump (medication name and patient weight) and the pump looks up the drug in the library and calculates the amount of medication that the clinician needs to give. The clinician then puts this amount of medication in an IV bag, and the pump infuses the medication.

## Key Features
The project allows for an automized infusion or a manually added infusion. It also allows the user to add drugs to the existing drub library file. In an automized infusion, the drug is already in the drug library - the user only needs to enter the patient weight and the program will calculate the dose. In a manually added infusion, the user directly enters the dose rate and patient weight, and the program calculates the dose. The project also includes appropriate warnings and confirmations to ensure that the user is ready to start infusion. The drug library includes warnings for each drug - the warnings can be displayed prior to starting infusion.

## Guide
To run the project, simply run the **drug_library.py** file and follow the in-file instructions. The program provides warnings and input specifications where possible, but general guidelines for formatting for inputs include:

* drug name - the name of the drug (not case sensitive)
* warnings to be added - can include spaces and punctuation, and is not case sensitive
* dose rate - must be a rate between 0.1 and 9.9 ml/lb
* patient weight - patient's weight in lbs
* filename - the name of the drug library - must be a txt file


## Installation Instructions
To run this project locally, download all files, **drug_library.py**, **app_user_inferface.py**, and **drug_library.txt**. Ensure that all files are saved in the directory in which you are working. The program will encounter an error if the drug_library file is not saved to the working directory. 

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

The two files with code in this project are:
* **app_user_input.py** - https://github.com/jaimeeespinola/CS-5001-Final-Project/blob/main/app_user_interaction.py
* **drug_library** - https://github.com/jaimeeespinola/CS-5001-Final-Project/blob/main/drug_library.py

Txt files that are required for this project are:
**drug_library_txt**

**app_user_input** contains the functions that interact with the user. Print statements that display information such as:


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

There are also numerous functions that ask for user input but do not print anything to the user, instead returns a value for the drug_library functions to use.
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



### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
