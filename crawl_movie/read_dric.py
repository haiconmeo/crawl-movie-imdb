import os
dic={}

f =  open("ml_plot.dat",'r')
f2 = open("disc.txt",'w')
for i in f:
    line = i.split("::")
    stt=int(line[0])
    print(stt)
    content =line[1]
    content = content.replace("|","")
    content = content.replace("\t"," ")
    f2.write(str(stt)+":"+content)
    f2.write("\n")
f2.close()
