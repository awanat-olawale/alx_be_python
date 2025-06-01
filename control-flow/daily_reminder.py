#A Python script that uses conditional statements, Match Case, and loops to remind the user
# about a single, priority task for the day based on time sensitivity.

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high priority task. Try completing it as soon as possible")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that should be executed today.")
        else:
            print(f"{task} is a medium priority task. Do find tme to complete it today")
    case "low":
        if time_bound != "yes":
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"{task} is a low priority task but don't forget the deadline.")
    case _ :
        print("Invalid input")
