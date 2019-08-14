#!usr/bin/env python
# Python Program to mine data from a Brand's Facebook Account

import json
import facebook
# The library needed to read an excel file using Python 
from openpyxl import Workbook
from openpyxl import load_workbook

# The location of the input file 
filename_root = 'C:/Users/Synergos/OneDrive/Documents/SusMon_Facebook_API'
input_filename = filename_root + '/FBPage_Input.xlsx'

# Function that reads Access Token and Page ID from an Excel file
def getInputData():
    
    print("I am about to attempt opening this document")
    #open our excel input workbook
    wb_input = load_workbook(filename=input_filename,read_only=True)
    
    # select FBPage_Input.xlsx
    sheet = wb_input.active

    # get Page ID
    pageIdLabel = sheet['B1']
    pageIdValue = sheet['B2']
    pageIdValue = round(pageIdValue.value)

    # get Brand name
    pageNameLabel = sheet['C1']
    pageNameValue = sheet['C2']
    pageNameValue = pageNameValue.value

    # get Access Token
    pageAccessTokenLabel = sheet['D1']
    pageAccessTokenValue = sheet['D2']
    pageAccessTokenValue = pageAccessTokenValue.value
    

def main():
    # Call function to get input data
    getInputData()

    token = pageAccessTokenValue
    graph = facebook.GraphAPI(token)
    #fields = ['first_name', 'location{location}','email','link']
    profile = graph.get_object(pageIdValue,fields='name,fan_count,posts,link')
    #return desired fields
    print(json.dumps(profile, indent=4))

if __name__ == '__main__':
    main()