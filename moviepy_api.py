import requests
import pprint
import pandas as pd
api_key = "99558ae618ca3adc4cfcf6b988a999dd"
api_key_v4 = "<your v4 key>"


api_version = 3

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
searh_query = input("Enter Movie to search:")
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            print(result['title'],"ID:", _id,"\nRelease Date:",result['release_date'],"\nOverview:" ,result['overview'],"\nVote Average:", result['vote_average'] ,"\n\n")
            
        