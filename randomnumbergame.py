import random

#Generate the random number
print('In this game you will try to predict a  number which the computer has in mind. If your number matches, you win. ')
print('If not the computer will give you hints. Go ahead, try it out.')
randomnumber = random.randint(0,1000)

#Select the numbers which give the hints
minusten = randomnumber - random.randint(1,20)
plusten = randomnumber + random.randint(1,20)

#Run the code
for i in range(1000):
#Ask User's input
    rawusernumber = input("Please enter a number: ") 
    
    usernumber = int(rawusernumber)
    if randomnumber == usernumber:
        print('Your number was right!' + '\n')
        break
    elif (minusten == randomnumber) or (plusten == randomnumber):
        print('You have failed. The number was ' + str(randomnumber) + '\n')
        break
    else:        
        print('Try again. The number is between ' + str(minusten) + ' and ' + str(plusten)+ '\n')
        minusten = minusten + 1
        plusten = plusten - 1
    
    
        
        
        
print('The End')

