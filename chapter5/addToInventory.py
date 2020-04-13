def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal += v
    print('Total number of items: ' + str(itemTotal))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return(inventory)
    
inv = {'gold coin': 42, 
       'rope': 1}
dragonLoot = ['gold coin', 
              'dagger', 
              'gold coin', 
              'gold coin', 
              'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
