'''Exercise 1.2 from MITx 6.00.2X by Iñigo Esteban on 200402'''

class Stuff(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def getVWRatio(self):
        return self.getValue()/self.getWeight()
    '''el metodo __str__ define como quieres que se imprima la instancia cuando usas el metodo propio prin()'''
    def __str__(self):
        return self.name + ": <" + str(self.value)\
                + ", " + str(self.weight) + ">"
    
def homeObject(names, values, weights):
    '''These are the lists we append to an empty list in order to display a catalog :) '''
    elements = []
    for i in range(len(values)):
        elements.append(Stuff(names[i],values[i],weights[i]))
    return elements

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getWeight()) <= maxCost:
            result.append(itemsCopy[i])
            totalValue += itemsCopy[i].getValue()
            totalCost += itemsCopy[i].getWeight()
    return (result, totalValue)
    
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print("Total value of items taken =", val)
    for item in taken:
        print("    ", item)
        
def testGreedys(objects, maxWeight):
    print("Use greedy by value to allocate ", maxWeight, " Kilograms.")
    testGreedy(objects, maxWeight, Stuff.getValue)
    print("\nUse greedy by weight to allocate ", maxWeight, " Kilograms")
    testGreedy(objects, maxWeight, lambda x: 1/Stuff.getWeight(x))
    print("\nUse greedy by vwRatio to allocate ", maxWeight, " Kilograms")
    testGreedy(objects, maxWeight, Stuff.getVWRatio)
    
    
    
names = ("clock","picture", "radio", "vase", "book", "computer")
values = (175,90,20,50,10,200)
weights = (10, 9, 4, 2, 1, 20)

objects = homeObject(names,values,weights)
testGreedys(objects, 20)
        

            
            
            
    
        
        
    
        
    
