import csv
import gspread
import pandas as pd
import numpy as np 
from google.oauth2.service_account import Credentials
from functions import *

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_cars_2023')

cars = SHEET.worksheet('cars').get_all_values()

"""
Targeting each column in the spreadsheet to access in future functions. 
"""

car_make = SHEET.worksheet('cars').col_values(1)
model = SHEET.worksheet('cars').col_values(2)
year = SHEET.worksheet('cars').col_values(3)
body_type = SHEET.worksheet('cars').col_values(4)
colour = SHEET.worksheet('cars').col_values(5)
fuel_type = SHEET.worksheet('cars').col_values(6)        
transmission_type = SHEET.worksheet('cars').col_values(7)
top_speed = SHEET.worksheet('cars').col_values(8)
cost = SHEET.worksheet('cars').col_values(9)      
rating = SHEET.worksheet('cars').col_values(10)
sales = SHEET.worksheet('cars').col_values(11)
headings = SHEET.worksheet('cars').row_values(1)   

def selecting_questions():
    print("Hello! Welcome to Cars 2023 info session! \n")
    print('We have a range of questions you can get the answer of here:') 
    print('1 - Car Model Information') 
    print('2 - Transmission Type Information') 
    print('3 - Body Type Information and Stats')
    print('4 - Car Cost Information') 
    print('5 - Car Sales Information')
    print('6 - Counting Number of Models for Desired Brands')
    print("Don't worry you can make your way through all if you are interested!")
 
    question_selection_input = input('Which question would you like to get the answer of? ')
    if question_selection_input == '1':
        print_car_info()
    elif question_selection_input == '2':
        print_num_transmission_type()
    elif question_selection_input == '3':
        print_body_type() 
    elif question_selection_input == '4':
        calculate_average_max_min_cost()
    elif question_selection_input == '5':
        car_sales_information()
    elif question_selection_input == '5':
        counting_num_of_models_in_brand()
    else:
        print('Please enter a valid selection: 1,2,3,4,5')
        selecting_questions()
    
selecting_questions()