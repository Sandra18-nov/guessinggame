#1 get user name 
from random import randint
random_number=randint(10, 50)
username=input("enter name: ")
print("hello there " + username + "!")

#generate a number
counter=0
while counter < 5:
    usernumber=eval(input("enter number:"))
    counter +=1
    if usernumber<random_number: 
        print("your guess is too low")
    elif usernumber>random_number:  
        print("your guess is too high")
    elif usernumber==random_number:
        
        break

if usernumber==random_number:
    print("you win!")
else:
    print("game over!" "The correct number is")
print(random_number)
















#usig a while loop
#get user number
#
#check if user input is equal to generated number
