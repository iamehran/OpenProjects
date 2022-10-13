# contributed by @JBidlack

#Ask thge user in the console how many terms you'd like to find the 
#sequence total for
terms = int(input("How many terms?"))

#Function recursively finds the total of the fibonacci sewquence of that 
#number and prints it into the console
def fibonacci(terms):
    if terms < 0:
        print("Invalid entry")
    elif terms == 0:
        return 0
    elif terms ==1 or terms == 2:
        return 1
    else:
        return fibonacci(terms-1) + fibonacci(terms-2)
print(fibonacci(terms))
