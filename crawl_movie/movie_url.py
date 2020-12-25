import csv
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

row_names = ['movie_id', 'movie_title']
with open('move_name.txt', 'r', encoding = "ISO-8859-1") as f:
    
    for row in f:

        movie_id = row.split(":")[0]
        movie_title = row.split(":")[1].strip()
        print(movie_title)
        movie_title = movie_title.split(",")[0]
        movie_title = movie_title.split("(")[0]

        domain = 'http://www.imdb.com'
        search_url = domain + '/find?q=' + urllib.parse.quote_plus(movie_title)
        print(search_url)
        with urllib.request.urlopen(search_url) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            # Get url of 1st search result
            try:
                title = soup.find('table', class_='findList').tr.a['href']
                movie_url = domain + title
                with open('movie_url_1M_2.csv', 'a', newline='') as out_csv:
                    writer = csv.writer(out_csv, delimiter=',')
                    writer.writerow([movie_id, movie_url])
            # Ignore cases where search returns no results
            except AttributeError:
                pass
