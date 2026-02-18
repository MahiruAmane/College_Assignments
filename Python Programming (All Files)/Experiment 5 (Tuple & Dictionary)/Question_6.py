# Write a Python Program To Create a Contact Book Where Users Can Store, Search, Update & Delete Contacts (Use Dictionary For Storing Contacts).

n = int(input("Please Enter The Number Of Contacts You Want To Add : "))
contact_book = {}

for i in range(n):
    name = input("Please Enter The Name Of The {} Contact : ".format(i+1))
    phone_number = input("Please Enter The Phone Number Of The Contact : ")
    contact_book[name] = phone_number

print()
while True:
    print("Phone Contact Book Menu :")
    print("(1) - Search Contact")
    print("(2) - Update Contact")
    print("(3) - Delete Contact")
    print("(4) - Display All Contacts")
    print("(5) - Exit Contact Book")

    choice = input("Please Enter Your Choice (1 To 5) : ")

    if choice == '1':
        print()
        search_name = input("Please Enter The Name Of The Contact To Search : ")

        if search_name in contact_book:
            print("Contact Found : {} - {}".format(search_name, contact_book[search_name]))
        else:
            print("Contact Not Found")
        print()

    elif choice == '2':
        print()
        update_name = input("Please Enter The Name Of The Contact To Update : ")

        if update_name in contact_book:
            new_phone_number = input("Please Enter The New Phone Number : ")
            contact_book[update_name] = new_phone_number
            print("Contact Updated Successfully")
        else:
            print("Contact Not Found")
        print()

    elif choice == '3':
        print()
        delete_name = input("Please Enter The Name Of The Contact To Delete : ")

        if delete_name in contact_book:
            del contact_book[delete_name]
            print("Contact Deleted Successfully")
        else:
            print("Contact Not Found")
        print()

    elif choice == '4':
        print()
        print("All Existing Contacts Are As Follows : ")
        for key, value in contact_book.items():
            print("{} - {}".format(key, value))
        print()
    
    elif choice == '5':
        print()
        print("Program Terminated Successfully")
        break

    else:
        print()
        print("Invalid Choice Program Is Shutting Down")
        print("Program Terminated Successfully")
        break