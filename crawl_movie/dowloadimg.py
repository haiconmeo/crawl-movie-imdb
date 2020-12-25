import requests 
import csv
import shutil 
row_names = ['movie_id', 'movie_img']
with open('movie_poster_1M.csv', 'r', newline='') as in_csv:
    reader = csv.DictReader(in_csv, fieldnames=row_names, delimiter=',')
    for row in reader:
        movie_id = row['movie_id']
        movie_url = row['movie_img']


        filename = row['movie_id']+".jpg"


        r = requests.get(movie_url, stream = True)


        if r.status_code == 200:

            r.raw.decode_content = True
            

            with open("data/"+filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')