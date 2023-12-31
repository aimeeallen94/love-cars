import csv
import gspread
import pandas as pd
import numpy as np
from google.oauth2.service_account import Credentials

"""
Connecting my Googlesheet to this workspace using Google APIs
"""
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


class Car:
    """
    Class representing car within the spreadhseet
    """
    global cars

    def __init__(self, car_model):
        for car in cars:
            if car_model == car[1]:
                self.make = car[0]
                self.car_year = car[2]
                self.car_body_type = car[3]
                self.fuel = car[5]
                self.transmission = car[6]
                self.max_speed = car[7]
                self.car_price = car[8]
                self.sales_figures = car[10]
                self.car_model = car_model

    def display_information(self):
        """
        Creating format for car info to print in
        """
        print(F'Make = {self.make}\n')
        print(F'Model = {self.car_model}\n')
        print(F'Year = {self.car_year}\n')
        print(F'Body Type = {self.car_body_type}\n')
        print(F'Fuel = {self.fuel}\n')
        print(F'Max Speed = {self.max_speed}\n')
        print(F'Price = {self.car_price}\n')
        print(F'Sales = {self.sales_figures}\n')


def print_car_info():
    """
    Allows user to input desired car model and for console
    to return information about that car in a dictionary format
    with the heading row.
    """
    car_model = input("Please enter a car model(as seen on spreadsheet): \n")

    if(car_model in SHEET.worksheet('cars').col_values(2)):
        my_car = Car(car_model)
        my_car.display_information()
    else:
        print('Sorry, car not found')

    print('********************************************')
    print('')
    selecting_questions()


def calculate_percentage_transmission():
    """
    Function to calculate the percentage of each transmission
    type of the data set.
    """

    automatic = transmission_type.count('Automatic')
    cvt = transmission_type.count('CVT')
    manual = transmission_type.count('Manual')
    # transmission length -1 to remove the header from this column length
    transmission_length = (len(transmission_type)) - 1

    percentage_question = input('Which tranmission would you like to see the percentange of: Automatic, Manual or CVT? \n')
    percentage_question = percentage_question.lower()

    if percentage_question == 'automatic':
        automatic_percentage = (automatic / transmission_length) * 100
        print(F'Automatic = {int(automatic_percentage)}% of this dataset \n')
    elif percentage_question == 'cvt':
        cvt_percentage = (cvt / transmission_length) * 100
        print(F'CVT = {int(cvt_percentage)}% of this dataset\n')
    elif percentage_question == 'manual':
        manual_percentage = (manual / transmission_length) * 100
        print(F'Manual = {int(manual_percentage)}% of this dataset\n')
    else:
        print('INVALID DATA. Please enter: Automatic, CVT or Manual.\n')
        calculate_percentage_transmission()

    print('********************************************')
    print('')
    selecting_questions()


def print_num_transmission_type():
    """
    Funciton to return the count of desired transmission
    type of car.
    """
    transmission_input = input('Enter a transmission type to see count: \n')

    if transmission_input == 'a=Automatic':
        automatic = transmission_type.count('Automatic')
        print(F'There are {automatic} automatic cars in this dataset \n')
    elif transmission_input == 'CVT':
        cvt = transmission_type.count('CVT')
        print(F'There are {cvt} CVT cars in this.\n')
    elif transmission_input == 'Manual':
        manual = transmission_type.count('Manual')
        print(F'There is {manual} manual cars in this dataset.\n')
    else:
        print('INVALID DATA. Please enter: Automatic, CVT or Manual.\n')
        print_num_transmission_type()

    print('********************************************')
    print('')
    calculate_percentage_transmission()


