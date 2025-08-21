import tkinter as tk

# code python first, convert to tkinter code later

def metric():
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (meter): "))
    bmi = weight / (height**2)
    return bmi

def us():
    weight = float(input("Enter weight (lb): ")) 
    height = float(input("Enter height (in): "))
    bmi = weight / (height**2) * 703
    return bmi


def metricUse():
    choice = input("Do you want to use metric (1) or US unit (2)? : ")
    
    if choice == "1":
        useThisMetric = metric()
    elif choice == "2":
        useThisMetric = us()
    else:
        print("Invalid choice.")

    if useThisMetric < 18.5:
        category = "Underweight"
    elif 18.5 <= useThisMetric < 25:
        category = "Normal (healthy weight)"
    elif 25 <= useThisMetric < 30:
        category = "Overweight"
    elif 30 <= useThisMetric < 35:
        category = "Obesity class I"
    elif 35 <= useThisMetric < 40:
        category = "Obesity class II"
    else:
        category = "Obesity class III"

    print(f"Your BMI is: {useThisMetric:.2f}, ({category})")


metricUse()

