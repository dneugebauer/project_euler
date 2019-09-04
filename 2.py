#!/usr/bin/env python3

def fib_sum(num):
    output = [0,1]
    sum = 0
    for i in range(1, num+1):
        if output[1] >= 4000000:
            return print(sum)
        output[1], output[0] = output[0]+output[1], output[1]
        if output[1] % 2 == 0:
            sum += output[1]
fib_sum(10000)
fib_sum(100000)
fib_sum(10)
#VICTORY!
