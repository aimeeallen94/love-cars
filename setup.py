import csv
import gspread
import uuid
import pandas as pd
import numpy as np 
import locale
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


cars = SHEET.worksheet('cars').get_all_values()


"""
Targeting each column in the spreadsheet to access for data analysis in future functions 
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

def print_cars():
     user_input = input("Please enter a car make: ")
     for car in cars:
         if user_input in car:
             print(car)

#print_cars()

def print_num_fuel():
    fuel_list = []
    fuel_user_input = input('Which fuel type would you like to count?')
    for car in cars:
        if "Gasoline" in car:
            fuel_list.append(car)
    
    print(len(fuel_list))

#print_num_fuel()

def print_body_type():
#    sedan_body_type = []
#    suv_body_type = []
#    convertible_body_type = []
#    truck_body_type = []
#    hatchback_body_type = []
#    coupe_body_type = []
#     wagon_body_type = []
#   minivan_body_type = []
    body_type_input = input('Which body type would you like to count?')
#    for car in cars:
#        if body_type_input == 'Sedan' in car:
#            sedan_body_type.append(car)
#            print(len(sedan_body_type))
#        elif 'SUV' in car:
#            suv_body_type.append(car)
#            print(len(suv_body_type))
#        elif 'Convertible' in car:
#            convertible_body_type.append(car)
#            print(len(convertible_body_type))
#        elif 'Truck' in car:
#            truck_body_type.append(car)
#            print(len(truck_body_type))
#        elif 'Hatchback' in car:
#            hatchback_body_type.append(car)
#            print(len(hatchback_body_type))
#        elif 'Coupe' in car:
#            coupe_body_type.append(car)
#            print(len(coupe_body_type))
#        elif 'Wagon' in car:
#           wagon_body_type.append(car)
#            print(len(wagon_body_type))
#        elif 'Minivan' in car:
#            minivan_body_type.append(car)
#            print(len(minivan_body_type))
#    print(body_type)
    if body_type_input == 'SUV':
        SUV_count = body_type.count('SUV')
        print(F'There were ${SUV_count} cars with the body type of an SUV')
    if body_type_input == 'Sedan':
        sedan_count = body_type.count('Sedan')   
        print(body_type.count('Sedan'))
    if body_type_input == 'Truck':
        print(body_type.count('Truck'))
    print(body_type.count('Wagon'))
    print(body_type.count('Minivan'))   
    print(body_type.count('Coupe'))                        
    print(body_type.count('Convertible'))
    print(body_type.count('Hatchback'))

print_body_type()

def calculate_average_max_min_cost():
    """
    Function to display the average cost of a car in 2023 and at the lowest and highest cost of a car.
    """
    max_min_average_input = input('Would you like to find out the maximum, minimum or average cost of a car in 2023?')

    # Removing first row in Price column to remove the word 'Price' from list to allow data cleaning
    cost.pop(0)
    
    #Removing commas in price and creating a new list of these numbers
    no_comma_cost = []
    for num in cost:
        new_num = num.replace(',','')
        no_comma_cost.append(new_num)

    # Converting list to integers to for data manipulation
    cost_list = []    
    for num in no_comma_cost:
        no_comma = int(num)
        cost_list.append(no_comma)


    average = np.mean(cost_list)
    minimum = np.min(cost_list)
    maximum = np.max(cost_list)

    if max_min_average_input == 'Average':
        print(F'The average cost of a car in 2023 is ${round(average)}')

    elif max_min_average_input == 'Minimum':
        print(F'The lowest price of a car in 2023 is ${minimum}.')

    elif max_min_average_input == 'Maximum':
        print(F'The highest price of a car in 2023 is ${maximum}.')

#calculate_average_max_min_cost()



#def creating_uuid():
#    """
#    Creating unique identifier for each row entry in spreadsheet
#    """
#    cars = SHEET.worksheet('cars').get_all_values()


#    for row, col in enumerate(cars):
#        id = uuid.uuid1()
#        cars.update_cell(row + 1, 1, str(id))
#    print(cars)

#creating_uuid()