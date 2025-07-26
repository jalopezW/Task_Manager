from services.API_Response import gemini_response
from datetime import datetime
import os
import json
import csv
# extensions:
# put this on git and use vscode: Complete!
# MOST IMPORTANT CHECKPOINT: IMPROVE LOGIC FOR CSV FILE!!!
# soothing music: NEXT
# view tasks that are completed: NEXT
# database to store tasks offline to complete: NEXT 
# take in multiple tasks at once by parsing string and splitting at comma: NEXT!
# port this project over to github: Complete!
# store tasks in a csv file containing the following: completed, uncompleted, priority: NEXT

def read_tasks():
    # second parameter for open defaults to "r" which means to read the file
    with open("user_tasks.csv") as csv_tasks:
        for task in csv_tasks:
            print(task)
    csv_tasks.close()

    # test out how the tasks are appended to the task list
def write_tasks(new_user_task: str):
        # the second parameter "a" appends a task to the end of the file
        # if we were to use write/"w" it would overwrite anything inside of the file
    with open("user_tasks.csv", "a") as writing_task:
        writing_task.write(new_user_task)
    writing_task.close()

def delete_task(task_to_del: str):
    with open("user_tasks.csv", "w") as user_tasks:
        for task in user_tasks:
            if task == task_to_del:
                user_tasks.remove(task)
    user_tasks.close()

def main():
    if not os.path.exists("user_tasks.csv"):
        with open("user_tasks.csv", "w") as f:
            pass
    print("Welcome to your AI To-Do List Manager!")
    print("Please enter your name below or type \"exit\" to exit the task manager.")
    user_name = input("").capitalize()
    if "Exit" in user_name:
        print("Now closing task manager...")
        print("Goodbye!")
        return

    while True:
        # get rid of the stored tasks list????
        if not read_tasks():
            print(f"Hi {user_name}. There are currently no tasks to complete.")
            new_task = input("Please enter a task here: ")
            write_tasks(new_task)
        else:
            print("These are all the current tasks you have to complete!")
            saved_tasks = read_tasks()
            for index, task in enumerate(saved_tasks, 0):
                print(f"Task { index + 1 }: { task }")
            # task_index = 0
            # while task_index < len(stored_tasks):
            #     print(f"Task {task_index + 1}:", stored_tasks[task_index])
            #     task +=1
        print()
        print("Would you like to add, delete, get AI suggestions to complete your task(s), view your tasks, or exit the program?")
        print("Enter 1 to add a task")
        print("Enter 2 to delete a task")
        print("Enter 3 to get AI suggestions")
        print("Enter 4 to view your tasks")
        print("Enter 5 to exit the Task Manager")
        # lower is absolute unnecessary, but, in case of future, might be helpful
        user_decision = input("Please input your decision here: ").lower()

        if "1" in user_decision:
            user_adding_task = input("Please input your task: ")
            write_tasks(user_adding_task)
            print()
        # IMPLEMENT A WAY TO GET RID OF A SPECIFIC TASK IN THE CSV FILE
        elif "2" in user_decision:
            print("Please enter the exact task you would like to erase from the task list.")
            user_deleting_task = input("Do so here: ")
            # this line below is for the extension of viewing already completed tasks
            # task_to_delete = stored_tasks.index(user_deleting_task)
            # stored_tasks.pop(task_to_delete) # pop takes the index of the element u want to delete
            # put a try and else block here if the task is not found within the task list
            delete_task(user_deleting_task)
            print()
        elif "3" in user_decision:
            print("You may get suggestions from chatGPT's AI of how to complete your tasks, how to schedule your tasks, and etc.\n")
            print("For the best responses from the AI, give as much detail as possible for what you plan to do.")
            user_decision_for_ai = input("Please input your instructions here for the AI to utilize: ")
            # POSSIBLY CHANGE THE FUNCTION PARAMETER TAKING IN THE FUNCTION BC THE FUNCTION ONLY PRINTS ALL THE TASKS IN THE CSV FILE
            ai_response = gemini_response(read_tasks(), user_decision_for_ai)
            print()
            print(ai_response)
            print()
        elif "5" in user_decision:
            print(f"Have a great day {user_name}!")
            break
        elif "4" in user_decision:
            # POSSIBLY JUST LIST ALL TASKS AND PROMPT THE USER IF THEY WOULD LIKE TO EDIT THEIR TASKS
            continue
        else:
            print("Please input a valid command")
            print()

if __name__ == "__main__":
    main()