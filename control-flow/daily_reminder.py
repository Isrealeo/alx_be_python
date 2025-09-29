task = input("Enter your task: ")
priority = input ("Priority (high/medium/low): ")
time_bound = input ("Is it time-bound? (yes/no): ") 
match priority:
    case "high":if time_bound == "yes":
        Reminder = "is a high priority task that requires immediate attention today"
            print(f"{Reminder} ")
        else:
            print(f"note: {Task}. consider completeing it when you have free time.")
    case "medium":if time_bound == "yes":
            print(f"{Task} is a medium priority task that should be completed today.")
        else:
            print(f"note: {Task}. consider completing it when you have free time.")
    case "low":print(f"note: {Task} is of low priority take all the time.")
    case _:print("Invalid priority level. Please enter high, medium, or low.")
    
