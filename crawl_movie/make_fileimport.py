import   csv
f_list = {}
no_img = "no-img.png"
# for i in open("file.txt",'r'):
#     noimg = i
for i in open("file.txt",'r'):
    if i =="\n":
        continue
    stt = (i.split("::")[0].split(".")[0])
    if stt != "no-img":
        f_list[stt] = i.split("::")[1].split("\n")[0]
# print(f_list[1])
dem = 0
f = open("movie_name_list.txt",'r')
for line in f:
    if line =="\n":
        continue
    # if dem > 50 :
    #     break
    id = line.split("::")[0]
    name = line.split("::")[1]
    year = line.split("::")[2]
    content = line.split("::")[3]
    if id not in f_list:
        img = no_img
    else:
        img = f_list[id]



    with open('importMovie_2.csv', 'a', newline='') as out_csv:
        writer = csv.writer(out_csv, delimiter=',')
        writer.writerow([id, name,content,img,year])