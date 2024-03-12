import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint

ua = UserAgent()

url = 'https://www.boxofficemojo.com'
path = '/intl/'
params = {'ref_': 'bo_nb_hm_tab'}
headers = {'User-Agent': ua.random}

session = requests.session()
response = session.get(url+path, params=params, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

test_link = soup.find("a", {'class': 'a-link-normal'})
rows = soup.find_all('tr')
films = []
for row in rows[2:]:
    film = dict()
    # area_info = row.find('td', {'class': 'mojo-field-type-area_id'}).find('a')  # first method
    try:
        area_info = row.find('td', {'class': 'mojo-field-type-area_id'}).findChildren()[0] # second method
        film['area'] = [area_info.getText(), area_info.get('href')]
    except:
        film['area'] = None

    try:
        weekend_info =  row.find('td', {'class': 'mojo-field-type-date_interval'}).findChildren()[0]
        film['weekend_info'] = [weekend_info.getText(), weekend_info.get('href')]
    except:
        film['weekend_info'] = None
    
    try:
        film['releases'] = row.find('td', {'class': 'mojo-field-type-positive_integer'}).getText()
        release_info = row.find('td', {'class': 'mojo-field-type-release'}).findChildren()[0]
    except:
        film['releases'] = None

        film['release_info'] = [release_info.getText(), release_info.get('href')]
    try:
        distributor_info = row.find('td', {'class': 'mojo-field-type-studio'}).findChildren()[0]
        film['distributor_info'] = [distributor_info.getText(), distributor_info.get('href')]
    except:
        film['distributor_info'] = None

    try:
        film['place'] = int(row.find('td', {'class': 'mojo-field-type-positive_integer'}).getText())
    except:
        film['place'] = None

    films.append(film)

pprint(films)