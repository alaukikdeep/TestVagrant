Leather_Wallet=1100.00
Umbrella=900.00
Cigarette=200.00
Honey=100.00


print("Leather_Wallet : 1100.00")
print("Umbrella : 900.00")
print("Cigarette : 200.00")
print("Honey : 100.00")

while True:
    choice=input('\nChoose an item: Leather_Wallet, Umbrella, Cigarette, Honey \n')
    if choice == 'Leather_Wallet':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Leather_Wallet, Umbrella, Cigarette, Honey \n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: ",sum)
                print(" ")
    elif choice == 'Umbrella':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Leather_Wallet, Umbrella, Cigarette, Honey \n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: ",sum)
                print(" ")
    elif choice == 'Cigarette':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Leather_Wallet, Umbrella, Cigarette, Honey \n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: ",sum)
                print(" ")
    elif choice == 'Honey':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Leather_Wallet, Umbrella, Cigarette, Honey \n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: ",sum)
                print(" ")
    
    else: 
        print("Error!")
    break
