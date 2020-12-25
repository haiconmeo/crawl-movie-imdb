import csv
dem=0
cate={"Animation":1,"Children's":2,"Comedy":3,"Adventure":4,"Fantasy":5,"Romance":6,"Drama":7,"Action":8,"Crime":9,"Thriller":10,"Horror":11,"Sci-Fi":12,"Documentary":13,"War":14,"Musical":15,"Mystery":16,"Film-Noir":17,"Western":18}
f= open("ml-1m_movies.dat",'r')
for i in f:
    line =  i.split("::")
    stt = line[0]
    cat = line[2].split("\n")[0].split("|")
    for j in cat:
        dem+=1
        with open('importcategori.csv', 'a', newline='') as out_csv:
            writer = csv.writer(out_csv, delimiter=',')
            writer.writerow([dem, stt,cate[j]])
