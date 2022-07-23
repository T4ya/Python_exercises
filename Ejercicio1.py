#@T4ya (YESID ORTIZ)

#Exercise 1: Calculate the multiplication and sum of two numbers:

#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.


def product_or_sum():

    #Inputs

    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))

        except:
            print ("Error, please enter integer numbers only")
        break

    if (num1 * num2) <= 100:
        print ("The product of the numbers is: ", num1 * num2)
    else:
        print ("The sum of the number is: ", num1 + num2)

product_or_sum()
