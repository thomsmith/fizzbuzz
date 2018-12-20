##Fizzbuzz Python Practice
#Tom Smith 2018

#"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number
#and for the multiples of five print “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz”."


#multiples of 3 fizz
#multiples of 5 Buzz
#3 & 5 print FizzBuzz

for x in range(1,101):
    if x % 3 == 0 and x % 5 != 0:
        print (str(x) + " Fizz")
    elif x % 5 == 0 and x % 3 != 0:
        print (str(x) + " Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print (str(x) + " FizzBuzz")
    else:
        print(x)
