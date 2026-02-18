# Write a Python Program To Create a To-Do List Manager Where Users Can Add, View & Remove Tasks (Use List For Storing Tasks).

n = int(input("Please Enter The Number Of Tasks You Want To Add : "))
tasks = []

for i in range(n):
    task = input("Please Enter The Task : ")
    tasks.append(task)

print()
while True:
    print("To-Do List Manager Menu :")
    print("(1) - View Tasks")
    print("(2) - Remove Task")
    print("(3) - Add Task")
    print("(4) - Exit To-Do List Manager")

    choice = input("Please Enter Your Choice (1 To 4) : ")

    if choice == '1':
        print()
        print("Your To-Do List Is As Follows : ")
        print(tasks)
        print()

    elif choice == '2':
        print()
        remove_index = int(input("Please Enter The Task Number To Remove : "))

        if 1 <= remove_index <= len(tasks):
            removed_task = tasks.pop(remove_index - 1)
            print("Task '{}' Removed Successfully".format(removed_task))
        else:
            print("Invalid Task Number")
        print()

    elif choice == '3':
        print()
        new_task = input("Please Enter The New Task To Add : ")
        tasks.append(new_task)
        print("Task '{}' Added Successfully".format(new_task))
        print()

    elif choice == '4':
        print()
        print("Program Terminated Successfully")
        break

    else:
        print()
        print("Invalid Choice Program Is Shutting Down")
        print("Program Terminated Successfully")
        break