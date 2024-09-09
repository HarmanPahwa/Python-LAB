num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

a = num1
b = num2
while(b!=0):
    temp = b
    b = a%b
    a = temp

hcf = a 
lcm = int((num1*num2)/hcf)

print("LCM (",num1,", ",num2,") = ",lcm)
print("HCF (",num1,", ",num2,") = ",hcf)