def print_body_type():
    """
    Function to print out count of desired body type of car.
    """
    print('Options: SUV, Sedan, Truck, Wagon, Minivan, Coupe, Convertible, Hatchback')

    body_type_input = input('Which body type would you like to count? \n')
    body_type_input = body_type_input.lower()

    if body_type_input == 'suv':
        SUV_count = body_type.count('SUV')
        print(F'There were {SUV_count} Suv cars. \n')
    elif body_type_input == 'sedan':
        sedan_count = body_type.count('Sedan')
        print(F'There were {sedan_count} Sedan cars. \n')
    elif body_type_input == 'truck':
        truck_count = body_type.count('Truck')
        print(F'There were {truck_count} Truck cars \n')
    elif body_type_input == 'wagon':
        wagon_count = body_type.count('Wagon')
        print(F'There were {wagon_count} Wagon cars. \n')
    elif body_type_input == 'minivan':
        minivan_count = body_type.count('Minivan')
        print(F'There were {minivan_count} Minivans. \n')
    elif body_type_input == 'coupe':
        coupe_count = body_type.count('Coupe')
        print(F'There were {coupe_count} Coupe cars. \n')
    elif body_type_input == 'convertible':
        convertible_count = body_type.count('Convertible')
        print(F'There were {convertible_count} Covvertible cars. \n')
    elif body_type_input == 'hatchback':
        hatchback_count = body_type.count('Hatchback')
        print(F'There were {hatchback_count} Hatchback cars. \n')
    else:
        print('INVALID DATA. Please enter: SUV, Sedan, Truck, Wagon, Minivan,Coupe, Convertible or Hatchback.\n')
        print_body_type()

    print('********************************************')
    print('')
    selecting_questions()


def calculate_average_max_min_cost():
    """
    Function to display the average cost of a car in 2023
    and at the lowest and highest cost of a car.
    """
    max_min_average_input = input('Would you like to find the maximum, minimum or average cost of a car in this dataset? \n')
    max_min_average_input = max_min_average_input.lower()

    # Removing first row in Price column to remove the word 'Price' from list
    # to allow data cleaning
    cost.pop(0)

    # Removing commas in price and creating a new list of these numbers
    no_comma_cost = []
    for num in cost:
        new_num = num.replace(',', '')
        no_comma_cost.append(new_num)

    # Converting list to integers to for data manipulation
    cost_list = []
    for num in no_comma_cost:
        no_comma = int(num)
        cost_list.append(no_comma)

    average = np.mean(cost_list)
    minimum = np.min(cost_list)
    maximum = np.max(cost_list)

    if max_min_average_input == 'average':
        print(F'The average cost of a car in 2023 is ${round(average)}\n')
    elif max_min_average_input == 'minimum':
        print(F'The lowest price of a car in 2023 is ${minimum}.\n')
    elif max_min_average_input == 'maximum':
        print(F'The highest price of a car in 2023 is ${maximum}.\n')
    else:
        print('INVALID DATA. Please enter: Maximum, Minimum or Average.')
        calculate_average_max_min_cost()

    print('********************************************')
    print('')
    selecting_questions()


def car_sales_information():
    """
    Function to display total car sales in 2023 so far
    """
    sales_input = input('Enter T for total sales, L for lowest, H for highest or A for average car sales, of for all enter ALL \n')
    sales_input = sales_input.upper()

    """
    Removing heading from sales list to allow for list to be converted
    into integers.
    """
    sales.pop(0)

    # Removing commas from sales values so they can be converted to integers
    no_comma_sales = []
    for num in sales:
        new_sale_num = num.replace(',', '')
        no_comma_sales.append(new_sale_num)

    # Converting list of strings to integers
    sales_list = []
    for num in no_comma_sales:
        no_comma_sale = int(num)
        sales_list.append(no_comma_sale)

    total_car_sales = np.sum(sales_list)
    lowest_car_sales = np.min(sales_list)
    highest_car_sales = np.max(sales_list)
    average_car_sales = np.mean(sales_list)

    if sales_input == 'T':
        print(F"In this dataset {total_car_sales} cars have been sold\n")
    elif sales_input == 'L':
        print(F'Lowest sales are {lowest_car_sales} for Mercedes S-Class \n')
    elif sales_input == 'H':
        print(F'Highest sales are {highest_car_sales} for Nissan Sentra & Ford Escape.\n')
    elif sales_input == 'A':
        print(F'Average car sales are {round(average_car_sales)}.\n')
    elif sales_input == 'ALL':
        print(F'In this dataset there has been {total_car_sales} cars sold. \n lowest car sales are {lowest_car_sales} for Mercedes S-Class, \n highest car sales are {highest_car_sales} for the Nissan Sentra \n and Ford Escape and average car sales are {round(average_car_sales)}.\n')
    else:
        print("INVALID DATA. Please enter: T, L, H, A or ALL. ")
        car_sales_information()

    print('********************************************')
    print('')
    selecting_questions()


