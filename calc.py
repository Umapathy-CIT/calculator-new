while True:
    print("Choose any one of the given operators"+"\n")
    print(" +  -  *  /  %  **  // "+"\n")
    print("To quit the calculator press'q'"+"\n")
    userchoice = input("ENTER THE OPERATOR : ")
    if userchoice == "q":
        break
    elif userchoice in ["+","-","*","/","%","**","//"]:
       
       num1 = float(input("Enter the first number : "))
       num2 = float(input("Enter the second number : "))

    if userchoice == "+":
        result = num1 + num2
        print(num1,"+",num2,"=",result+"\n")
   
    elif userchoice == "-":
          result = num1 - num2
          print(num1,"-",num2,"=",result+"\n")
   
    elif userchoice == "*":
          result = num1 * num2
          print(num1,"*",num2,"=",result+"\n")

    elif userchoice == "/":
          result = num1 / num2
          print(num1,"/",num2,"=",result+"\n")

    elif userchoice == "%":
        result = num1 % num2
        print(num1,"%",num2,"=",result+"\n")
   
    elif userchoice == "**":
          result = num1 ** num2
          print(num1,"**",num2,"=",result+"\n")

    elif userchoice == "//":
          result = num1 // num2
          print(num1,"//",num2,"=",result+"\n")

    else:
        print("INVALID OUTPUT"+"\n")
