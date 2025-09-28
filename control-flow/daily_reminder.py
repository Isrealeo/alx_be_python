task = input("What task do you want to be reminded of daily? ")
priority = input("Is this task a high, medium or low priotity task ? ")
time_bound = input("Is this task time-bound? (yes/no) ")
match priority.lower():
    case "high":if time_bound.lower() == "yes":
            print(f"{task} is a high priority task that requires immediate attention today")
        else:
            print(f"note: {task}. consider completeing it when you have free time.")
    case "medium":if time_bound.lower() == "yes":
            print(f"{task} is a medium priority task that should be completed today.")
        else:
            print(f"note: {task}. consider completing it when you have free time.")
    case "low":print(f"note: {task} is of low priority take all the time.")
    case _:print("Invalid priority level. Please enter high, medium, or low.")
    