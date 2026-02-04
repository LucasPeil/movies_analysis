import os
import time

from dotenv import load_dotenv
import requests
import pprint
import database

load_dotenv()

session = requests.Session()
session.headers.update({'accept': 'application/json','Authorization': 'Bearer {}'.format(os.environ.get('API_KEY'))})

def api_request(page):
    base_url = 'https://api.themoviedb.org/3'
    base_query_params = 'include_adult=false&include_video=false&language=en-US&sort_by=popularity.desc&release_date.gte=2016-01-01&release_date.lte=2026-01-01'
    url = f"{base_url}/discover/movie?{base_query_params}&page={page}"
    batches =[]
    try:
        response = session.get(url)
        response.raise_for_status()
        json_response = response.json()
        movies= json_response.get('results',[])
        for movie in movies:
            movie_id = movie.get('id')
            detail_url = f"{base_url}/movie/{movie_id}"
            detail_response = session.get(detail_url)
            if detail_response.status_code == 429 :
                retry_after = detail_response.headers.get('retry-after', 5)
                time.sleep(int(retry_after))
                detail_response = session.get(detail_url)
            detail_data = detail_response.json()
            batches.append({
                'id': detail_data.get('id'),
                'title': detail_data.get('title'),
                'revenue': detail_data.get('revenue'),
                'budget': detail_data.get('budget'),
                'runtime': detail_data.get('runtime'),
                'genres': [g['name'] for g in detail_data.get('genres', [])],
                'release_date': detail_data.get('release_date'),
                'vote_average': detail_data.get('vote_average'),
                'vote_count': detail_data.get('vote_count'),
                'popularity': detail_data.get('popularity'),
            })
            time.sleep(0.1)

    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')

    return batches


def save_movies():
    # Initialize the database
    database.setup_db()
    pages = 150
    batches_saved = 0
    for page in range(1, pages+1):
        movies = api_request(page)
        time.sleep(0.5)
        if len(movies):
            database.save_movies_batch(movies)
            batches_saved+=1
            print(f"Successfully saved {batches_saved} batches.")
    print('All movies successfully saved to database.')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == "__main__":
    print('Loading Movies Database...')
    # save_movies()
