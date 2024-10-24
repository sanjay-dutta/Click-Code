x = int(input("Enter the value of x: "))

match x:
    # if x is 0
    case 0:
        print("x is zero")
    # if x is 4
    case 4:
        print("x is 4")
    # if x is 90
    case _ if x == 90:
        print(x, "is 90")
    # if x is 80
    case _ if x == 80:
        print(x, "is 80")
    # if x is 100
    case _ if x == 100:
        print(x, "is 100")
    # if x is neither 90 nor 80
    case _ if x != 90 and x != 80:
        print(x, "is neither 90 nor 80")
