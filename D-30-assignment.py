# 1. Smart Traffic Signal
# You are given the current signal color ("red", "yellow", "green") and a boolean value indicating whether an emergency vehicle is approaching.
# Decide what action should be taken:
# Stop
# Slow down
# Go
# Or override the signal for emergency vehicles.

signal=input("Enter signal color (red/yellow/green):").lower()
emergency=input("Are there any emergency vehicles approaching ?(true/false) ").lower()

emergency=emergency=="true" #imp to remember

if emergency:
    print("override the signal for emergency vehicles")
else:
    if signal=="red":
        print("Stop")
    elif signal=="yellow":
        print("Slow down")
    elif signal=="green":
        print("Go")
    else:
        print("Invalid signal color input... ")

#OUTPUT:
# Enter signal color (red/yellow/green):red
# Are there any emergency vehicles approaching ?(true/false) true
# override the signal for emergency vehicles

# 2. Loan Eligibility Checker
# A bank provides a loan based on the following conditions:
# Age must be between 21 and 60
# Monthly salary ≥ 25,000
# Credit score ≥ 700
# Given age, salary, and credit score, determine whether the person is:
# Fully eligible
# Partially eligible
# Not eligible

age=int(input("Enter age:"))
salary=int(input("Enter Monthly Salary:"))
cbil=int(input("Enter Credit Score:"))

if (21<=age<=60) :
    if (salary>=25000):
        if (cbil>=700):
            print("Eligible")
        else:
            print("Partially eligible")
    else:
        print("Partially eligible")
else:
    print("Not Eligible")

#OUTPUT:
# Enter age:21
# Enter Monthly Salary:25000
# Enter Credit Score:698
# Partially eligible

# 3. Triangle Type Identifier
# Given three integer values representing the sides of a triangle, determine:
# If a triangle is possible
# If possible, identify whether it is Equilateral, Isosceles, or Scalene
# Also handle invalid inputs logically.

side1=int(input("Enter side 1:"))
side2=int(input("Enter side 2:"))
side3=int(input("Enter side 3:"))

if side1<=0 or side2<=0 or side3<=0:
    print("Triangle is not possible , please enter positive sides")
elif side1+side2>side3 and side1+side3>side2 and side2+side3>side1:

    if side1==side2==side3:
        print("Equilateral Triangle")
    elif side1==side2 or side2==side3 or side3==side1:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Triangle is not possible")

#OUTPUT:
# Enter side 1:20
# Enter side 2:21
# Enter side 3:3
# Scalene Triangle

# 4. Electricity Bill Slab Logic
# Electricity charges depend on units consumed:
# First 100 units → free
# 101–300 units → ₹5 per unit
# Above 300 units → ₹10 per unit
# Given the number of units consumed, calculate the total bill amount using proper conditional logic.

units=int(input("Enter Consumed units:"))
if (units<=100):
    print("TOTAL BILL:Free")
elif (101<=units<=300):
    print(f"TOTAL BILL:{units*5} Rupees")
elif (units>300):
    print(f"TOTAL BILL:{units*10} Rupees")
else:
    print("Invalid input...")

# OUTPUT:
# Enter Consumed units:130
# TOTAL BILL:650 Rupees

# 5. Exam Result Analyzer
# A student has marks in three subjects.
# Rules:
# If any subject < 35 → Fail
# If average ≥ 75 → Distinction
# If average ≥ 60 → First Class
# If average ≥ 50 → Second Class
# Else → Pass
# Determine the student’s final result.

sub1=int(input("Enter Subject1 marks:"))
sub2=int(input("Enter Subject2 marks:"))
sub3=int(input("Enter Subject3 marks:"))

tot=sub1+sub2+sub3
avg=tot/3

if (sub1<35 or sub2<35  or sub3<35):
    print("Fail")
else:
    if (avg>=75):
        print("Distinction")
    elif (avg>=60):
        print("First class")
    elif (avg>=50):
        print("Second Class")
    else:
        print("Pass")

# OUTPUT:
# Enter Subject1 marks:35
# Enter Subject2 marks:56
# Enter Subject3 marks:65
# Second Class

