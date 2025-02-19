import os
import csv

def add_lists(activity, date):
    with open("activities.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([activity, date])
    print("Activity added successfully!")

def view_activities():
    if not os.path.exists("activities.csv"):
        print("No activities found.")
        return
    
    with open("activities.csv", "r") as file:
        reader = csv.reader(file)
        activities = list(reader)
        if not activities:
            print("No tasks to do.")
            return
        
        print("\nActivities:")
        for idx, (activity, date) in enumerate(activities, start=1):
            print(f"{idx}. {activity} - {date}")    

def delete_activity(index):
    if not os.path.exists("activities.csv"):
        print("No activities found.")
        return
    
    with open("activities.csv", "r") as file:
        reader = csv.reader(file)
        activities = list(reader)
        if not activities:
            print("No tasks to do.")
            return

    if index < 1 or index > len(activities):
        print("Invalid index.")
        return
    
    del activities[index - 1]
    with open("activities.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(activities)
    print("Activity deleted successfully!")

def main():
    while True:
        print("\nActivity Tracker")
        print("1. Add Activity")
        print("2. View Activities")
        print("3. Delete Activity")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            activity = input("Enter activity: ").lower()
            date = input("Enter date (YYYY-MM-DD): ")
            add_lists(activity, date)
        elif choice == "2":
            view_activities()
        elif choice == "3":
            view_activities()
            index = int(input("Enter index of activity to delete: "))
            delete_activity(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()