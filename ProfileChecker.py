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
    gpa=float(input("Enter your gpa :"))
    field=input("what is your field of interest :")
    graduated=input("Yes or No :") 
    print("Name :" , name)
    print("age :" , age)
    print("gpa :" , gpa)
    print("field :" , field)
    print("graduated :" , graduated)
    if age<25 and gpa>=3.5 and graduated=="yes":
        print("You are eligible for a scholarship")
    elif age<30 and gpa>=2.5:
        print("You are eligible for a internship")
    else:
        print("You are not eligible now please apply later")
students()    






