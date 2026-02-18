# Write a Python Function To Create 2 Lists & Generate a Dictionary With Keys From First List & Values From Second List.

def create_dict_from_lists(keys_list, values_list):
    return dict(zip(keys_list, values_list))

print("Please Enter a Sequence Of Numbers Separated By Spaces (For Keys) : ", end = "")
keys_list = [int(i) for i in input().split()]

print("Please Enter a Sequence Of Numbers Separated By Spaces (For Values) : ", end = "")
values_list = [int(i) for i in input().split()]

result_dict = create_dict_from_lists(keys_list, values_list)
print("Generated Dictionary : {}".format(result_dict))