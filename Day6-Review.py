'''
https://www.hackerrank.com/challenges/30-review-loop?isFullScreen=true
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(0,T):
    S=input()
    print(S[0::2],S[1::2])
    
    
#for j in m.split("\n"):
    #print(m[0:len(m):2],m[1:len(m):2])
"""
    T = int(input())
for i in range (0 , T):
    S = input()
    print(S[0::2] + " " + S[1::2])
    """
