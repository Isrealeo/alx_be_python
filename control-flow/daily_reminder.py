Task = input("What task do you want to be reminded of daily? ")
Priority = input("Is this task a high, medium or low priotity task ? ")
Time_Bound = input("Is this task time-bound? (yes/no) ")
match priority.lower():
    case "high":if time_bound.lower() == "yes":
            print(f"{Task} is a high priority task that requires immediate attention today")
        else:
            print(f"note: {Task}. consider completeing it when you have free time.")
    case "medium":if time_bound.lower() == "yes":
            print(f"{Task} is a medium priority task that should be completed today.")
        else:
            print(f"note: {Task}. consider completing it when you have free time.")
    case "low":print(f"note: {Task} is of low priority take all the time.")
    case _:print("Invalid priority level. Please enter high, medium, or low.")
    
