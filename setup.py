import csv
import gspread
import uuid
import pandas as pd
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_cars_2023')

"""
Removing duplicates from datasheet to prevent errors during analysis
"""

spreadsheet = SHEET.worksheet('cars').get_all_values()

def targeting_each_column():
    """
    Targeting each column in the spreadsheet to access for data analysis
    """

    if unique_identifier == cars[0]:
        self.car_make = cars[1]
        self.car = cars[2]
        self.year = cars[3]
        self.body_type = cars[4]
        self.colour = cars[5]
        self.fuel_type = cars[6]
        self.transmission_type = cars[7]
        self.top_speed = cars[8]
        self.price = cars[9]
        self.rating = cars[10]
        self.sales = cars[11]


def creating_uuid():
    """
    Creating unique identifier for each row entry in spreadsheet
    """
    sheet = SHEET.worksheet('cars')


    for row, col in enumerate(spreadsheet):
        id = uuid.uuid1()
        sheet.update_cell(row + 1, 1, str(id))
    
# creating_uuid()