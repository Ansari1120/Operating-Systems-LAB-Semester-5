print("Priority Job SCHEDULLING")
n= int(input("Enter number of processes : "))
d = dict()
 
for i in range(n):
    key = "P"+str(i+1)
    c = int (input("Enter Priority of the Process : "))
    a = float(input("Enter arrival time of process"+str(i+1)+": "))
    b = float(input("Enter burst/Executing time of process"+str(i+1)+": "))
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    d[key] = l
 #sorting in terms of Priority of a process
d = sorted(d.items(), key=lambda item: item[1][2])
 
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
 
print("Process | Priority | Arrival | Execute time | Exit | Turn Around | Wait |")
for i in range(n):
      print("   ",d[i][0]," | "," | ",d[i][1][2]," | ",d[i][1][0]," Sec"," | ",d[i][1][1]," Sec"," | ",ET[i]," Sec"," | ",TAT[i]," Sec"," | ",WT[i]," Sec"," | ")
print("\nAverage Waiting Time: ",avg_WT," sec")
print("\nAverage TurnAround Time: ",avg_TAT," sec")


