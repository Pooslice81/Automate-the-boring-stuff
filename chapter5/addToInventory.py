import pprint

inventory = {'arrow': 12,
             'gold coin': 42,
             'rope': 1,
             'torch':6, 
             'dagger': 1}

def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal = itemTotal + v
    print('Total number of items: ' + str(itemTotal))


def addToInventory(inventory, addedItems):
    


inv = {'gold coin': 42,
       'rope': 1}
dragonLoot = {'gold coin',
              'dagger',
              'gold coin',
              'gold coin',
              'ruby'}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
