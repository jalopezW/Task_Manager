from services.API_Response import gemini_response
from datetime import datetime
import os
import json
import csv


def read_tasks() -> list:
    """
    This function reads and prints each task within the user_tasks.csv file.
    """
    user_tasks = list()
    with open("user_tasks.csv") as csv_tasks:
        reader = csv.reader(csv_tasks)
        for task in csv_tasks:
                user_tasks.append(task)
    csv_tasks.close()
    return user_tasks

def write_tasks(new_user_task: str):
    """
    This function takes a task input fromm the user and writes the given data to the user_tasks.csv file.
    """
    with open("user_tasks.csv", "a") as writing_task:
        if "," != new_user_task[-1]:
            new_user_task += ","
            writing_task.write(new_user_task)
        elif "," == new_user_task[-1]:
            writing_task.write(new_user_task)
    
    writing_task.close()

def delete_task(task_to_del: str):
    """
    This function deletes a user inputted task from the user_tasks.csv file.
    """
    with open("user_tasks.csv", "r") as all_tasks:
        current_line = all_tasks.readline().strip()
    all_tasks.close()
    if not current_line:
        return
    tasks = [task.strip() for task in current_line.split(",") if task.strip()]
    updated_tasks = [task for task in tasks if task.lower() != task_to_del.strip().lower()]

    with open("user_tasks.csv", "w") as user_tasks_file:
        if updated_tasks:
            user_tasks_file.write(",".join(updated_tasks))
        else:
            user_tasks_file.write("")

    user_tasks_file.close()

def main():
    if not os.path.exists("user_tasks.csv"):
        with open("user_tasks.csv", "w") as f:
            pass
    print("Welcome to your AI To-Do List Manager!")
    print("Please enter your name below or type \"Exit\" to exit the task manager.")
    user_name = input("").capitalize()
    if "Exit" in user_name:
        print("Now closing task manager...")
        print("Goodbye!")
        return

    while True:
        user_amount_of_tasks = read_tasks()
        if len(user_amount_of_tasks) == 0:
            print(f"\nHi {user_name}! There are currently no tasks to complete.")
            new_task = input("Please enter a task here or input \"Exit\" to quit: ")
            if new_task.capitalize() == "Exit":
                    print("Now closing task manager...")
                    print("Goodbye!")
                    return
            write_tasks(new_task)
        else:

            print("\nThese are all the current tasks you have to complete!")
            saved_tasks: list = read_tasks()
            # the list comprehension checks for the single line of tasks in the csv file 
            # then cleans the tasks and displays a more presentable output to the user
            cleaned_up_tasks = [task.strip() for task in saved_tasks[0].split(",") if task.strip()]
            for index, task in enumerate(cleaned_up_tasks, 1):
                print(f"Task {index}: {task.capitalize()}")

        print()
        print("Would you like to add, delete, get AI suggestions to complete your task(s), view your tasks, or exit the program?")
        print("Enter 1 to add a task")
        print("Enter 2 to delete a task")
        print("Enter 3 to get AI suggestions")
        print("Enter 4 to view your tasks")
        print("Enter 5 to delete all tasks")
        print("Enter 6 to exit the Task Manager")
        user_decision = input("Please input your decision here: ").lower()

        if user_decision == "1":
            print("You may input a singular task or multiple at once, but separated with a comma.")
            user_adding_task = input("Add any tasks here: ")
            write_tasks(user_adding_task)
            print()
        elif user_decision == "2":
            print("Please enter the exact task you would like to erase from the task list.")
            user_deleting_task = input("Do so here: ")
            # put a try and else block here if the task is not found within the task list
            delete_task(user_deleting_task)
            print()
        elif user_decision == "3":
            print("You may get suggestions from chatGPT's AI of how to complete your tasks, how to schedule your tasks, and etc.\n")
            print("For the best responses from the AI, give as much detail as possible for what you plan to do.")
            user_decision_for_ai = input("Please input your instructions here for the AI to utilize: ")
            ai_response = gemini_response(read_tasks(), user_decision_for_ai)
            print()
            print(ai_response)
            print()
        elif user_decision == "4":
            # lists all tasks and asks user if they would like to do anything with them
            continue
        elif user_decision == "5":
            print("WARNING!\nYou are about to clear all your tasks.\nAre you sure you want to proceed?\n")
            deleting_decision = input("Enter Y/N: ").upper()
            if deleting_decision == "Y":
                with open("user_tasks.csv", "w"):
                    pass
            else:
                print("Your tasks have not been deleted!\n")
                continue
        elif user_decision == "6":
            print(f"Have a great day {user_name}!")
            break
        else:
            print()
            print("Please input a valid command.")
            print()

if __name__ == "__main__":
    main()