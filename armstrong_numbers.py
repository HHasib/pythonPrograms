

def armstrong(x):
    # for i in range (3):
    y=x
    third_digit = x%10
    y= y//10
    # print (y)
    second_digit = y%10
    y= y//10
    # print(y)

    first_digit = y%10
    # print(x)
    # print(third_digit)
    # print(second_digit)
    # print(first_digit)
    if x == (third_digit**3)+(second_digit**3)+(first_digit**3):
        print(x,"is an armstrong number")
    else:
        print(x,"is not an armstrong number")



x = 378
armstrong(x)