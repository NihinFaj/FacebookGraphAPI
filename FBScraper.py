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
keyword_filename = filename_root + '/SusMon_Keywords.xlsx'

# Function that reads Access Token and Page ID from an Excel file


def getInputData():

    # open the excel input workbook
    wb_input = load_workbook(filename=input_filename, read_only=True)

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

    # Store ID and Access token in a dictionary
    d = dict()
    d['pageId'] = pageIdValue
    d['accessToken'] = pageAccessTokenValue
    return d

# Function to get all sustainability keywords from an excel file


def getSustainabilityKeywords():

    # open the keyword excel workbook
    kw_wb_input = load_workbook(filename=keyword_filename)

    # select SusMon_Keywords.xlsx
    kw_sheet = kw_wb_input.active

    # Get all the keywords from the first column
    m_row = kw_sheet.max_row

    # Initialize keyword list
    keywordList = []

    for i in range(1, m_row + 1):
         cell_obj = kw_sheet.cell(row=i, column=1)
         keywordList.append(cell_obj.value)

    print(keywordList)

def createOutputFile():

    responseFromFacebook = connectToFacebook()

    wb = Workbook()

    # set file path
    filePath = 'C:/Users/Synergos/OneDrive/Documents/SusMon_Facebook_API/FBOutput.xlsx'

    # Save file in the path
    wb.save(filePath)

    # Load workbook
    wb = load_workbook(filePath)

    sheet = wb.active

    # Create Headers in created output file in a row
    sheet['A1'] = 'Name'
    sheet['B1'] = 'Fan Count'
    sheet['C1'] = 'Posts'
    sheet['D1'] = 'Link'

    # Save data retreived from Facebook in next rwo
    sheet['A2'] = responseFromFacebook.get("name")
    sheet['B2'] = responseFromFacebook.get("fan_count")
    sheet['C2'] = json.dumps(responseFromFacebook.get("posts"))
    sheet['D2'] = responseFromFacebook.get("link")

    wb.save(filePath)


# Function to initialize and connect to FacebookGraphAPI
def connectToFacebook():
    # Call function to get input data
    values = getInputData()

    pageId = values.get("pageId")
    # accessToken = values.get("accessToken")

    token = values.get("accessToken")
    graph = facebook.GraphAPI(token)
    # fields = ['first_name', 'location{location}','email','link']
    profile = graph.get_object(pageId, fields='name,fan_count,posts,link')
    # return desired fields
    # print(json.dumps(profile, indent=4))

    return profile


def main():

    # Call function to import all keywords
    getSustainabilityKeywords()

    createOutputFile()


if __name__ == '__main__':
    main()
