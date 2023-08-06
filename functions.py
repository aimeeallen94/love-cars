def print_cars():
     user_input = input("Please enter a car make: ")
     for car in cars:
         if user_input in car:
             print(car)

print_cars()