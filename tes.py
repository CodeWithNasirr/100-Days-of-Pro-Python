

import os
import json

file_name='xyz.json'


def load_task():
    if os.path.exists(file_name):
        with open(file_name,'r')as f:
            return json.load(f)
    return []


def save_task(tasks):
    with open(file_name,'w')as f:
        json.dump(tasks,f,indent=4)

def add_task(tasks,task):
    tasks.append({'task':task,"Completed":False})
    save_task(tasks)

def view_task(index):
    tasks=load_task()
    if 0<=index < len(tasks):
        print(f"Task {index + 1} : {tasks[index]}")
    else:
        print("No Records Found")

def main():
    tasks=load_task()
    print("**********************Welcome To The Todo-List of 2025**********************")
    user=input('Enter What You Want To do :\n1-ADD\n2-View\n3-Edit\n4-Delete\n5-Exit\n')

    if user == '1':
        task=input("Enter What You Want to add Your Task: ")
        add_task(tasks,task)
     
    elif user=='2':
        print(f"Total Task {len(load_task())}")
        index=int(input("Enter Your task Number:"))-1
        view_task(index)

if __name__=="__main__":
    main()