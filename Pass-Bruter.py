x = "Y"
infolist = []
out = []
f = open("pass-list.txt","w+")
while x == "Y" or x == "y":
    y = input("What have you got for me? : ")
    x = input("Do you want to continue entering info[Y,N] : ")
    infolist.append(y)
for i in range(0,len(infolist)):
    out.append(infolist[i])    
    for j in range(0,len(infolist)):
        out.append(infolist[i]+infolist[j])
for k in range(0,len(out)):
    f.write(out[k]+"\n")
