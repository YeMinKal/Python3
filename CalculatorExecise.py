#!/usr/bin/python3

#Program name :     Calculator
#Programmer   :     Ye Min Kal
#Start date   :     6.6.2020
#End date     :     6.6.2020


while 1:
    first_number    =   float(input('First Number:  '))
    Calculate_sign  =   input('Calculate Sign:  ')
    Second_number   =   float(input('Second Number: '))

    if Calculate_sign           == '+':
        result                  = first_number + Second_number
    elif Calculate_sign         == '-':
        result                  = first_number - Second_number
    elif Calculate_sign         == '*':
        result                  = first_number * Second_number
    elif Calculate_sign         == '/':
        result                  = first_number / Second_number
    elif Calculate_sign         == '%':
        result                  = first_number % Second_number
    else:
        print ('anyone is false')
    print("Calculation Done     ", result )
