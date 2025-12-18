#!/bin/bash

echo
echo "------------------------------------------------------------ FITNESS MANAGEMENT SYSTEM ------------------------------------------------------------"
echo
echo "--------------------------------------------------------- PLEASE ENTER YOUR BASIC DETAILS ---------------------------------------------------------"
echo

echo -n "Please Enter Your Name : "
read name

if [ -z "$name" ]; then
	echo "Please Enter a Valid Name"
	exit 1
fi

echo -n "Please Enter Your Age : "
read age

if [ "$age" -lt 18 ]; then
	echo "Use Of This Software Is Permitted For Individuals Aged 18 And Above"
	exit 1
fi

echo -n "Please Enter Your Gender (Male/Female) : "
read gender

if [[ "$gender" != "Male" && "$gender" != "Female" ]]; then
	echo "Invalid Gender Entered"
	exit 1
fi

echo

echo "What Is Your Baseline Activity Level ? "
echo "(1) Not Very Active - Spend Most Of The Day Sitting (Example - Desk Job)"
echo "(2) Lightly Active - Spend a Good Part Of The Day On Your Feet (Example - Teacher)"
echo "(3) Active - Spend a Good Part Of The Day Doing Some Physical Activity (Example - Food Server)"
echo "(4) Very Active - Spend a Good Part Of The Day Doing Some Heavy Physical Activity (Example - Carpenter)"
echo
echo -n "Please Enter Your Baseline Activity Level : "
read choice

if [[ "$choice" -lt 1 || "$choice" -gt 4 ]]; then
	echo "Please Enter a Valid Choice"
	exit 1
fi

case $choice in
	1)
		activity="Not Very Active"
		;;
	2)
		activity="Lightly Active"
		;;
	3)
		activity="Active"
		;;
	4)
		activity="Very Active"
		''
esac
echo

echo -n "Please Enter Your Height (In Meters) : "
read height

if (( $(echo "$height < 0.5 || $height > 2.5" | bc -l) )); then
        echo "Please Enter a Valid Height"
        exit 1
fi

echo -n "Please Enter Your Weight (In Kilograms) : "
read weight

if (( $(echo "$weight < 10 || $weight > 200" | bc -l) )); then
        echo "Please Enter a Valid Weight"
        exit 1
fi

bmi=$(echo "scale=2; $weight / ($height * $height)" | bc -l)

min_weight=$(echo "scale=2; 18.5 * ($height * $height)" | bc -l)
max_weight=$(echo "scale=2; 24.9 * ($height * $height)" | bc -l)

echo -n "Please Enter Your Goal Weight (In Kilograms) : "
read goal_weight

if (( $(echo "$goal_weight == $weight" | bc -l) )); then
	echo "Your Goal Weight Cannot Be The Same As Your Current Weight"
	exit 1
elif (( $(echo "$goal_weight < $min_weight || $goal_weight > $max_weight" | bc -l) )); then
	echo "Based On Your Height, The Healthy Weight Range Is Between $min_weight Kg And $max_weight Kg"
	exit 1
fi

echo

if (( $(echo "$bmi < 18.5" | bc -l) )); then
	echo "Your Body Mass Index (BMI) Is : $bmi"
	category="Underweight"
	echo "Your Body Mass Index (BMI) Indicates That You Are In The Underweight Category"
elif (( $(echo "$bmi <= 24.9" | bc -l) )); then
	echo "Your Body Mass Index (BMI) Is : $bmi"
	category="Normal"
        echo "Your Body Mass Index (BMI) Indicates That You Are In The Normal Category"
elif (( $(echo "$bmi <= 29.9" | bc -l) )); then
	echo "Your Body Mass Index (BMI) Is : $bmi"
	category="Overweight"
        echo "Your Body Mass Index (BMI) Indicates That You Are In The Overweight Category"
elif (( $(echo "$bmi <= 34.9" | bc -l) )); then
        echo "Your Body Mass Index (BMI) Is : $bmi"
	category="Obesity Class I"
        echo "Your Body Mass Index (BMI) Indicates That You Are In The Obesity Class I Category"
elif (( $(echo "$bmi <= 39.9" | bc -l) )); then
        echo "Your Body Mass Index (BMI) Is : $bmi"
	category="Obesity Class II"
        echo "Your Body Mass Index (BMI) Indicates That You Are In The Obesity Class II Category"
elif (( $(echo "$bmi > 39.9" | bc -l) )); then
        echo "Your Body Mass Index (BMI) Is : $bmi Which Falls Within The Obesity Class III Range"
	echo "Your Body Mass Index Is Extremely High, Please Consult a Doctor"
	exit 1
fi

echo
echo "-------------------------------------------------------------- COMPILING INFORMATION --------------------------------------------------------------"
echo

echo "Name Of The User : $name"
echo "Age Of The User : $age"
echo "Gender Of The User : $gender"
echo "Baseline Activity Level : $activity"
echo "Height Of The User (In Meters) : $height"
echo "Weight Of The User (In Kilograms) : $weight"
echo "Current Body Mass Index (BMI) And Category : $bmi ($category)"
echo
echo "Healthy Weight For Your Height Is Between $min_weight Kg And $max_weight Kg"
echo "You Have Entered The Goal Weight As $goal_weight Kg"

