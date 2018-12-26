#The user enters a cost and then the amount of money given.
#The program will figure out the change and the numbers of denominations to be returnedself.
#Available denominations are 1000,500,200,100,50,20,10,5,1

import pandas as pd
cost= int(input("Enter the cost of the product:\n"))
amount= int(input("Enter the money given:\n"))
change=amount-cost
print("Total change is: \n {}".format(change))
result=[]

denominations=[1000,500,200,100,50,20,10,5,1]

for i in denominations:
    for f in range (0,change):
        if change>=i:
            change=change-i
            result.append(i)
            if change==0:
                break
mycount=pd.Series(result).value_counts()
print("denominations to return are:\n{}".format(mycount))