def counting_num_of_models_in_brand():
    """
    Function to count the number of specified car makes
    per brand
    """
    brand_input = input('Which brand would you like to count? \n')

    # Removing header from car brand list
    car_make.pop(0)

    df = pd.value_counts(np.array(car_make))
    print(F"There are {df.loc[brand_input]} {brand_input} models \n")

    print('********************************************')
    print('')
    selecting_questions()


def exit_program():
    """
    Function to allow user to exit program when they
    have gotten answers to all questions they want
    """
    confirm_exit = input('Are you sure you wish to exit? Y/N')
    confirm_exit = confirm_exit.upper()

    if confirm_exit == 'Y':
        print('To begin again please press Run Program above the terminal')
        exit()
    elif confirm_exit == 'N':
        selecting_questions()
    else:
        print('INVALID DATA, Please enter: Y or N')
        exit_program()


def request_help():
    help_input = input('Which question would you like further information on? ')

    if help_input == '1':
        print('This option allows you to enter a car model from the spreadsheet and returns information in a clearly read format in relation to the specified car, for example, Model = Q7, Make = Audi')
    elif help_input == '2':
        print('This option allows you to enter a desired transmission type: CVT, Manual or Gasoline and the terminal returns the number of cars with that transmission. There is a bonus question which allows you to see the percentage value of any of the transmission types also.')
    elif help_input == '3':
        print('This option allows you to enter a desired car body time and the3 console will return a count of the body type entered. Options are: SUV, Sedan, Coupe, Convertible, Hatchback, Minivan, Truck or Wagon')
    elif help_input == '4':
        print('This option provides you with the choice of displaying either the maximum, minimum or average car cost within this dataset by entering either: Maximum, Minimum or Average.')
    elif help_input == '5':
        print('This options allows the user to display the total, highest, lowest or average car sales within the dataset. This option also displays the names of the cars with the maximum and minimum sales. Alternatively, you can pick to display all four figures in one statement. Options are: H for highest, L for loweset, T for total, A for average and ALL to display all.')
    elif help_input == '6':
        print('This options allows you to enter a desired car brand and the terminal will display a count of models from the specified car brand.')
    else:
        print('INVALID INPUT: Please enter: 1, 2, 3, 4, 5 or 6.')

    print('********************************************')
    print('')
    selecting_questions()


def selecting_questions():
    """
    Function to alllow users to select which question
    they would like to get the answer of
    """

    print("Hello! Welcome to Cars 2023 info session! \n")
    print('We have a range of questions you can get the answer of here:')
    print('1 - Car Model Information')
    print('2 - Transmission Type Information')
    print('3 - Body Type Information and Stats')
    print('4 - Car Cost Information')
    print('5 - Car Sales Information')
    print('6 - Counting Number of Models for Desired Brands')
    print('Exit - Exit app, I have found out all I need!')
    print('Help - if you need some help!')
    print("You can make your way through all if you are interested!")

    question_selection_input = input('Which question do you choose or End Programme? \n')
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
    elif question_selection_input == '6':
        counting_num_of_models_in_brand()
    elif question_selection_input == 'Exit':
        exit_program()
    elif question_selection_input == 'Help':
        request_help()
    else:
        print('INVALID DATA. Please enter: 1, 2, 3, 4, 5, 6 or Exit')
        selecting_questions()

selecting_questions()
