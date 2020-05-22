data1 = int( input("enter the value of a:"))
print("a=",data1)

data2 = int(input("enter the value of b:"))
print("b=",data2)

data3 = input("enter an operation:")
if data3 == "+":
    print("added value is ", data1+data2)
elif data3 =="-":
    print("subtracted value is", data1-data2)
elif data3 =="*":
    print("multiplied value is",data1*data2)
elif data3 == "/":
    print("divided value is", data1/data2)
else:
    print("enter any of the following operations \n +,-,*,/")