import requests

def fetch_data(animal_name):
    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {'X-Api-Key': 'qHlQOuzOCRcMJX4N2vZyoadg1Ei5w0II4gsu6boG'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data
