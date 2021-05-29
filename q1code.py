def fizzBuzz():
    teststring = ""
    for i in range (1,101):
        if ((i % 3) == 0):
            if ((i % 5) == 0):
                teststring = teststring + "FizzBuzz "
            else:
                teststring = teststring + "Fizz "
        elif ((i % 5) == 0):
                teststring = teststring + "Buzz "
        else:
            teststring = teststring + str(i) + " "
    return(teststring)