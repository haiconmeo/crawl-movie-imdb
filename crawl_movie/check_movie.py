import os
dic = [i for i in range(1,3953)]
f = open("movie_poster_1M.csv","r")
for line in f:
   
    stt = int(line.split(",")[0])
    if stt in dic:
        dic.remove(stt)
print(dic)
f.close()
f2=open("move_name.txt",'w')
f= open("ml-1m_movies.dat",'r')
for line in f:
    stt = int(line.split("::")[0])
    if stt in dic:
        f2.write(str(stt)+":"+line.split("::")[1])
        f2.write("\n")
f2.close()
        