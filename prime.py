a = int(input("enter number : "))
flag = 0
for i in range(2,a-1,1):
    if(a%i!=0):
        flag = 1
        break

if(a==1):
    print("neither prime or composite")
if(flag == 1):
    print("prime number")
else:
    print("composite number")
