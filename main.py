import random
Username = input("Enter Your Username : ")

# Email Verification

Email = input("Enter Your Email : ")
EmailAccepted = None
for i in Email :
    if i == "@" :
        EmailAccepted = True
        if EmailAccepted == True :
            break
if EmailAccepted == True:
    print("Email Accepted Succesfully !!")
else:
    print("Email Not Valid !! ")


# Email Confirmation

Email_Confirmation = input("Confirm Your Email : ")

if Email_Confirmation == Email :
    Confirmation = True
else:
   Confirmation = False

if Confirmation == True :
    print("EmaiL Cofirmed Succesfully !! ")
else:
    print("Emails Don't Match !!")


#Password Verification

Password = input("Type Your Password : ")

# Password Confirmation

Password_Confirmation = input("Confirm Your Password : ")
sonfirmation = None
if Password_Confirmation == Password :
    sonfirmation = True
else:
   sonfirmation = False

if sonfirmation == True :
    print("Password Cofirmed Succesfully !! ")
else:
    print("Passwords Don't Match !!")

# Captcha

FirstNumber = str(random.randint(1, 10))
SecondNumber = str(random.randint(1, 10))
ReCaptcha = print("Answer : " + str(FirstNumber) + " + "+  str(SecondNumber))

# Captcha Answer

# Captcha

FirstNumber = random.randint(1, 10)
SecondNumber = random.randint(1, 10)
ReCaptcha = print("Answer : " + str(FirstNumber) + " + "+  str(SecondNumber))

# Captcha Answer

Answer = input("The Correct Answer Is : ")
rightAnswer = FirstNumber + SecondNumber
if rightAnswer == Answer :
    print("You're not a Robot ")
else:
    print("Failed To Check Your Identity !!")