marks = int(input("enter percentage : "))

if(marks>90):
    print("Grade A")

elif(marks>80 and marks<=90):
    print("Grade B")

elif(marks>60 and marks<=80):
    print("Grade C")

elif(marks>50 and marks<=60):
    print("Grade D")

elif(marks>33 and marks<=50):
    print("Grade E")

elif(marks<=33):
    print("Grade F")