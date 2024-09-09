num = int(input("enter a number : "))
sum = 0
temp = num
while(num):
    i=1
    fact = 1
    r = num%10
    while(i<=r):
        fact = fact * i
        i = i + 1
    sum = sum + fact
    num = num//10
if(sum == temp): print(temp,"is a strong number")
else : print(temp," is not a strong number")