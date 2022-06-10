#Calculate the simple interest for a specified number of years using the formula:
         # interest = principal * rate * time
    #For example, 1500 * (3.25/100) * 1 = 48.75
    #Assign the result to a variable

while True:
    my_loan=int(input("enter the amount of loan "))

    if my_loan > 0 :
        print("validated")
        break
    else :
        print("enter a loan again")

while True:
    my_intrest=float(input("enter the interest rate  "))

    if my_intrest > 0 :
        print("validated")
        break
    else :
        print("enter a interest again")

while True:
    my_time=int(input("enter the number of years"))

    if my_time > 0 :
        print("validated")
        break
    else :
        print("enter a number of years again")

#interest = principal * rate * time
myInt = my_loan* (my_intrest/100) * my_time

print("principle amount is",myInt)