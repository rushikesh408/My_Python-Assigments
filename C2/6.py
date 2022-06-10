print("""\tThis Find Simple Interest application will ask user to specify
the amount of a loan, an interest rate, and the number of years.
The application calculates and display the simple interest for the
given loan at the specified interest for a specified number of years.""")

user_choice ='y'
while user_choice.lower() =='y':
    #2
    while True:
            my_loan=int(input("enter the amount of loan "))

            if my_loan > 0 :
                print("validated")
                break
            else :
                print("enter a loan again")
    #3
    while True:
            my_intrest=float(input("enter the interest rate  "))

            if my_intrest > 0 :
                print("validated")
                break
            else :
                print("enter a interest again")
    #4
    while True:
            my_time=int(input("enter the number of years"))

            if my_time > 0 :
                print("validated")
                break
            else :
                print("enter a number of years again")

    #5 #interest = principal * rate * time
    myInt = my_loan* (my_intrest/100) * my_time

    print("principle amount is",myInt)
    #6
    print("The  interest on a loan of $",my_loan, "at",my_intrest,"%", "interest rate for ",my_time,"year\n"
              "is $",myInt)

    #7
    user_choice=input("Do you want to do another calculation? (y for yes)")

print("Done")



