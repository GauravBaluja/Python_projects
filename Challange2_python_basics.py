#Programming Challenge2: Miles Per Gallon
#For this exercise, you will create a program that approximates the number of miles per gallon that a car gets.

from random import randint

gallan_fuel_tank = randint(10,25)  # gallan_fuel_tank = the number of gallons of gas that the car's fuel tank holds.
milage = randint(200,500)   # milage = the miles that the car can travel on a full tank before needing a refuel.
MPG = milage/gallan_fuel_tank
print(round(MPG,2))


#Challange3
#grading system for school teacher
grade = int(input("Enter student Score: "))
if grade >= 90:
    print("Grade A")
elif grade >= 80:
        print("Grade B")
elif grade >= 70:
        print("Grade C")
elif grade >= 60:
        print("Grade D")
else: print("grade F")

