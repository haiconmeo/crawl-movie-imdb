import os
category= []
f= open("ml-1m_movies.dat",'r')
f2=open("list_cat",'w')
dem=0
for line in f:
    categori = line.split("::")[2]
    for i in categori.split("|"):
        i = i.replace("\n","")
        if i not in category:
            f2.write(str(dem)+":"+i)
            f2.write("\n")
            dem+=1
            
            category.append(i)

print(category)
f2.close()