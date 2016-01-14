# In his exalted name
# Algorithm: Tower of Hanoi
# Author: Ahmad Siavashi (ahmad.siavashi@gmail.com)
# Date: 16/3/2013
def MoveTower(n):
    stages = []
    stageName = {0:"A",1:"B",2:"C"}
    for i in xrange(3):
        stages.append([])
    for i in xrange(n,0,-1):
        stages[0].append((i,0))
    print stages
    for i in xrange(1,2**n):
        # Odd Moves
        if i%2 != 0:
            if i == 1 and n%2 == 0:
                stages[1].append((stages[0].pop()[0],0))
                print "Move A To B"
            elif i == 1 and n%2 == 1:
                stages[2].append((stages[0].pop()[0],0))
                print "Move A To C"
            else:
                pillars = [0,1,2]
                for i in xrange(3):
                    if stages[i] != [] and stages[i][-1][0] == 1:
                        pillars.remove(i)
                        pillars.remove(stages[i][-1][1])
                        break
                stages[pillars[-1]].append((stages[i].pop()[0],i))
                print "Move " + stageName[i] + " To " + stageName[pillars[-1]]
        # Even Moves
        else:
            pillars = [0,1,2]
            for i in xrange(3):
                if stages[i] != [] and stages[i][-1][0] == 1:
                    pillars.remove(i)
                    break
            if stages[pillars[0]] == []:
                stages[pillars[0]].append((stages[pillars[1]].pop()[0],pillars[1]))
                print "Move " + stageName[pillars[1]] + " To " + stageName[pillars[0]]
            elif stages[pillars[1]] == []:
                stages[pillars[1]].append((stages[pillars[0]].pop()[0],pillars[0]))
                print "Move " + stageName[pillars[0]] + " To " + stageName[pillars[1]]
            else:
                if stages[pillars[0]][-1][0] < stages[pillars[1]][-1][0] :
                    stages[pillars[1]].append((stages[pillars[0]].pop()[0],pillars[0]))
                    print "Move " + stageName[pillars[0]] + " To " + stageName[pillars[1]]
                else:
                    stages[pillars[0]].append((stages[pillars[1]].pop()[0],pillars[1]))
                    print "Move " + stageName[pillars[1]] + " To " + stageName[pillars[0]]

            
                    
MoveTower(8)
