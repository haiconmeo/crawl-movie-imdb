import os
f = open("ml-1m_movies.dat",'r')
dic ={}
f_dicr =  open("disc.txt",'r')
for i in f_dicr:
    if i == '\n':
        continue

    stt = i.split(":")[0]
    dic[stt] =  i.split(":")[1]
    

f2 = open("movie_name_list.txt",'w')
for i in f :
    line  = i.split("::")
    id = line[0]
    name = line[1].split("(")[0]
    year = int(line[1].split("(")[-1].split(")")[0])
    diii = ""
    if id not in dic:
        diii = "no content"
    else:
        diii = dic[id]
    discripsion =  diii
    f2.write(str(id)+"::"+name+"::"+str(year)+"::"+discripsion+"\n")
f2.close()