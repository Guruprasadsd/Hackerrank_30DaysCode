'''
https://www.hackerrank.com/challenges/30-binary-numbers?isFullScreen=true
'''
#!/bin/python3

num = int(input())

result = 0
max1 = 0

while num > 0:
    if num % 2 == 1:
        result += 1
        if result > max1:
            max1 = result

    else:
        result = 0

    num //= 2

print(max1)
