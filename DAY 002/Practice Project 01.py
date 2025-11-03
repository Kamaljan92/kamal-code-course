email="email@gmail.com"
password="123456ch"
name = input("Enter your name:")
emailuser=input("Enter your email:") 

if email==emailuser :
  passuser=input("Enetr your Password:")
  user=True
  if password==passuser:
    print(" WElcome ",name,"You have loggen in!")
  else:
    print("Your password is incorrect1")
else:
    print("Your Email is incorrect!")
    user=False
