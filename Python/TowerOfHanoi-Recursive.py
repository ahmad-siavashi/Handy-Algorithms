# In his exalted name
# Algorithm: Tower of Hanoi
# Author: Ahmad Siavashi (ahmad.siavashi@gmail.com)
# Date: 11/9/2013

def MoveTower(n,Source,Temp,Destination):
    if n == 1 :
        print "Move " + Source + " To " + Destination
        return
    MoveTower(n-1,Source,Destination,Temp)
    MoveTower(1,Source,Temp,Destination)
    MoveTower(n-1,Temp,Source,Destination)

MoveTower(8,"A","B","C")
