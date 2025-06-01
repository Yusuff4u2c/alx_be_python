# daily_reminder.py

# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority
match priority:
    case "high":
        message = ("Reminder: ", task, "is a high priority task")
    case "medium":
        message = ("Note: ", task, "is a medium priority task")
    case "low":
        message = ("Note: ", task, "is a low priority task")
    

# If the task is time-sensitive, add extra emphasis
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ("medium", "low"):
        message += ". Consider completing it when you have free time."

        
print(message)
