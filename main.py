from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
top_movies = response.text
soup = BeautifulSoup(top_movies, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")

                                #reverses the numbers [::-1]
titles = [t.getText() for t in movie_titles[::-1]]


with open("movies.txt", mode="w") as movie_file:
    for title in titles:
        movie_file.write(f"{title}\n")
        print(title)
