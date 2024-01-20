""" This module provides functions for creating a series of project folders"""

#Imports
import pathlib
from pathlib import Path
import math
import statistics
import time

#Import Modules
import ColeNollette_utils

#Byline
print (f"Byline: {ColeNollette_utils} ")


#Function 1: Create a function to generate folders for a given range
def create_folders_for_range(start_year, end_year):
    """
    Creates a folder for range of years.
    :param start: First year to be created, e.g. 2000
    :param end: Last year to be created, e.g. 2024
    """
    for year in range(start_year, end_year +1):
        pathlib.Path(str(year)).mkdir(exist_ok=True)




#Function 2: Develop a function to create folders from a list of names
def create_folders_from_list(folder_names, to_lowercase=False, remove_spaces=False):
    """
    Creates folders from a list of folder names.
    :param folder_names: folders to be created
    """
    for i in folder_names:
        if to_lowercase:
            i=i.lower()
        if remove_spaces:
            i=i.replace(" ","")
        folder_names = str(i)
        Path(folder_names).mkdir(exist_ok=True)
        print(f"Folder '{folder_names}.")



#Function 3: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix
def create_prefixed_folders(folder_names, prefix):
    for i in folder_names:
        folder_names = str(prefix)+str(i)
        Path(folder_names).mkdir(exist_ok=True)
        print(f"Folder {folder_names}")



#Function 4: Write a function to create folders periodically 
def create_folders_periodically(duration_secs):
    num_folders = 5
    next_folder = 1 #Hopefully this will start the while loop

    while next_folder <= num_folders:
        pathlib.Path("folder-" + str(next_folder)).mkdir(exist_ok=True)
        next_folder += 1
        time.sleep(duration_secs)


#Create a path object
project_path = (pathlib.Path.cwd())

#Define the new sub folder path
data_path = project_path.joinpath("data")

#Create new if it doesn't exist

data_path.mkdir(exist_ok=True)

# Add module block at the bottom

def main():
    """Main function for module capabilities"""
    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2000, end_year=2024)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5 #duration is seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces
    # to one or more of your functions
    # Call your function and tese these
    regions = [
        "North America",
        "South America",
        "Europe",
        "Asia",
        "Africa",
        "Oceania",
        "Middle East"
    ]
    create_folders_from_list (regions, to_lowercase=True, remove_spaces=True)

if __name__ =='__main__':
    main()