if [[ $(echo "$goal_weight > $weight" | bc -l) -eq 1 && "$category" == "Underweight" ]]; then
    echo "Recommended Weight Goal - Gain Weight"
elif [[ $(echo "$goal_weight < $weight" | bc -l) -eq 1 && ( "$category" == "Obesity Class I" || "$category" == "Obesity Class II" ) ]]; then
    echo "Recommended Weight Goal - Lose Weight"
else
    echo "Recommended Weight Goal - Maintain Weight"
fi

echo
echo "Please Select One Of The Following Goals"
echo "(1) Gain Weight"
echo "(2) Lose Weight"
echo "(3) Maintain Weight"
echo -n "Please Enter Your Goal (Recommended Will Provide Better Results) : "
read goal_choice

if [[ "$goal_choice" -lt 1 || "$goal_choice" -gt 3 ]]; then
        echo "Please Enter a Valid Choice"
        exit 1
fi

case $goal_choice in
	1)
		goal="Gain Weight"
		;;
	2)
		goal="Lose Weight"
		;;
	3)
		goal="Maintain Weight"
		;;
esac

echo
echo "------------------------------------------------------------ EXERCISE  RECOMMENDATIONS ------------------------------------------------------------"
echo

days=0

if [[ $goal_choice -eq 1 ]]; then
    case $choice in
        1) days=4 ;;
        2) days=3 ;;
        3) days=2 ;;
        4) days=1 ;;
    esac
elif [[ $goal_choice -eq 2 ]]; then
    case $choice in
        1) days=6 ;;
        2) days=5 ;;
        3) days=2 ;;
        4) days=3 ;;
    esac
elif [[ $goal_choice -eq 3 ]]; then
    case $choice in
        1) days=5 ;;
        2) days=4 ;;
        3) days=3 ;;
        4) days=2 ;;
    esac
fi

if [[ $days -gt 0 ]]; then
    echo "Your Personalized One Week Exercise Plan Lasting $days Days Is Designed To Help You Make Effective Progress"
fi

echo
echo "Exercises For The Legs Are As Follows : "
echo

squats=0
for ((i = 1; i <= days; i++)); do
        squats=$((squats + 10))
done
echo "Please Complete $squats Squats (2 Sets) Every Day For The Next $days Days"

lunges=0
for ((i = 1; i <= days; i++)); do
        lunges=$((lunges + 4))
done
echo "Please Complete $lunges Lunges Per Leg (3 Sets) Every Day For The Next $days Days"

deadlift=0
for ((i = 1; i <= days; i++)); do
        deadlift=$((deadlift + 2))
done
echo "Please Complete $deadlift Deadlifts (2 Sets) Every Day For The Next $days Days"
echo

echo "Exercises For The Chest Are As Follows : "
echo

push_ups=0
for ((i = 1; i <= days; i++)); do
	push_ups=$((push_ups + 5))
done
echo "Please Complete $push_ups Push Ups (2 Sets) Every Day For The Next $days Days"

flys=0
for ((i = 1; i <= days; i++)); do
        flys=$((flys + 4))
done
echo "Please Complete $flys Chest Flys (3 Sets) Every Day For The Next $days Days"
echo

echo "Exercises For The Arms Are As Follows : "
echo

curls=0
for ((i = 1; i <= days; i++)); do
        curls=$((curls + 5))
done
echo "Please Complete $curls Bicep Curls (3 Sets) Every Day For The Next $days Days"

dips=0
for ((i = 1; i <= days; i++)); do
        dips=$((dips + 8))
done
echo "Please Complete $dips Tricep Dips (2 Sets) Every Day For The Next $days Days"
echo

echo "Exercises For The Full Body Are As Follows : "
echo

burpees=0
for ((i = 1; i <= days; i++)); do
        burpees=$((burpees + 3))
done
echo "Please Complete $burpees Burpees (3 Sets) Every Day For The Next $days Days"

jacks=0
for ((i = 1; i <= days; i++)); do
        jacks=$((jacks + 12))
done
echo "Please Complete $jacks Jumping Jacks (2 Sets) Every Day For The Next $days Days"
echo

echo "Exercises For The Core Are As Follows : "
echo

plank=0
for ((i = 1; i <= days; i++)); do
        plank=$((plank + 15))
done
echo "Please Complete $plank Seconds Of Planks (3 Sets) Every Day For The Next $days Days"

climb=0
for ((i = 1; i <= days; i++)); do
        climb=$((climb + 7))
done
echo "Please Complete $climb Mountain Climbers (2 Sets) Every Day For The Next $days Days"

leg=0
for ((i = 1; i <= days; i++)); do
        leg=$((leg + 6))
done
echo "Please Complete $leg Leg Raises (3 Sets) Every Day For The Next $days Days"

echo
echo "--------------------------------------------------------- PROGRAM TERMINATED SUCCESSFULLY ---------------------------------------------------------"
echo