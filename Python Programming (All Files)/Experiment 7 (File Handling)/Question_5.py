# Write a Python Program To Create Multiple Suitable Exceptions For a File Handling Program.

try:
    file_name = input("Enter The File Name To Read : ")
    with open(file_name, 'r') as file:
        content = file.read()
        print("File Contents :")
        print(content)

except FileNotFoundError:
    print("Error : The File You Are Trying To Read Does Not Exist.")
except PermissionError:
    print("Error : You Do Not Have Permission To Read This File.")
except Exception as e:
    print(f"An Unexpected Error Occurred : {e}")
try:
    file_name = input("Enter The File Name To Write : ")
    with open(file_name, 'w') as file:
        data = input("Enter The Data To Write To The File : ")
        file.write(data)
        print("Data Written To The File Successfully.")
except PermissionError:
    print("Error : You Do Not Have Permission To Write To This File.")
except Exception as e:
    print(f"An Unexpected Error Occurred : {e}")
try:
    file_name = input("Enter The File Name To Append : ")
    with open(file_name, 'a') as file:
        data = input("Enter The Data To Append To The File : ")
        file.write(data)
        print("Data Appended To The File Successfully.")
except PermissionError:
    print("Error : You Do Not Have Permission To Append To This File.")
except Exception as e:
    print(f"An Unexpected Error Occurred : {e}")