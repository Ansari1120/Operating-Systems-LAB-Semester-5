print("FIRST COME FIRST SERVE SCHEDULLING")
n= int(input("Enter number of processes : "))
d = dict()
 
for i in range(n):
    key = "Process"+str(i+1)
    a = float(input("Enter ready time of process"+str(i+1)+": "))
    b = float(input("Enter executing time of process"+str(i+1)+": "))
    l = [] #list
    l.append(a)
    l.append(b)
    d[key] = l
 
d = sorted(d.items(), key=lambda item: item[1][0])
    
ET = []
for i in range(len(d)):
    # first process
    if(i==0):
        ET.append(d[i][1][1])
 
    # get prevET + newBT
    else:
        ET.append(ET[i-1] + d[i][1][1])
 
TAT = []
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0])
 
WT = []
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1]/1000)
 
avg_WT = 0
for i in WT:
    avg_WT +=i
avg_WT = (avg_WT/n)

avg_TAT = 0
for i in TAT:
    avg_TAT +=i
avg_TAT = (avg_TAT/n)
 
print("Process_Name | ready | Executing | Exit | Wait time of a process |")
for i in range(n):
     print("   ",d[i][0],"   |   ",d[i][1][0]," |  ",ET[i],"  |    ",TAT[i],"  |   ",WT[i])
print("Average Waiting Time: ",avg_WT)
print("Average TurnAround Time: ",avg_TAT)

