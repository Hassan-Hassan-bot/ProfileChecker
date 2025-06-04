# Write a Python program that asks the user for the following information:
#     Name, Age, GPA (0-5, can be decimals), Field of Interest, Graduated ("yes" or "no").
# 1- Print a nicely formatted 
# 2- Based on the info, determine and print:

#     If the user is eligible for a scholarship (age < 25, GPA ≥ 3.5, has graduated)
#     If the user is eligible for an internship (age < 30, GPA ≥ 2.5)
#     If neither, recommend they apply again later.

def students():
    name= input("whats your name :")
    age=int(input("Enter your age :"))
    while True:
        gpa = float(input("Enter your gpa (0-5): "))
        if 0 <= gpa <= 5:  # chek gpa
            break
        else:
            print("Invalid GPA! Please enter a number between 0 and 5.")
    field=input("what is your field of interest :")
    graduated=input("Yes or No :") 
    print("Name :" , name)
    print("Age :" , age)
    print("Gpa :" , gpa)
    print("Field :" , field)
    print("Graduated :" , graduated)
    if age<25 and 5>=gpa>=3.5 and graduated.lower()=="yes":
        print((name+", you are eligible for a scholarship").capitalize())
    elif age<30 and 5>=gpa>=2.5:
        print((name+", you are eligible for a internship").capitalize())
    else:
        print((name+", you are not eligible now, please apply later").capitalize())
students()    






