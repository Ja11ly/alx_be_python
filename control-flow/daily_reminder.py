# daily_reminder.py

# Get user input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the input with match-case and conditionals
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        print("Invalid priority entered. Please use: high, medium, or low.")
        exit()

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ". Consider scheduling it soon."

# Display the final reminder
print("\n" + reminder)
