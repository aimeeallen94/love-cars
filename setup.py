import csv
import gspread
import uuid
import pandas as pd
import numpy as np 
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

#df = pd.DataFrame.from_dict(cars)


def print_cars():
    user_input = input("Please enter a car make: ")
    for car in cars:
        if user_input in car:
            result1 = headings
            result2 = car
            dictionary = dict(zip(result1, result2))
            print(dictionary)

print_cars()

def calculate_percentage_transmission():
    """
    Function to calculate the percentage of each transmission type of the data set. 
    """

    automatic = transmission_type.count('Automatic')
    cvt = transmission_type.count('CVT')
    manual = transmission_type.count('Manual')
    # transmission length -1 to remove the header from this column length
    transmission_length = (len(transmission_type)) - 1

    percentage_question = input('Which tranmission would you like to calculate the percentage of? ')

    if percentage_question == 'Automatic':
        automatic_percentage = (automatic / transmission_length) * 100
        print(F'Automatic cars take up {int(automatic_percentage)}% of this dataset')
    if percentage_question == 'CVT':
        cvt_percentage = (cvt / transmission_length) * 100
        print(F'CVT cars take up {int(cvt_percentage)}% of this dataset')
    if percentage_question == 'Manual':
        manual_percentage = (manual / transmission_length) * 100
        print(F'Manual cars take up {int(manual_percentage)}% of this dataset')
    else:
        print('Please enter a valid transmission type: Automatic, CVT, Manual.')

def print_num_transmission_type():
    """
    Funciton to return the count of desired transmission type of car.
    """
    transmission_input = input('Which transmission type would you like to count? ')
    
    if transmission_input == 'Automatic':
        automatic = transmission_type.count('Automatic')
        print(F'There are {automatic} cars in 2023 with an automatic transmission.')
    if transmission_input == 'CVT':
        cvt = transmission_type.count('CVT')
        print(F'There are {cvt} cars in 2023 with a CVT transmission.')
    if transmission_input == 'Manual':
        manual = transmission_type.count('Manual')
        print(F'There is {manual} car in 2023 with a manual transmission.')
    else:
        print('Please enter valid transmission type: Automatic, CVT or Manual.')
    calculate_percentage_transmission()

#print_num_transmission_type()


def print_body_type():
    """
    Function to print out count of desired body type of car.
    """
    print('Your options are as follows: SUV, Sedan, Truck, Wagon, Minivan, Coupe, Convertible, Hatchback')        
    
    body_type_input = input('Which body type would you like to count? ')  

    if body_type_input == 'SUV':
        SUV_count = body_type.count('SUV')
        print(F'There were {SUV_count} cars with the body type of an SUV')
    if body_type_input == 'Sedan':
        sedan_count = body_type.count('Sedan')               
        print(F'There were {sedan_count} cars with the body type of a Sedan')
    if body_type_input == 'Truck':
        truck_count = body_type.count('Truck')
        print(F'There were {truck_count} cars with the body type of a Truck')
    if body_type_input == 'Wagon':
        wagon_count = body_type.count('Wagon')          
        print(F'There were {wagon_count} cars with the body type of a Wagon')
    if body_type_input == 'Minivan':
        minivan_count = body_type.count('Minivan')            
        print(F'There were {minivan_count} cars with the body type of a Minivan')
    if body_type_input == 'Coupe':
        coupe_count = body_type.count('Coupe')        
        print(F'There were {coupe_count} cars with the body type of a Coupe')
    if body_type_input == 'Convertible':
        convertible_count = body_type.count('Convertible')                        
        print(F'There were {convertible_count} cars with the body type of a Convertible')
    if body_type_input == 'Hatchback':
        hatchback_count = body_type.count('Hatchback')
        print(F'There were {hatchback_count} cars with the body type of a Hatchback')
    else:
        print('Please enter one of the following valid options: SUV, Sedan, Truck, Wagon, Minivan, Coupe, Convertible, Hatchback.')


#print_body_type()

def calculate_average_max_min_cost():
    """
    Function to display th#e average cost of a car in 2023 and at 
    the lowest and highest cost of a car.
    """
    max_min_average_input = input('Would you like to find out the maximum, minimum or average cost of a car in 2023? ')

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
    else:
        print('Please enter a valid option: Maximum, Minimum or Average.')

#calculate_average_max_min_cost()

def calculate_total_car_sales():
    """
    Function to display total car sales in 2023 so far
    """
    sales_input = input('Would you like to know the total number of cars sold this year so far? Y/N ')
    # Removing heading from sales list to allow for list to be converted into integers
    sales.pop(0)

    # Removing commas from sales values so they can be converted to integers
    no_comma_sales = []
    for num in sales:
        new_sale_num = num.replace(',','')
        no_comma_sales.append(new_sale_num)

    # Converting list of strings to integers
    sales_list = []    
    for num in no_comma_sales:
        no_comma_sale = int(num)
        sales_list.append(no_comma_sale)

    total_car_sales = np.sum(sales_list)
    if sales_input == 'Y':
        print(F'In 2023 so far there has been {total_car_sales} cars sold.')
    else:
        print("Let's proceed to the next one!")

#calculate_total_car_sales()

def print_info_based_on_model():
    """
    Function that accepts car name and prints details about the car as a result.
    """
# Removing first entry from model list as this is the heading and does not need analysis
model.pop(0)

#model_input = input('Which model would you like more information on? ')

#for model in cars:
#    if model_input in model:
#        print(model)
    #else:
    #    print('Please enter valid car model as seen on spreadsheet')
    #    break

#print_info_based_on_model()


def selecting_questions():
    print("Hello! Welcome to Cars 2023 info session! \n")
    print('We have a range of questions you can get the answer of here: \n') 
    print('If you would like to find out information based on car model select 1 \n') 
    print('If you would like to find out how many car runs on a specific fuel type select 2 \n') 
    print('If you would like to find out the mininumn, maximum and average car cost select 3 \n') 
    print("Don't worry you can make your way through all if you are interested! \n")
 
    question_selection_input = input('Which question would you like to get the answer of? ')
    if question_selection_input == '1':
        print_cars()
    if question_selection_input == '2':
        print_num_transmission_type()
    if question_selection_input == '3':
        calculate_average_max_min_cost()

#selecting_questions()
