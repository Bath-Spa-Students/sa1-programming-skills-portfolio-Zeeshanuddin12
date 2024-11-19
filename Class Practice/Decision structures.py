sales = int (input ("Enter Sales:")) #Input from user on how much sales has taken place.
bonus = 0 #Default Bonus value set to 0
if sales >  50000: #If sales is greater than 50000
     bonus = 5100 # set Bonus to 5100
else :
       bonus = 0 # else set Bonus to 0
print ("Your Bonus is "+str(bonus )) #Prints the Bonus