import requests
import collections
from typing import List

#Movie=  collections.namedtuple('Movie', 'imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score')

Search= collections.namedtuple('Search', 'category, id, url, title, description')

def find_movie_by_title(keyword: str) -> List[Search]:
    #url = f'http://movie_service.talkpython.fm/api/search/{keyword}'
    url= f'https://search.talkpython.fm/api/search?q={keyword}'

    resp= requests.get(url)
    resp.raise_for_status

    #print(resp.text)

    results= resp.json()
    search= []

    for s in results.get('results'):
        search.append(Search(**s))

    return search
   