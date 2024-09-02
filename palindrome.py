num = int(input("enter number : "))
temp = num
reverse = 0 
while(temp>0):
    remainder = temp%10
    reverse = reverse*10 + remainder
    temp = temp // 10

print("the reverse number is : ",reverse)
if(num==reverse): 
    print("palindrome")
else:
    print("not palidrome")