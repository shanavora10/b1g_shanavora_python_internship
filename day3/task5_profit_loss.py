cost = float(input("Enter cost price:"))
selling =float(input("Enter selling price:"))

if selling > cost:
    profit =selling - cost
    print("profit=",int(profit))

elif cost > selling :
    loss =cost - selling 
    print("loss=",int(loss))

else:
    print("no profit, no loss")

    