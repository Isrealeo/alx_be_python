from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Todays date is: ", current_date.strftime("%Y-%m-%d"))
    return current_date
    
def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    print("The date after", days_to_add, "days will be:", future_date.strftime("%Y-%m-%d"))
     

current_date = display_current_datetime()

future_days = int(input("Enter the number of days to add to the current date: "))

calcuate_future_date =  (current_date, future_days) 
  
    
    
    
