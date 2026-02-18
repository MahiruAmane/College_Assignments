# Write a Python Function To Find The Maximum & Minimum Numbers From a Sequence Of Numbers (Note - Do Not Use Built In Functions)

def find_max_min(numbers):
    
    if len(numbers) < 2:
        print("Please Enter At Least Two Numbers To Find Maximum And Minimum")
        return None, None

    max_num = numbers[0]  
    min_num = numbers[0]  

    for i in numbers:
        if i > max_num:
            max_num = i  
        elif i < min_num:
            min_num = i  
    
    if max_num == min_num:
        print("All Numbers Are Equal")

    return max_num, min_num

print("Please Enter a Sequence Of Numbers Separated By Spaces : ", end = "")
numbers = [int(i) for i in input().split()]

max_number, min_number = find_max_min(numbers)
print(f"Maximum Number Is : {max_number}")
print(f"Minimum Number Is : {min_number}")