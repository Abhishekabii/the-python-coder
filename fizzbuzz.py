'''1. Write a program that prints the numbers from 1 to N. 
But, for multiples of three,  print “Fizz” instead of the number and
for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.

Below is an example:

Input: N = 17
Output:
1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17'''




n=int(input('Enter an input integer N'))
lisst=[i for i in range(1,n+1)]
final=[]


def fizzbuzz(val):
    for i in val:
        if i%3==0 and i%5==0:
            final.append('FizzBuzz')
        elif i%3==0:
            final.append('Fizz')
        elif i%5==0:
            final.append('Buzz')
        else:
            final.append(i)
    return(final)



print(fizzbuzz(lisst))
