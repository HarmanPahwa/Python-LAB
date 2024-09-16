def length(n):
    len = 0
    while(n!=0):
        len = len + 1
        n //= 10
    return len

n = int(input("enter a number : "))
rem = sum = 0
len = length(n)
num = n

while(num>0):
    rem = num%10
    sum = sum + int(rem**len)
    num//=10
    len = len - 1

if(sum==n): print(n,"is a disarium number")
else: print(n,"is not a disarium number")