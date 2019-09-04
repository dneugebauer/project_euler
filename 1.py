#!/usr/bin/env python3

def sum_of_mult(num):
    sum = 0
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return print(sum)

sum_of_mult(10)
sum_of_mult(1000)

#VICTORY!
