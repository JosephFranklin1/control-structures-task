total = 0
customerName = input("please enter your name\n")
customerAddress = input("please enter your address\n")
customerNumber = int(input("please enter your phone number\n"))
widthOfLawn = int(input("please enter the width of the lawn\n"))
if widthOfLawn <2 or widthOfLawn>30:
    print("your lawn is above the maximum width or below the minimum width\n")
lengthOfLawn = int(input("please enter the length of the lawn\n"))
if lengthOfLawn <2 or lengthOfLawn >50:
    print("your lawn is above the maximum length or below the minimum length\n")
quality = input("would you like to select a lawn care product?\n")
if quality == "yes":
    product = input("what quality of product would you like, luxury, standard, or economy\n")
    if product == "luxury":
        total = total + 1.15
    elif product == "standard":
        total = total + 0.8
    elif product == "economy":
        total = total + 0.45
if quality == "no":
    total = total + 0
areaOfLawn = widthOfLawn * lengthOfLawn
print (areaOfLawn,"is your lawn area")
total = total + areaOfLawn * 0.50
VAT = total * 0.2
totalVAT = total + VAT
print("Your total is £",total)
VAT = round(VAT,2)
print("Your VAT is £",VAT)
print("Your complete total is £",totalVAT)
print("Your details are", customerName,",",customerAddress,",",customerNumber,)
