# Write a Python Lambda Function Which Gives Tuple Of Max & Min From a List.

max_min = lambda lst: (max(lst), min(lst))

print("Please Enter a Sequence Of Numbers Separated By Spaces : ", end = "")
numbers = [int(i) for i in input().split()]

if len(numbers) < 2:
    print("Please Enter At Least Two Numbers To Find Maximum And Minimum")
else:
    result = max_min(numbers)
    print(f"Tuple Of Maximum And Minimum Is : {result}")
    print(f"Maximum Number Is : {result[0]}")
    print(f"Minimum Number Is : {result[1]}")