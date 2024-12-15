age = eval(input("Enter your age ---> "))

if age >= 1 and age <= 7:
     print(" toddler ")

elif age >= 8 and age <= 13:
     print(" pre teen ")

elif age >= 14 and age <= 18:
     print(" teenager ")

elif age >= 19 and age <= 31:
     print(" early adulthood ")

elif age >= 32 and age <= 45:
     print(" mid adulthood ")

elif age >= 46 and age <= 59:
     print(" post adulthood ")
 
elif age >= 60 and age <= 150:
   print(" senior ")



else:
     print("INVALID AGE")