order = "salad water hamburger salad hamburger"

def item_order(order):
   return 'salad:' + str(order.count('salad')) + ' ' + 'hamburger: ' + str(order.count('hamburger')) +\
   ' ' +  'water:' + str(order.count('water'))
    
print item_order(order)