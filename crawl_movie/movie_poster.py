import csv
import urllib.request
from bs4 import BeautifulSoup

row_names = ['movie_id', 'movie_url']
with open('movie_url_1M.csv', 'r', newline='') as in_csv:
    reader = csv.DictReader(in_csv, fieldnames=row_names, delimiter=',')
    for row in reader:
        movie_id = row['movie_id']
        print(movie_id)
        movie_url = row['movie_url']
        domain = 'http://www.imdb.com'
        with urllib.request.urlopen(movie_url) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')

            try:
                image_url = soup.find('div', class_='poster').a.img['src']

                extension = '.jpg'
                image_url = ''.join(image_url.partition('_')[0]) + extension
                filename = 'img/' + movie_id + extension
                with urllib.request.urlopen(image_url) as response:
                    with open(filename, 'wb') as out_image:
                        out_image.write(response.read())
                    with open('movie_poster_1M.csv', 'a', newline='') as out_csv:
                        writer = csv.writer(out_csv, delimiter=',')
                        writer.writerow([movie_id, image_url])

            except AttributeError:
                pass