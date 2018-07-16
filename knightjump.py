import numpy as np

class State:
    def __init__(self,position,before):
        self.position=position
        self.before=before
    def __eq__(self,other):
        if self.position==other.position:
            return True
        return False

goal=State((2,1),None)
start=State((0,0),None)

def getNeighbours(currentState):
    nextStates=[]
    i=currentState.position[0]
    j=currentState.position[1]
    #up
    if i-2>=0:
        #left
        if j-1>=0:
            nextStates.append(State((i-2,j-1),currentState))
        #right
        if j+1<5:
            nextStates.append(State((i-2,j+1),currentState))
    #down
    if i+2<5:
        #left
        if j-1>=0:
            nextStates.append(State((i+2,j-1),currentState))
        #right
        if j+1<5:
            nextStates.append(State((i+2,j+1),currentState))
    #left
    if j-2>=0:
        #up
        if i-1>=0:
            nextStates.append(State((i-1,j-2),currentState))
        #down
        if i+1<5:
            nextStates.append(State((i+1,j-2),currentState))
    #right
    if j+2>=0:
        #up
        if i-1>=0:
            nextStates.append(State((i-1,j+2),currentState))
        #down
        if i+1<5:
            nextStates.append(State((i+1,j+2),currentState))

    return nextStates

currentState=start
visitedStates=[]
openStates=[]
visitedStates.append(currentState)

while True:
    if currentState==goal: break
    
    visitedStates.append(currentState)

    for state in getNeighbours(currentState):
        if state not in visitedStates:
            openStates.append(state)

    currentState=openStates.pop(0)

backtrack=[]
while(currentState.before is not None):
    backtrack.append(currentState.position)
    currentState=currentState.before
backtrack.append(currentState.position)

for i in range(len(backtrack)-1,-1,-1):
    print(backtrack[i])
