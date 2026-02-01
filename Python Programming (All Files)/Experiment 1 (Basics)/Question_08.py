# Write a Python Program To Convert Given Seconds Into Hours, Minutes & Remaining Seconds.

seconds = int(input("Please Enter The Number Of Seconds : "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print("The Conversion Of {} Seconds Is : {} Hours {} Minutes {} Seconds".format(seconds, hours, minutes, remaining_seconds))