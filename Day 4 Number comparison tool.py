 #Nuber Comparison tool

#step 1: get input
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second Number: "))

#step 2: comparison
print("\n---- Comparison result ----")
if num1 == num2:
    print(f"Both numbers are equal: {num1}")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

#step 3: check if any number is zerp(0)
if num1 == 0 or num2 == 0:
    print("\nAt least one of number is zero.")
else:
    print("\nBoth number is non-zero.")


#Check nubers are positive or negative