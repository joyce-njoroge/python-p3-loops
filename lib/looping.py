#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = ""
    number = 10

    while number > 1:
        countdown += str(number) + "\n"
        number -= 1

    countdown += "1\n"
    countdown += "Happy New Year!"

    assert countdown == '10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nHappy New Year!', "Unexpected output"
    print(countdown)
    

def square_integers(int_list):
    # code goes here!
    return [x ** 2 for x in int_list]
    

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    
