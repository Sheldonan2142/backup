# Name: Abigail Sheldon
# Period 4
# Dice Rolling Simulator
import random
min = 1
max = 6
rolls = int(input("How many times should the dice roll? "))
#rannum = random.randint(min,max)
dicenum = 1
#diceroll = rolls
# Declare variables to count occurances of each number
countone = 0
counttwo = 0
countthree = 0
countfour = 0
countfive = 0
countsix = 0

for i in range(rolls):
  number =  int(random.randint(min,max))
  #print ("Roll "+str(dicenum)+" was a "+str(random.randint(min,max)))
  if number == 1: 
    countone +=1
  if number == 2:
    counttwo  +=1
  if number == 3:
    countthree +=1
  if number == 4:
    countfour +=1
  if number == 5:
    countfive +=1
  if number == 6:
    countsix +=1
    
  print ("Roll "+str(dicenum) +" was a " +str(number))
 
  
  #count the number of occurances
 

  dicenum = dicenum + 1

print('\n')
print("Total rolls: "+str(rolls)+'\n')
print ("The total number of 1's is: " +str(countone))
print ("The total number of 2's is: " +str(counttwo))
print ("The total number of 3's is: " +str(countthree))
print ("The total number of 4's is: " +str(countfour))
print ("The total number of 5's is: " +str(countfive))
print ("The total number of 6's is: " +str(countsix))


print('\n')
print ("The percentage of 1's is: "+ str(countone*(100/(int(countone)+int(rolls)))
)+'%')
print ("The percentage of 2's is: "+ str(counttwo*(100/(int(counttwo)+int(rolls)))
)+'%')
print ("The percentage of 3's is: "+ str(countthree*(100/(int(countthree)+int(rolls)))
)+'%')
print ("The percentage of 4's is: "+ str(countfour*(100/(int(countfour)+int(rolls)))
)+'%')
print ("The percentage of 5's is: "+ str(countfive*(100/(int(countfive)+int(rolls)))
)+'%')
print ("The percentage of 6's is: "+ str(countsix*(100/(int(countsix)+int(rolls)))
)+'%')