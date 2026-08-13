print("hello ! welcome to calculator")
print("Press + for addition \n Press - for subtraction \n Press * for multiplication \n Press / for division ")
op=input("enter the operation : ")
try:
    num1=int(input("enter the first number : "))
    num2=int(input("enter the second number : "))

    match op:
        case "+":
            print(f"the addition is : {num1+num2}")
        case "-":
            print(f"the subtraction is : {num1-num2}")
        case "*":
            print(f"the multiplication is : {num1*num2}")
        case "/":
            print(f"the division is : {num1/num2}")
        case default: 
            print("enter the valid operation !!")
except Exception as e:
    print(f"enter the valid value for numbers {e}")
