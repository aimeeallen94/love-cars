def print_cars():
     user_input = input("Please enter a car make: ")
     for car in cars:
         if user_input in car:
             print(car)

print_cars()


def creating_uuid():
    """    
    Creating unique identifier for each row entry in spreadsheet
    """
    unique_id = SHEET.worksheet('cars').col_values(12)
    
    for row, col in enumerate(cars):
        id = str(uuid.uuid1())
        cars.update_cells(1, 12 , id)
    print(cars)

creating_uuid()


#Functions in code 
def print_cars()
def print_num_fuel() #need to change this as only one fuel type 
def print_body_type()
def calculate_average_max_min_cost()
def calculate_total_car_sales()
def print_info_based_on_model() #need to change the format that prints out of this to allow for better formatting



