playerid,cpuid='',''
def decideID(playerID,cpuID): 
    playerID= playerID+input("Which one do you want? X/O: ")
    
    if playerID=="X": 
        cpuID+="O"
    elif playerID=="O": cpuID+="X"
    else: 
        print("wrong choice...")
        decideID(playerID,cpuID)
    playerid,cpuid=(playerID,cpuID)
    return (playerID,cpuID)