dice=input("")
dice1=dice.split(" ")
money=0

if(len(set(dice1))==1):
    money=10000+int(dice1[0])*1000

elif(len(set(dice1))==2):

    if(dice1.count(list(set(dice1))[0])==2):
        money=1000+int(list(set(dice1))[0])*100

    else:
        money=1000+int(list(set(dice1))[1])*100

else:
    dice1.sort()
    money=int(dice1[-1])*100

print(money)
