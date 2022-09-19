print("\n\n*** Hey This is Z&E Coffe shop ***\n")
print("\nWe have special case for 'Ben'")
name=input("\nwhats your name?\n")

if name=="Ben":
  ans=input("Are you Evil?\n")
  if ans=="yes":
    print("sorry you are not gonna have coffee")
    exit()
  else:
    print("hey",name, "whatsaaap!!!!!")
  
else:
  print("Hellow "+name +", welcome to our shop!!!")
  
print("What would you like to have from our menu\nMenu : Espresso,Latte, Capachino, Mocha, Hazelnut, Frappuchino")
order=input()

if order=="Espresso" or order=="Latte" or order== "Capachino" or order=="Mocha" or order=="Hazelnut" or order=="Frappuchino":
  print("What quantity you want to order?")
  q=input()
  if order=="Espresso": 
    bill=int(q)*10
  if order=="Latte":
    bill=int(q)*20
  if order=="Capachino":
    bill=int(q)*30
  if order=="Mocha":
    bill=int(q)*40
  if order=="Hazelnut":
    bill=int(q)*50
  if order=="Frappuchino":
    bill=int(q)*60

  print("please pay $",bill)
# pass
    
else:
  print("Sorry your selected item is not available !!!")